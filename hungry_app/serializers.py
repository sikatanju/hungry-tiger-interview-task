from rest_framework.serializers import ModelSerializer

from .models import Product, Vendor


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'description']


class VendorSerializer(ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['id', 'business_name']