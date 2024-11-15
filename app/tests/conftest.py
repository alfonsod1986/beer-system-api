import pytest
import pathlib
import json
from typing import List
from fastapi.testclient import TestClient
from unittest.mock import Mock
from app.domain.entities.product import ProductEntity
from app.domain.entities.order import OrderEntity
from app.infrastructure.rest.fastapi.api import create_app


@pytest.fixture
def domain_products() -> List[ProductEntity]:
  filepath = pathlib.Path("app/tests/data/products.json") 
  with open(filepath, "r") as file:
    return [ProductEntity.from_dict(data) for data in json.load(file)]

@pytest.fixture
def domain_orders() -> List[OrderEntity]:
  filepath = pathlib.Path("app/tests/data/orders.json") 
  with open(filepath, "r") as file:
    return [OrderEntity.from_dict(data) for data in json.load(file)]

@pytest.fixture
def mock_product_repository(domain_products):
    product_repository = Mock()
    product_repository.get_all = Mock(return_value=domain_products)
    product_repository.get_by_id = Mock(side_effect=lambda id: next((p for p in domain_products if p.id == id), None))
    product_repository.create = Mock()
    product_repository.update = Mock()
    product_repository.delete = Mock(return_value=True)
    return product_repository

@pytest.fixture
def mock_order_repository(domain_orders):
  order_repository = Mock()
  order_repository.get_all = Mock(return_value=domain_orders)
  return order_repository

@pytest.fixture
def client(mock_product_repository, mock_order_repository):
    app = create_app()
    app.container.product_repository.override(mock_product_repository)
    app.container.order_repository.override(mock_order_repository)

    return TestClient(app)