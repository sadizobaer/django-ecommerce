import pytest

pytestmark = pytest.mark.django_db


class TestCategoryModel:
    def test_str_method(self, category_factory):
        # Arrange
        # Act
        temp_category = category_factory()
        # Assert
        assert temp_category.__str__() == "test_category"


class TestBrandModel:
    def test_str_method(self, brand_factory):
        # Arrange
        # Act
        temp_brand = brand_factory()
        # Assert
        assert temp_brand.__str__() == "test_brand"


class TestProductModel:
    def test_str_method(self, product_factory):
        # Arrange
        # Act
        temp_product = product_factory(name="test_product")
        # Assert
        assert temp_product.__str__() == "test_product"
