import pathlib
import json
from typing import List
from app.domain.repositories.product import ProductRepository
from app.domain.entities.product import ProductEntity
from app.domain.exceptions import ProductNotFoundError

class ProductInMemoryRepository(ProductRepository):
  def __init__(self, filepath: str = None):
    self.__products: List[ProductEntity] = []
    self.__last_id: int = 0
    if filepath:
      self.__load_data(filepath)
  
  def __load_data(self, filepath: str):
    with open(pathlib.Path(filepath), "r") as file:
      self.__products = [ProductEntity.from_dict(data) for data in json.load(file)]
      self.__last_id = max((product.id for product in self.__products), default=0)
  
  def get_all(self) -> List[ProductEntity]:
    return self.__products
  
  def get_by_id(self, id: int) -> ProductEntity | None:
    return next((product for product in self.__products if product.id == id), None)
  
  def create(self, product: ProductEntity) -> ProductEntity:
    self.__products.append(product)
    self.__last_id = max(self.__last_id, product.id)
    return product
  
  def update(self, id: int, product: ProductEntity):
    founded = self.get_by_id(id)

    if not founded:
      raise ProductNotFoundError(id)
    
    founded.name = product.name
    founded.price = product.price
    founded.stock = product.stock
    return founded

  
  def delete(self, id: int) -> bool:
    product = self.get_by_id(id)
    if not  product:
      raise ProductNotFoundError(id)
    self.__products.remove(product)
    return True
  
  def next_id(self) -> int:
    self.__last_id += 1
    return self.__last_id
