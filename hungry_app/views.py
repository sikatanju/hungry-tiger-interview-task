from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser

from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    
    def get_queryset(self):
        if self.request.user.is_staff:
            return Product.objects.all()
        
        return Product.objects.filter(vendor=self.user)
    
    serializer_class = ProductSerializer