from abc import ABC, abstractmethod
from app.domain.entities.order import Order
from typing import List

class OrderRepository(ABC):
  @abstractmethod
  def get_all(self) -> List[Order]:
    raise NotImplemented
