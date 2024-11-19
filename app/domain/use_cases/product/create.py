from app.domain.repositories.product import ProductRepository
from app.domain.entities.product import ProductEntity

class CreateProductUseCase:
  def __init__(self, repository: ProductRepository):
    self.__repository = repository
  
  def execute(self, product: ProductEntity) -> ProductEntity:
    return self.__repository.create(product)