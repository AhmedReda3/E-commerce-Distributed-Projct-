from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from order.views import OrderItemViewSet, OrderViewSet
from rest_framework import routers
from product.views import ProductViewSet,CategoryViewSet

router = routers.DefaultRouter()
router.register('api/products', ProductViewSet)
router.register('api/categories', CategoryViewSet)
router.register('api/orders', OrderViewSet)
router.register('api/orderitems', OrderItemViewSet)


urlpatterns = [

    path('', include('core.urls')),
    path('cart/', include('cart.urls')),
    path('products/', include('product.urls')),
    path('order/', include('order.urls')),
    path('admin/', admin.site.urls),
    path('api/auth/', include('rest_framework.urls')),
    path('', include(router.urls)),  # include generated URLs
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)