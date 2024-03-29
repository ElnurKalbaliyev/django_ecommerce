from django import forms
from .models import Order, OrderProduct

class OrderForm(forms.ModelForm):

    class Meta:
        exclude = ['customer', 'coupon_code', 'copuon_discount', 'accepted', 'delivered', 'created']
        model = Order
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),  
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control'}),  
            'city': forms.TextInput(attrs={'class': 'form-control'}),   
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control'}),  
            'country': forms.Select(attrs={'class': 'custom-select'})  
        }


    def save(self, customer, basketlist, coupon):
        data = self.cleaned_data.copy()
        data['customer'] = customer
        if coupon and coupon.is_valid(customer)[0]:
            data['coupon_code'] = coupon.code
            data['copuon_discount'] = coupon.discount

        order = Order.objects.create(**data)

        ordered_products = []
        for basketitem in basketlist:
            op = OrderProduct(
                order=order,
                title=basketitem.product.title,
                count=basketitem.count,
                price=basketitem.product.price,
                size=basketitem.size.title,
                color=basketitem.color.title,

            )
            ordered_products.append(op)
        OrderProduct.objects.bulk_create(ordered_products)
        basketlist.delete()
        return order  
