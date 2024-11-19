from typing import List
from app.domain.use_cases.order.get_all import GetAllOrdersUseCase
from app.domain.use_cases.order.get_by_id import GetOrderByIdUseCase
from app.domain.entities.order import OrderEntity

class OrderService:
  def __init__(
    self,
    get_all_orders_use_case: GetAllOrdersUseCase,
    get_order_by_id_use_case: GetOrderByIdUseCase,
  ):
    self.__get_all_orders_use_case = get_all_orders_use_case
    self.__get_order_by_id_use_case = get_order_by_id_use_case
  
  def get_all(self) -> List[OrderEntity]:
   return self.__get_all_orders_use_case.execute()
  
  def get_by_id(self, id: int) -> OrderEntity | None:
    return self.__get_order_by_id_use_case.execute(id)