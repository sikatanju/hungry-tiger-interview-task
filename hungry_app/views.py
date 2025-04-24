from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import Product, Vendor, Customer, OrderItem, Order 
from .serializers import ProductSerializer, VendorSerializer, CreateOrderSerializer, OrderSerializer, SimpleOrderSerializer
from .permissions import IsVendorOrReadOnly, IsVendorAndReadOnly, IsCustomerOrReadOnly

class ProductViewSet(ModelViewSet):
    permission_classes = [IsVendorOrReadOnly]
    serializer_class = ProductSerializer
    
    def get_queryset(self):
        return Product.objects.all()

    def create(self, request, *args, **kwargs):
        if request.user.is_vendor and not request.user.is_staff:
            serializer = ProductSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(vendor=Vendor.objects.get(user=request.user))
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        else:
            return Response({"message": "You must be a vendor to create a product"}, status=status.HTTP_400_BAD_REQUEST)
        

class VendorViewSet(ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    permission_classes = [IsVendorAndReadOnly]


class OrderViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, IsCustomerOrReadOnly]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Order.objects.all()
        elif self.request.user.is_customer:
            print('customer from views :)')
            return Order.objects.filter(customer__user=self.request.user).prefetch_related('items__product').select_related('customer__user')
        elif self.request.user.is_vendor:
            print('Vendor from views :)')
            vendor = self.request.user.vendor
            return Order.objects.filter(items__product__vendor=vendor).prefetch_related('items__product').select_related('customer__user').distinct()

    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateOrderSerializer
        
        return OrderSerializer
    

    def get_serializer_context(self):
        if self.request.user.is_customer:
            return {'customer': Customer.objects.get(user=self.request.user)}
         
        return super().get_serializer_context()