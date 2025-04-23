from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from .models import Product, Vendor
from .serializers import ProductSerializer, VendorSerializer
from .permissions import IsVendorOrReadOnly, IsAdminAndReadOnly

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
    permission_classes = [IsAdminAndReadOnly]