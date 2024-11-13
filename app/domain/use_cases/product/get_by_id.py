from app.domain.repositories.product import ProductRepository
from app.domain.entities.product import ProductEntity

class GetProductByIdUseCase:
  def __init__(self, repository: ProductRepository):
    self.__repository = repository
  
  def execute(self, id: int) -> ProductEntity | None:
    return self.__repository.get_by_id(id)