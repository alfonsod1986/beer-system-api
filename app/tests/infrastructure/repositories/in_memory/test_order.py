import pytest
from app.infrastructure.repositories.in_memory.order import OrderInMemoryRepository


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