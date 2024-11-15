from app.domain.repositories.order import OrderRepository
from app.domain.entities.order import OrderItemEntity

class GetOrderByIdUseCase:
  def __init__(self, repository: OrderRepository):
    self.__repository = repository
  
  def execute(self, id: int) -> OrderItemEntity | None:
    return self.__repository.get_by_id(id)