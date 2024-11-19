from app.domain.repositories.product import ProductRepository
from app.domain.entities.product import ProductEntity

class DeleteProductUseCase:
  def __init__(self, repository: ProductRepository):
    self.__repository = repository
  
  def execute(self, id: int) -> bool:
    return self.__repository.delete(id)