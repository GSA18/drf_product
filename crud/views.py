from rest_framework import viewsets

from .models import Category, Product, Color
from .serializers import CategorySerializer, ProductSerializer, CorSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer


class ColorViewSet(viewsets.ModelViewSet):
    queryset = Color.objects.all().order_by('name')
    serializer_class = CorSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('name')
    serializer_class = ProductSerializer
