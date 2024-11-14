from app.domain.repositories.order import OrderRepository
from app.domain.entities.order import Order
from typing import List

class GetAllOrdersUseCase:
  def __init__(self, repository: OrderRepository):
    self.__repository = repository
  
  def execute(self) -> List[Order]:
    return self.__repository.get_all()