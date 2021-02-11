from django.urls import include, path
from rest_framework import routers

from .views import CategoryViewSet, ProductViewSet, ColorViewSet

router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet, basename="categories")
router.register(r'colors', ColorViewSet, basename="colors")
router.register(r'products', ProductViewSet, basename="products")

urlpatterns = [
    path('', include(router.urls)),
]
