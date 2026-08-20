from django.urls import path

from apps.home.views import *



urlpatterns = [
    path('', home, name='home'),
    path('product-category/', category_summary_view, name='category-summary'),
    path('product-category/<int:pk>', category_view, name='product-category'),
    path('product/<int:pk>', product_view, name='product'),
    path('about-us', about_us, name='about-us'),
    path('last-offer', last_offer, name='last-offer'),
]