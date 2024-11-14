from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from app.domain.entities.product import ProductEntity
from app.domain.exceptions import ProductNotFoundError
from app.infrastructure.rest.fastapi.v1.schemas.product import ProductOutput, ProductInput
from app.infrastructure.container import Container
from app.application.services.product import ProductService

router = APIRouter(
  prefix='/v1/products',
  tags=['Products']
)

@router.get('/', response_model=List[ProductOutput])
@inject
def get_all_products(
  product_service: ProductService = Depends(Provide[Container.product_service])
):
  try:
    products = product_service.get_all()
    return [product.to_dict() for product in products]
  except ValueError as e:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.get('/{product_id}', response_model=ProductOutput)
@inject
def get_product_by_id(
  product_id: int,
  product_service: ProductService = Depends(Provide[Container.product_service])
):
  try:
    product = product_service.get_by_id(product_id)
    if not product:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Product with ID {product_id} not found")
    return product.to_dict()
  except ValueError as e:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
  

@router.post('/', response_model=ProductOutput, status_code=status.HTTP_201_CREATED)
@inject
def create_product(
  product: ProductInput,
  product_service: ProductService = Depends(Provide[Container.product_service])
):
  try:
    product_dict = product.model_dump() 
    created = product_service.create(ProductEntity.from_dict(product_dict))
    return created.to_dict()
  except ValueError as e:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
  except Exception as e:
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.put('/{id}', response_model=ProductOutput)
@inject
def update_product(
  id: int,
  product: ProductInput,
  product_service: ProductService = Depends(Provide[Container.product_service])
):
  try:
    product_dict = product.model_dump() 
    updated = product_service.update(id, ProductEntity.from_dict(product_dict))
    return updated.to_dict()
  except ValueError as e:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
  except ProductNotFoundError as e:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
  except Exception as e:
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
  
@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
@inject
def delete_product(
  id: int,
  product_service: ProductService = Depends(Provide[Container.product_service])
):
  try:
    product_service.delete(id)
  except ValueError as e:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
  except ProductNotFoundError as e:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
  except Exception as e:
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))