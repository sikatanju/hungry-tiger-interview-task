from rest_framework.routers import DefaultRouter

from . import views as v

router = DefaultRouter()

router.register('products', v.ProductViewSet, basename='products')
router.register('vendors', v.VendorViewSet, basename='vendors')
router.register('orders', v.OrderViewSet, basename='orders')

urlpatterns = [] + router.urls
