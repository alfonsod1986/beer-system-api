import pytest
from app.infrastructure.repositories.in_memory.order import OrderInMemoryRepository
from app.domain.entities.order import OrderEntity


@pytest.fixture
def order_in_memory_repository():
  return OrderInMemoryRepository(
    filepath="app/tests/data/orders.json"
  )

def test_load_data_from_file(domain_orders):
  repository = OrderInMemoryRepository(filepath="app/tests/data/orders.json")

  assert repository.get_all() == domain_orders

def test_load_data_from_file_with_default_value():
  repository = OrderInMemoryRepository()

  orders = repository.get_all()

  assert len(orders) == 0

def test_get_order_by_id(order_in_memory_repository, domain_orders):
  order = order_in_memory_repository.get_by_id(1)

  first, *_ = domain_orders

  assert isinstance(order, OrderEntity) == True
  assert order.id == 1
  assert order == first
  order = order_in_memory_repository.get_by_id(99)

  assert order is None