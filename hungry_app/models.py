from django.db import models
from django.conf import settings

# Create your models here.
class Vendor(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False, related_name='vendor')
    business_name = models.CharField(max_length=255)
    

class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False, related_name='customer')
    phone = models.CharField(max_length=14, blank=True)
    address = models.CharField(max_length=512)


class Product(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=False, related_name='products')
    name = models.CharField(max_length=255, null=False, blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=False, blank=False, related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    quantity = models.PositiveSmallIntegerField(default=1)