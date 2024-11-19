from app.domain.repositories.order import OrderRepository
from app.domain.entities.order import OrderEntity
from typing import List

class GetAllOrdersUseCase:
  def __init__(self, repository: OrderRepository):
    self.__repository = repository
  
  def execute(self) -> List[OrderEntity]:
    return self.__repository.get_all()