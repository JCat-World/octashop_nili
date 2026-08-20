from django.urls import path

from apps.catalogs.views.site import LastOfferAPIView


urlpatterns = [
    path('product-last-offer/',LastOfferAPIView.as_view(), name="product-last-offer"),
]