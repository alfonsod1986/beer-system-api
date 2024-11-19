import pytest
from app.domain.value_objects.stock import Stock

def test_stock_positive_int_value():
  stock = Stock(value=10)
  assert stock.value == 10

@pytest.mark.parametrize("test_input,expected",[
  ("edsdgd", "Stock must be a non-negative integer"),
  (-15, "Stock must be a non-negative integer"),
  ({ "number": 1 }, "Stock must be a non-negative integer"),
])
def test_stock_invalid_value(test_input, expected):
  with pytest.raises(ValueError) as exc_info:
    Stock(value=test_input)
  assert str(exc_info.value) == expected

def test_stock_equality():
  stock_1 = Stock(value=20)
  stock_2 = Stock(value=20)

  assert stock_1 == stock_2

def test_stock_inequality():
  stock_1 = Stock(value=20)
  stock_2 = Stock(value=21)

  assert stock_1 != stock_2