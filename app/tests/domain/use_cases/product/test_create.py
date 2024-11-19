from unittest import mock
from app.domain.use_cases.product.create import CreateProductUseCase
from app.domain.entities.product import ProductEntity

def test_create_product():
  repo = mock.Mock()
  repo.create.side_effect = lambda product: product

  product_data = {
    "id": 1,
    "name": "XX Lager",
    "description": "This is a description",
    "price": 15.99,
    "stock": 100
  }

  product_add = ProductEntity.from_dict(product_data)

  create_product_use_case = CreateProductUseCase(repo)


  product = create_product_use_case.execute(product_add)
  assert isinstance(product, ProductEntity)
  assert product.id == 1
  assert product.name == "XX Lager"
  assert product.description == "This is a description"
  assert product.price.value == 15.99
  assert product.stock.value == 100
  assert product.to_dict() == product_data
  repo.create.assert_called_once_with(product_add)