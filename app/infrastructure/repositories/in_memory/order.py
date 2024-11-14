import pathlib
import json
from typing import List
from app.domain.repositories.order import OrderRepository
from app.domain.entities.order import OrderEntity

class OrderInMemoryRepository(OrderRepository):
  def __init__(self, filepath: str = None):
    self.__orders: List[OrderEntity] = []
    self.__last_id: int = 0
    if filepath:
      self.__load_data(filepath)
  
  def __load_data(self, filepath: str):
    with open(pathlib.Path(filepath), "r") as file:
      self.__orders = [OrderEntity.from_dict(data) for data in json.load(file)]
      self.__last_id = max((order.id for order in self.__orders), default=0)
  
  def get_all(self) -> List[OrderEntity]:
    return self.__orders
  
  def get_by_id(self, id: int) -> OrderEntity | None:
    return next((order for order in self.__orders if order.id == id), None)
  
  def next_id(self) -> int:
    self.__last_id += 1
    return self.__last_id