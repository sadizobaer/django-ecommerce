import factory
from product.models import Category, Brand, Product


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = "test_category"


class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Brand

    name = "test_brand"


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product
        skip_postgeneration_save = True

    name = "test_product"
    description = "test_description"
    price = 100.00
    discount = 10.00
    brand = factory.SubFactory(BrandFactory)
    category = factory.RelatedFactory(CategoryFactory)
