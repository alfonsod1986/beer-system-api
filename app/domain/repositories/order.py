from abc import ABC, abstractmethod
from app.domain.entities.order import OrderEntity
from typing import List

class OrderRepository(ABC):
  @abstractmethod
  def get_all(self) -> List[OrderEntity]:
    raise NotImplemented
