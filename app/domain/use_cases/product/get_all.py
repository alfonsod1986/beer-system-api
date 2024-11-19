from app.domain.repositories.product import ProductRepository
from app.domain.entities.product import ProductEntity
from typing import List

class GetAllProductsUseCase:
  def __init__(self, repository: ProductRepository):
    self.__repository = repository
  
  def execute(self) -> List[ProductEntity]:
    return self.__repository.get_all()