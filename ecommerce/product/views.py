from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Category, Brand, Product
from .serializers import CategorySerializer, BrandSerializer, ProductSerializer

# Create your views here.


class CategoryView(viewsets.ViewSet):
    """a simple view for get all categories"""

    queryset = Category.objects.all()

    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response({"data": serializer.data})


class BrandView(viewsets.ViewSet):
    """a simple view for get all brands"""

    queryset = Brand.objects.all()

    def list(self, request):
        serializer = BrandSerializer(self.queryset, many=True)
        return Response({"data": serializer.data})


class ProductView(viewsets.ViewSet):
    """a simple view for get all brands"""

    queryset = Product.objects.all()

    def list(self, request):
        serializer = ProductSerializer(self.queryset, many=True)
        return Response({"data": serializer.data})
