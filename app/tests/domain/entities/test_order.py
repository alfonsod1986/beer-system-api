import random
import pytest
from app.domain.entities.order import OrderItem, Order
from app.domain.value_objects.quantity import Quantity

@pytest.fixture
def order_items():
  return [OrderItem(product_id=random.randint(1, 100), quantity=Quantity(random.randint(1, 100))) for _ in range(10)]

def test_valid_order_item():
  item = OrderItem(product_id=1, quantity=Quantity(10))

  assert item.product_id == 1
  assert item.quantity.value == 10

@pytest.mark.parametrize("test_input,expected",[
  (0, "Quantity must be a positive integer"),
  (-15, "Quantity must be a positive integer"),
  ({ "float": 22.34 }, "Quantity must be a positive integer"),
  (10.5, "Quantity must be a positive integer"),
])
def test_order_item_invalid_quantity(test_input, expected):
  with pytest.raises(ValueError) as exc_info:
    OrderItem(product_id=1, quantity=Quantity(value=test_input))
  assert str(exc_info.value) == expected

def test_valid_order(order_items):
  order = Order(id=1, items=order_items)

  assert order.id == 1
  assert len(order.items) == 10
  assert order.discount == 0.0
  assert order.tax_rate == 0.15
  assert order.subtotal == 0.0
  assert order.taxes == 0.0
  assert order.total == 0.0