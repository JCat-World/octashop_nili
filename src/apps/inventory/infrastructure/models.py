from django.db import models


# Create your models here.

class StockRecord(models.Model):
    product = models.ForeignKey('catalogs.Product', on_delete=models.CASCADE, related_name='stockrecords')
    sku = models.CharField(max_length=64, null=True, blank=True, unique=True)
    buy_price = models.PositiveBigIntegerField(null=True, blank=True)
    sale_price = models.PositiveBigIntegerField()
    in_offer = models.BooleanField(default=False)
    offer_price =  models.PositiveBigIntegerField(null=True, blank=True)
    num_stock = models.PositiveIntegerField(default=0)
    threshold_low_stack = models.PositiveIntegerField(null=True, blank=True)
    
    
    
    class Meta:
      verbose_name = 'Stock Record'
      verbose_name_plural = 'Stock Records'

    def __str__(self):
      return self.product.title