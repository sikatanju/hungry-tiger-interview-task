from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model

from .models import Product, Vendor, OrderItem, Order, Customer


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'description']


class VendorSerializer(ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['id', 'business_name']


class CreateOrderItemSerializer(ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity', 'sale_price']


class CreateOrderSerializer(ModelSerializer):
    items = CreateOrderItemSerializer(many=True)
    class Meta:
        model = Order
        fields = ['total_price', 'items']

    def create(self, validated_data):
        order_items = validated_data.pop('items')
        customer = self.context['customer']
        order = Order(customer=customer, total_price=validated_data['total_price'])
        order.save()
        for item in order_items:
            OrderItem.objects.create(order=order, **item)

        return order
    

class SimpleProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description']


class SimpleUserSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name']


class SimpleCustomerSerializer(ModelSerializer):
    user = SimpleUserSerializer()   
    class Meta:
        model = Customer
        fields = ['id', 'address', 'user']


class OrderItemSerializer(ModelSerializer):
    product = SimpleProductSerializer()
    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity', 'sale_price']


class OrderSerializer(ModelSerializer):
    customer = SimpleCustomerSerializer()
    items = OrderItemSerializer(many=True)
    class Meta:
        model = Order
        fields = ['id', 'total_price', 'customer', 'items']


class SimpleOrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'total_price']