from django.urls import path
from .views import CategoryView, BrandView, ProductView


urlpatterns = [
    path("categories/", view=CategoryView.as_view({"get": "list"})),
    path("brands/", view=BrandView.as_view({"get": "list"})),
    path("products/", view=ProductView.as_view({"get": "list"})),
]
