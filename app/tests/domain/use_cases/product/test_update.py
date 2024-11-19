from unittest import mock
from app.domain.use_cases.product.update import UpdateProductUseCase
from app.domain.entities.product import ProductEntity

def test_update_product():
  repo = mock.Mock()
  repo.update.side_effect = lambda id, product: product

  product_data = {
    "id": 1,
    "name": "XX Lager",
    "description": "This is a description",
    "price": 15.99,
    "stock": 100
  }

  product_update = ProductEntity.from_dict(product_data)

  update_product_use_case = UpdateProductUseCase(repo)


  product = update_product_use_case.execute(1, product_update)
  assert isinstance(product, ProductEntity)
  assert product.id == 1
  assert product.name == "XX Lager"
  assert product.description == "This is a description"
  assert product.price.value == 15.99
  assert product.stock.value == 100
  assert product.to_dict() == product_data
  repo.update.assert_called_once_with(1, product_update)