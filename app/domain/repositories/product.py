from abc import ABC, abstractmethod
from app.domain.entities.product import ProductEntity
from typing import List

class ProductRepository(ABC):
  @abstractmethod
  def get_all(self) -> List[ProductEntity]:
    raise NotImplemented
  
  @abstractmethod
  def get_by_id(self, id: int) -> ProductEntity | None:
    raise NotImplemented
  
  @abstractmethod
  def create(self, product: ProductEntity) -> ProductEntity:
    raise NotImplemented
  
  @abstractmethod
  def update(self, id: int, product: ProductEntity) -> ProductEntity:
    raise NotImplemented
  
  @abstractmethod
  def delete(self, id: int) -> bool:
    raise NotImplemented