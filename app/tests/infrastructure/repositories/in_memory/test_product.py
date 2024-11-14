import pytest
from app.infrastructure.repositories.in_memory.product import ProductInMemoryRepository
from app.domain.entities.product import ProductEntity
from app.domain.value_objects.price import Price
from app.domain.value_objects.stock import Stock
from app.domain.exceptions import ProductNotFoundError

@pytest.fixture
def product_in_memory_repository():
  return ProductInMemoryRepository(
    filepath="app/tests/data/products.json"
  )


def test_load_data_from_file(domain_products):
  repository = ProductInMemoryRepository(filepath="app/tests/data/products.json")

  assert repository.get_all() == domain_products

def test_load_data_from_file_with_default_value():
  repository = ProductInMemoryRepository()

  products = repository.get_all()

  assert len(products) == 0

def test_get_product_by_id(product_in_memory_repository):
  product = product_in_memory_repository.get_by_id(1)

  assert isinstance(product, ProductEntity) == True
  assert product.id == 1
  assert product.name == "XX Lager"
  assert product.price.value == 15.99
  assert product.stock.value == 100

  product = product_in_memory_repository.get_by_id(99)

  assert product is None

def test_create_product():
  repository = ProductInMemoryRepository()

  product = ProductEntity(name="Indio", price=Price(22.99), stock=Stock(70))

  created = repository.create(product)

  assert repository.next_id() == 2
  assert created == product

  founded = repository.get_by_id(1)

  assert isinstance(founded, ProductEntity)
  assert founded == created

def test_update_product(product_in_memory_repository):
  product = ProductEntity(name="XX Lager Updated", price=Price(22.99), stock=Stock(70))

  product_updated = product_in_memory_repository.update(id=1, product=product)

  founded = product_in_memory_repository.get_by_id(1)

  assert product_updated == founded

def test_update_product_not_found(product_in_memory_repository):
  with pytest.raises(ProductNotFoundError) as exc_info:
    product = ProductEntity(name="XX Lager Updated", price=Price(22.99), stock=Stock(70))
    product_in_memory_repository.update(id=99, product=product)
  assert str(exc_info.value) == "Product with ID 99 not found"

def test_delete_product(product_in_memory_repository):
  deleted = product_in_memory_repository.delete(1)

  assert deleted == True

  product = product_in_memory_repository.get_by_id(1)

  assert product is None

def test_delete_product_not_found(product_in_memory_repository):
  with pytest.raises(ProductNotFoundError) as exc_info:
    product_in_memory_repository.delete(99)
  assert str(exc_info.value) == "Product with ID 99 not found"

def test_next_id_with_no_products():
  repository = ProductInMemoryRepository()

  assert repository.next_id() == 1
  assert repository.next_id() == 2

def test_next_id_with_products():
  repository = ProductInMemoryRepository(filepath="app/tests/data/products.json")

  assert repository.next_id() == 5
  assert repository.next_id() == 6

def test_next_id_after_create():
  repository = ProductInMemoryRepository()

  product = ProductEntity(name="Indio", price=Price(22.99), stock=Stock(70))

  repository.create(product)

  assert repository.next_id() == 2