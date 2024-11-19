import pytest
from unittest.mock import Mock
from app.application.services.order import OrderService
from app.domain.entities.order import OrderEntity

@pytest.fixture
def mock_use_cases():
  return {    
    "get_all_orders": Mock(),
    "get_order_by_id": Mock(),
  }

@pytest.fixture
def order_service(mock_use_cases):
  return OrderService(
    get_all_orders_use_case=mock_use_cases["get_all_orders"],
    get_order_by_id_use_case=mock_use_cases["get_order_by_id"],
  )


def test_get_all_orders(order_service, mock_use_cases, domain_orders):
  mock_use_cases["get_all_orders"].execute.return_value = domain_orders

  orders = order_service.get_all()

  assert len(orders) == 3
  assert orders == domain_orders
  assert orders[0].id == 1
  mock_use_cases["get_all_orders"].execute.assert_called_once()

def test_get_order_by_id(order_service, mock_use_cases, domain_orders):
  mock_use_cases["get_order_by_id"].execute.side_effect = lambda id: next((o for o in domain_orders if o.id == id), None)
  first, *_ = domain_orders
  
  order = order_service.get_by_id(1)

  assert isinstance(order, OrderEntity) == True
  assert order.id == first.id
  assert order.created == first.created
  assert order.paid == first.paid
  assert order.items == first.items
  assert order.rounds == first.rounds
  assert order.discount == first.discount
  assert order.taxes == first.taxes
  assert order.subtotal == first.subtotal
  assert order.total == first.total
  mock_use_cases["get_order_by_id"].execute.assert_called_once_with(1)

def test_get_order_by_id_none(order_service, mock_use_cases, domain_orders):
  mock_use_cases["get_order_by_id"].execute.side_effect = lambda id: next((o for o in domain_orders if o.id == id), None)
  
  order = order_service.get_by_id(99)

  assert order is None
  mock_use_cases["get_order_by_id"].execute.assert_called_once_with(99)