import pytest
from app.domain.value_objects.quantity import Quantity

def test_quantity_positive_int_value():
  quantity = Quantity(value=10)
  assert quantity.value == 10

@pytest.mark.parametrize("test_input,expected",[
  ("edsdgd", "Quantity must be a positive integer"),
  (-15, "Quantity must be a positive integer"),
  ({ "number": 1 }, "Quantity must be a positive integer"),
  (10.1, "Quantity must be a positive integer"),
])
def test_quantity_invalid_value(test_input, expected):
  with pytest.raises(ValueError) as exc_info:
    Quantity(value=test_input)
  assert str(exc_info.value) == expected

def test_quantity_equality():
  quantity_1 = Quantity(value=20)
  quantity_2 = Quantity(value=20)

  assert quantity_1 == quantity_2

def test_quantity_inequality():
  quantity_1 = Quantity(value=20)
  quantity_2 = Quantity(value=21)

  assert quantity_1 != quantity_2