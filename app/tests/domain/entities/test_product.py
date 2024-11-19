import pytest
from app.domain.entities.product import ProductEntity
from app.domain.value_objects.price import Price
from app.domain.value_objects.stock import Stock

def test_valid_product():
  product = ProductEntity(id=1, name="XX Lager", price=Price(value=20.95), stock=Stock(value=100))
  assert product.id == 1
  assert product.name == "XX Lager"
  assert product.price.value == 20.95
  assert product.stock.value == 100

@pytest.mark.parametrize("test_input,expected",[
  (0, "Price must be a positive float"),
  (-15, "Price must be a positive float"),
  ({ "float": 22.34 }, "Price must be a positive float"),
])
def test_product_invalid_price(test_input, expected):
  with pytest.raises(ValueError) as exc_info:
    ProductEntity(id=2, name="Heineken", price=Price(value=test_input), stock=Stock(value=10))
  assert str(exc_info.value) == expected

@pytest.mark.parametrize("test_input,expected",[
  ("edsdgd", "Stock must be a non-negative integer"),
  (-15, "Stock must be a non-negative integer"),
  ({ "number": 1 }, "Stock must be a non-negative integer"),
])
def test_product_invalid_stock(test_input, expected):
  with pytest.raises(ValueError) as exc_info:
    ProductEntity(id=3, name="Corona", price=Price(value=11.95), stock=Stock(value=test_input))
  assert str(exc_info.value) == expected

def test_product_to_dict():
  product = ProductEntity(id=4, name="Tecate", price=Price(15.99), stock=Stock(30))
  product_dict = product.to_dict()
  assert product_dict == {
    "id": 4,
    "name": "Tecate",
    "description": None,
    "price": 15.99,
    "stock": 30
  }

def test_product_from_dict():
  product_dict = {
    "id": 5,
    "name": "Modelo",
    "description": None,
    "price": 15.99,
    "stock": 30
  }

  product = ProductEntity.from_dict(product_dict)

  assert isinstance(product, ProductEntity) == True
  assert product.id == product_dict["id"]
  assert product.name == product_dict["name"]
  assert product.description == product_dict["description"]
  assert product.price.value == product_dict["price"]
  assert product.stock.value == product_dict["stock"]
  assert product.to_dict() == product_dict