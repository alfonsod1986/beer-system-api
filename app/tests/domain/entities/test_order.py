import random
import pytest
from datetime import datetime
from app.domain.entities.order import (
  ProductItemEntity,
  RoundItemEntity,
  OrderItemEntity,
  OrderEntity
)
from app.domain.value_objects.price import Price
from app.domain.value_objects.quantity import Quantity
from app.domain.value_objects.total import Total

@pytest.fixture
def order_items():
  return [
    OrderItemEntity(
      name=f"Testing {random.randint(1, 100)}",
      price_per_unit=Price(random.randint(1, 100)),
      quantity=Quantity(random.randint(1, 100)),
      total=Total(random.randint(1, 100)))
    for _ in range(10)]

@pytest.fixture
def product_items():
  return [
    ProductItemEntity(
      name=f"Testing {random.randint(1, 100)}",
      quantity=Quantity(random.randint(1, 100)),
    )
    for _ in range(10)
  ]

@pytest.fixture
def round_items(product_items):
  created = datetime.strptime("2024-11-15T05:53:42.900906Z", "%Y-%m-%dT%H:%M:%S.%fZ")
  return [
    RoundItemEntity(
      created=created,
      items=product_items,
    )
    for _ in range(10)
  ]


def test_valid_order_item():
  item = OrderItemEntity(
    name="Testing",
    price_per_unit=Price(10),
    quantity=Quantity(10),
    total=Total(100))

  assert item.name == "Testing"
  assert item.price_per_unit.value == 10
  assert item.total.value == 100

@pytest.mark.parametrize("test_input,expected",[
  (0, "Price must be a positive float"),
  (-15, "Price must be a positive float"),
  ({ "float": 22.34 }, "Price must be a positive float"),
])
def test_order_item_invalid_price(test_input, expected):
  with pytest.raises(ValueError) as exc_info:
    OrderItemEntity(name="Testing", price_per_unit=Price(value=test_input), total=Total(100))
  assert str(exc_info.value) == expected

def test_order_item_to_dict():
  item = OrderItemEntity(
    name="Testing",
    price_per_unit=Price(10),
    quantity=Quantity(10),
    total=Total(10))
  item_dict = item.to_dict()

  assert item_dict == {
    "name": "Testing",
    "price_per_unit": 10,
    "quantity": 10,
    "total": 10
  }

def test_order_item_from_dict():
  item_dict = {
    "name": "Testing",
    "price_per_unit": 10,
    "quantity": 10,
    "total": 10
  }

  item = OrderItemEntity.from_dict(item_dict)

  assert isinstance(item, OrderItemEntity) == True
  assert item.name == item_dict["name"]
  assert item.price_per_unit.value == item_dict["price_per_unit"]
  assert item.quantity.value == item_dict["quantity"]
  assert item.total.value == item_dict["total"]
  assert item.to_dict() == item_dict

def test_valid_product_item():
  item = ProductItemEntity(
    name="Testing",
    quantity=Quantity(10),
  )

  assert item.name == "Testing"
  assert item.quantity.value == 10

@pytest.mark.parametrize("test_input,expected",[
  (0, "Quantity must be a positive integer"),
  (-15, "Quantity must be a positive integer"),
  ({ "float": 22.34 }, "Quantity must be a positive integer"),
  (10.99, "Quantity must be a positive integer"),
])
def test_product_item_invalid_quantity(test_input, expected):
  with pytest.raises(ValueError) as exc_info:
    ProductItemEntity(name="Testing", quantity=Quantity(test_input))
  assert str(exc_info.value) == expected

def test_product_item_to_dict():
  item = ProductItemEntity(name="Testing", quantity=Quantity(10))
  item_dict = item.to_dict()

  assert item_dict == {
    "name": "Testing",
    "quantity": 10
  }

def test_product_item_from_dict():
  item_dict = {
    "name": "Testing",
    "quantity": 10
  }

  item = ProductItemEntity.from_dict(item_dict)

  assert isinstance(item, ProductItemEntity) == True
  assert item.name == item_dict["name"]
  assert item.quantity.value == item_dict["quantity"]
  assert item.to_dict() == item_dict

def test_valid_round_item(product_items):
  created = datetime.strptime("2024-11-15T05:53:42.900906Z", "%Y-%m-%dT%H:%M:%S.%fZ")
  item = RoundItemEntity(
    created=created,
    items=product_items
  )

  assert item.created == created
  assert item.items == product_items

def test_round_item_to_dict(product_items):
  created = datetime.strptime("2024-11-15T05:53:42.900906Z", "%Y-%m-%dT%H:%M:%S.%fZ")
  item = RoundItemEntity(
    created=created,
    items=product_items
  )
  item_dict = item.to_dict()

  assert item_dict == {
    "created": "2024-11-15T05:53:42.900906Z",
    "items": [p_item.to_dict() for p_item in product_items]
  }

def test_round_item_from_dict(product_items):
  item_dict = {
    "created": "2024-11-15T05:53:42.900906Z",
    "items": [p_item.to_dict() for p_item in product_items]
  }

  item = RoundItemEntity.from_dict(item_dict)

  assert isinstance(item, RoundItemEntity) == True
  assert item.created == datetime.strptime("2024-11-15T05:53:42.900906Z", "%Y-%m-%dT%H:%M:%S.%fZ")
  assert item.items == product_items
  assert item.to_dict() == item_dict

def test_valid_order(order_items, round_items):
  order = OrderEntity(id=1, items=order_items, rounds=round_items)

  assert order.id == 1
  assert len(order.items) == 10
  assert order.discount == 0.0
  assert order.tax_rate == 0.15
  assert order.subtotal == 0.0
  assert order.taxes == 0.0
  assert order.total == 0.0

def test_order_to_dict(order_items, round_items):
  created = datetime.strptime("2024-11-15T05:53:42.900906Z", "%Y-%m-%dT%H:%M:%S.%fZ")
  order = OrderEntity(id=1, created=created, items=order_items, rounds=round_items)
  order_dict = order.to_dict()

  print(order_dict)

  assert order_dict == {
    "id": 1,
    "created": "2024-11-15T05:53:42.900906Z",
    "paid": False,
    "items": [item.to_dict() for item in order_items],
    "rounds": [item.to_dict() for item in round_items],
    "discount": 0.0,
    "tax_rate": 0.15,
    "subtotal": 0.0,
    "taxes": 0.0,
    "total": 0.0
  }

def test_order_from_dict(order_items, round_items):
  order_dict = {
    "id": 1,
    "created": "2024-11-15T05:53:42.900906Z",
    "items": [item.to_dict() for item in order_items],
    "rounds": [r_item.to_dict() for r_item in round_items],
    "discount": 0.0,
    "tax_rate": 0.15,
    "subtotal": 0.0,
    "taxes": 0.0,
    "total": 0.0
  }

  order = OrderEntity.from_dict(order_dict)

  assert isinstance(order, OrderEntity) == True
  assert len(order.items) == len(order_dict["items"])
  assert order.items == order_items
  assert len(order.rounds) == len(order_dict["rounds"])
  assert order.rounds == round_items
  assert order.discount == order_dict["discount"]
  assert order.tax_rate == order_dict["tax_rate"]
  assert order.subtotal == order_dict["subtotal"]
  assert order.taxes == order_dict["taxes"]
  assert order.total == order_dict["total"]
