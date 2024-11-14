from typing import List
from app.domain.use_cases.order.get_all import GetAllOrdersUseCase
from app.domain.entities.order import OrderEntity

class OrderService:
  def __init__(
    self,
    get_all_orders_use_case: GetAllOrdersUseCase,
  ):
    self.__get_all_orders_use_case = get_all_orders_use_case
  
  def get_all(self) -> List[OrderEntity]:
   return self.__get_all_orders_use_case.execute()
