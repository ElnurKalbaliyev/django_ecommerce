from django.urls import path
from . import views


urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('basket/', views.basket, name='basket'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),

]
