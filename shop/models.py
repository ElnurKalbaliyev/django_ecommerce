from django.db import models

# Create your models here.


class Size(models.Model):
    title = models.CharField(max_length=10)
    
    def __str__(self):
        return self.title
    
    

class Color(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

class GeneralCategory(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to='categories')
    general_category = models.ForeignKey(GeneralCategory, on_delete=models.SET_NULL, null=True, blank=True, related_name='sub_categories')

    def __str__(self):
        return self.title
    

class Campaign(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    is_slide = models.BooleanField(default=False)
    image = models.ImageField(upload_to='campaigns')
    discount = models.FloatField()

    def __str__(self):
        return self.title


class Products(models.Model):
    title = models.CharField(max_length=100)
    old_price = models.FloatField(null=True, blank=True)
    price = models.FloatField()
    description = models.TextField()
    sizes = models.ManyToManyField(Size, related_name='products')
    colors = models.ManyToManyField(Color, related_name='products')
    categories = models.ManyToManyField(Category, related_name='products')
    campaigns = models.ManyToManyField(Campaign, related_name='products')
    update = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class ProductImages(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images')