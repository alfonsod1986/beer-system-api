from app.domain.repositories.product import ProductRepository
from app.domain.entities.product import ProductEntity

class UpdateProductUseCase:
  def __init__(self, repository: ProductRepository):
    self.__repository = repository
  
  def execute(self, id: int, product: ProductEntity) -> ProductEntity:
    return self.__repository.update(id, product)