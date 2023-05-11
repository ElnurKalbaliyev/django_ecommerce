from django.shortcuts import render
from .models import Campaign, Category
from django.db.models import Count

# Create your views here.


def home(request):
    slide_campaigns = Campaign.objects.filter(is_slide=True)[:3]
    nonslide_campaigns = Campaign.objects.filter(is_slide=False)[:4]
    categories = Category.objects.annotate(product_count=Count('products'))
    return render(request, 'home.html', {
        'slide_campaigns': slide_campaigns,
        'nonslide_camapigns': nonslide_campaigns,
        'categories': categories,
    })



def product_list(request):
    return render(request, 'product-list.html')


def product_detail(request, pk):
    return render(request, 'product-detail.html')