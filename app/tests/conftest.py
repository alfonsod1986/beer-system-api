import pytest
import pathlib
import json
from app.domain.entities.product import ProductEntity

@pytest.fixture
def domain_products():
  filepath = pathlib.Path("app/tests/data/products.json") 
  with open(filepath, "r") as file:
    return [ProductEntity.from_dict(data) for data in json.load(file)]