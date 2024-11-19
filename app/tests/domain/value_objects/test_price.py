import pytest
from app.domain.value_objects.price import Price

def test_price_positive_float_value():
  price = Price(value=15.99)
  assert price.value == 15.99

@pytest.mark.parametrize("test_input,expected",[
  (0, "Price must be a positive float"),
  (-15, "Price must be a positive float"),
])
def test_price_invalid_value(test_input, expected):
  with pytest.raises(ValueError) as exc_info:
    Price(value=test_input)
  assert str(exc_info.value) == expected

def test_price_equality():
  price_1 = Price(value=11.45)
  price_2 = Price(value=11.45)

  assert price_1 == price_2

def test_price_inequality():
  price_1 = Price(value=10.45)
  price_2 = Price(value=11.45)

  assert price_1 != price_2