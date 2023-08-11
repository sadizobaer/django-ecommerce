from rest_framework import serializers
from .models import Category, Brand, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    brand_name = serializers.CharField(source="brand.name", read_only=True)
    category_names = serializers.SerializerMethodField()

    class Meta:
        model = Product
        exclude = ("brand", "category")
        extra_fields = ["brand_name", "category_names"]

    def get_category_names(self, obj):
        return obj.category.values_list("name", flat=True)
