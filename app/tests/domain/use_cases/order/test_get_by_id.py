from unittest import mock
from app.domain.use_cases.order.get_by_id import GetOrderByIdUseCase

def test_order_by_id_founded(domain_orders):
  repo = mock.Mock()
  repo.get_by_id.side_effect = lambda id: next((p for p in domain_orders if p.id == id), None)

  get_order_by_id_use_case = GetOrderByIdUseCase(repo)
  result = get_order_by_id_use_case.execute(1)

  repo.get_by_id.assert_called_with(1)
  assert result == domain_orders[0]

def test_order_by_id_none(domain_orders):
  repo = mock.Mock()
  repo.get_by_id.side_effect = lambda id: next((p for p in domain_orders if p.id == id), None)

  get_order_by_id_use_case = GetOrderByIdUseCase(repo)
  result = get_order_by_id_use_case.execute(15)

  repo.get_by_id.assert_called_with(15)
  assert result == None
