from rest_framework.routers import DefaultRouter

from django.urls import path
from . import views as v

router = DefaultRouter()
router.register('products', v.ProductViewSet, basename='products')
router.register('vendors', v.VendorViewSet, basename='vendors')

urlpatterns = [
    # path('hello/', v.hello, name='hello')
] + router.urls
