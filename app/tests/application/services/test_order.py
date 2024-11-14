import pytest
from unittest.mock import Mock
from app.application.services.order import OrderService
from app.domain.entities.order import OrderEntity

@pytest.fixture
def mock_use_cases():
  return {    
    "get_all_orders": Mock(),
  }

@pytest.fixture
def order_service(mock_use_cases):
  return OrderService(
    get_all_orders_use_case=mock_use_cases["get_all_orders"],
  )


def test_get_all_orders(order_service, mock_use_cases, domain_orders):
  mock_use_cases["get_all_orders"].execute.return_value = domain_orders

  orders = order_service.get_all()

  assert len(orders) == 3
  assert orders == domain_orders
  assert orders[0].id == 1
  mock_use_cases["get_all_orders"].execute.assert_called_once()
