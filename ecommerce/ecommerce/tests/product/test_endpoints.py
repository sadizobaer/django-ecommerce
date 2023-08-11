import pytest
import json

pytestmark = pytest.mark.django_db


class TestCategoryEndpoint:
    end_point = "/api/categories/"

    def test_category_get(self, category_factory, api_client):
        # Arrange
        category_factory()
        # Act
        response = api_client().get(self.end_point)
        # Assert
        assert response.status_code == 200


class TestBrandEndpoint:
    end_point = "/api/brands/"

    def test_brand_get(self, brand_factory, api_client):
        # Arrange
        brand_factory()
        # Act
        response = api_client().get(self.end_point)
        # Assert
        assert response.status_code == 200


class TestProductEndpoint:
    end_point = "/api/products/"

    def test_product_get(self, product_factory, api_client):
        # Arrange
        product_factory()
        # Act
        response = api_client().get(self.end_point)
        # Assert
        assert response.status_code == 200
