from fastapi import status
from app.domain.entities.product import ProductEntity
from app.domain.value_objects.price import Price
from app.domain.value_objects.stock import Stock
from app.domain.exceptions import ProductNotFoundError

def test_get_all_products(client, mock_product_repository, domain_products):
  response = client.get("/v1/products")
  products = response.json()

  assert response.status_code == status.HTTP_200_OK
  assert isinstance(products, list)
  assert len(products) == 4
  assert products == [p.to_dict() for p in domain_products]
  mock_product_repository.get_all.assert_called_once()

def test_get_product_by_id(client, mock_product_repository, domain_products):
  response = client.get("/v1/products/1")
  product = response.json()

  assert response.status_code == status.HTTP_200_OK
  assert isinstance(product, dict)
  assert product == domain_products[0].to_dict()
  mock_product_repository.get_by_id.assert_called_once_with(1)

def test_get_product_by_id_not_found(client, mock_product_repository):
  response = client.get("/v1/products/999")
  detail = response.json()["detail"]

  assert response.status_code == status.HTTP_404_NOT_FOUND
  assert detail == "Product with ID 999 not found"
  mock_product_repository.get_by_id.assert_called_once_with(999)

def test_create_product(client, mock_product_repository):
  product_created = ProductEntity(
    id=1,
    name="Testing",
    description="Testing description",
    price=Price(15.99),
    stock=Stock(100))
  
  mock_product_repository.create.return_value = product_created

  product_data = {
    "name": "Testing",
    "description": "Testing description",
    "price": 15.99,
    "stock": 100
  }

  response = client.post("/v1/products", json=product_data)
  product = response.json()

  assert response.status_code == status.HTTP_201_CREATED
  assert product == product_created.to_dict()
  mock_product_repository.create.assert_called_once_with(ProductEntity.from_dict(product_data))

def test_update_product(client, mock_product_repository):
  product_updated = ProductEntity(
    id=1,
    name="Testing",
    description="Testing description",
    price=Price(15.99),
    stock=Stock(100))
  
  mock_product_repository.update.return_value = product_updated

  product_data = {
    "name": "Testing",
    "description": "Testing description",
    "price": 15.99,
    "stock": 100
  }

  response = client.put("/v1/products/1", json=product_data)
  product = response.json()

  assert response.status_code == status.HTTP_200_OK
  assert product == product_updated.to_dict()
  mock_product_repository.update.assert_called_once_with(1, ProductEntity.from_dict(product_data))

def test_get_product_update_not_found(client, mock_product_repository):
  mock_product_repository.update.side_effect = ProductNotFoundError(999)

  product_data = {
    "name": "Testing",
    "description": "Testing description",
    "price": 15.99,
    "stock": 100
  }

  response = client.put("/v1/products/1", json=product_data)
  detail = response.json()['detail']

  assert response.status_code == status.HTTP_404_NOT_FOUND
  assert detail == "Product with ID 999 not found"

def test_delete_product(client, mock_product_repository):
   response = client.delete("/v1/products/1")

   assert response.status_code == status.HTTP_204_NO_CONTENT
   mock_product_repository.delete.assert_called_once_with(1)

def test_delete_product_not_found(client, mock_product_repository):
  mock_product_repository.delete.side_effect = ProductNotFoundError(999)

  response = client.delete("/v1/products/999")

  assert response.status_code == status.HTTP_404_NOT_FOUND
  detail = response.json()['detail']
  assert detail == "Product with ID 999 not found"