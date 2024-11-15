from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from app.infrastructure.rest.fastapi.v1.schemas.order import OrderOutput
from app.infrastructure.container import Container
from app.application.services.order import OrderService

router = APIRouter(
  prefix='/v1/orders',
  tags=['Orders']
)

@router.get('/', response_model=List[OrderOutput])
@inject
def get_all_orders(
  order_service: OrderService = Depends(Provide[Container.order_service])
):
  try:
    orders = order_service.get_all()
    return [order.to_dict() for order in orders]
  except ValueError as e:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.get('/{order_id}', response_model=OrderOutput)
@inject
def get_order_by_id(
  order_id: int,
  order_service: OrderService = Depends(Provide[Container.order_service])
):
  try:
    order = order_service.get_by_id(order_id)
    if not order:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Order with ID {order_id} not found")
    return order.to_dict()
  except ValueError as e:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))