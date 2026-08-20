
from django.db import models
from django.contrib.auth import get_user_model
from apps.catalogs.infrastructure.models import Product


User = get_user_model()

class OrderGroup(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, default='', blank=True)
    phone_number = models.CharField(max_length=20)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('shipped', 'Shipped'), ('delivered', 'Delivered')], default='pending')
    
    def __str__(self):
        return f"Order Group {self.id} for {self.customer.username}"


class Order(models.Model):
    order_group = models.ForeignKey(OrderGroup, on_delete=models.CASCADE, related_name="orders")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
      return self.product.title
    
    