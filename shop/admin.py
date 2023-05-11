from django.contrib import admin
from .models import Size, Color, GeneralCategory, Category, Campaign, Products, ProductImages


# Register your models here.



admin.site.register(Size)
admin.site.register(Color)
admin.site.register(GeneralCategory)
admin.site.register(Category)
admin.site.register(Campaign)
admin.site.register(Products)
admin.site.register(ProductImages)