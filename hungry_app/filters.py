from django_filters.rest_framework import FilterSet, CharFilter
from .models import Product

class ProductFilter(FilterSet):
    name = CharFilter(lookup_expr='icontains')

    class Meta:
        model = Product
        fields = {
            'price': ['gt', 'lt']
        }