from dataclasses import dataclass
from typing import List
from app.domain.value_objects.quantity import Quantity

@dataclass
class OrderItem:
  product_id: int
  quantity: Quantity

@dataclass(kw_only=True)
class Order:
  id: int = None
  items: List[OrderItem]
  discount: float = 0.0
  tax_rate: float = 0.15
  subtotal: float = 0.0
  taxes: float = 0.0
  total: float = 0.0