import pytest
from unittest.mock import Mock
from app.application.services.product import ProductService
from app.domain.entities.product import ProductEntity
from app.domain.value_objects.price import Price
from app.domain.value_objects.stock import Stock

@pytest.fixture
def mock_use_cases():
  return {    
    "get_all_products": Mock(),
    "get_product_by_id": Mock(),
    "create_product": Mock(),
    "update_product": Mock(),
    "delete_product": Mock(),
  }

@pytest.fixture
def product_service(mock_use_cases):
  return ProductService(
    get_all_products_use_case=mock_use_cases["get_all_products"],
    get_product_by_id_use_case=mock_use_cases["get_product_by_id"],
    create_product_use_case=mock_use_cases["create_product"],
    update_product_use_case=mock_use_cases["update_product"],
    delete_product_use_case=mock_use_cases["delete_product"],
  )

def test_get_all_products(product_service, mock_use_cases, domain_products):
  mock_use_cases["get_all_products"].execute.return_value = domain_products

  products = product_service.get_all()

  assert len(products) == 4
  assert products == domain_products
  assert products[0].name == "XX Lager"
  assert products[0].price.value == 15.99
  assert products[0].stock.value == 100
  mock_use_cases["get_all_products"].execute.assert_called_once()

def test_get_product_by_id(product_service, mock_use_cases, domain_products):
  mock_use_cases["get_product_by_id"].execute.side_effect = lambda id: next((p for p in domain_products if p.id == id), None)

  product = product_service.get_by_id(1)

  assert isinstance(product, ProductEntity) == True
  assert product.id == 1
  assert product.name == "XX Lager"
  assert product.price.value == 15.99
  assert product.stock.value == 100
  mock_use_cases["get_product_by_id"].execute.assert_called_once_with(1)

def test_create_product(product_service, mock_use_cases):
  product_return = ProductEntity(
    id=1, name="XX Lager", price=Price(15.99), stock=Stock(100)
  )

  mock_use_cases["create_product"].execute.return_value = product_return

  product = product_service.create(product_return)

  assert isinstance(product, ProductEntity) == True
  assert product.id == 1
  assert product.name == "XX Lager"
  assert product.price.value == 15.99
  assert product.stock.value == 100
  mock_use_cases["create_product"].execute.assert_called_once_with(product_return)

def test_update_product(product_service, mock_use_cases):
  product_return = ProductEntity(
    id=1, name="XX Lager Updated", price=Price(20.99), stock=Stock(300)
  )

  mock_use_cases["update_product"].execute.return_value = product_return

  product = product_service.update(1, product_return)

  assert isinstance(product, ProductEntity) == True
  assert product.id == 1
  assert product.name == "XX Lager Updated"
  assert product.price.value == 20.99
  assert product.stock.value == 300
  mock_use_cases["update_product"].execute.assert_called_once_with(1, product_return)

def test_delete_product(product_service, mock_use_cases):
  mock_use_cases["delete_product"].execute.return_value = True

  result = product_service.delete(1)

  assert result == True
  mock_use_cases["delete_product"].execute.assert_called_once_with(1)