from dataclasses import dataclass
from typing import List
from app.domain.value_objects.quantity import Quantity

@dataclass
class OrderItemEntity:
  product_id: int
  quantity: Quantity

  @classmethod
  def from_dict(cls, data: dict):
    data_copy = data.copy()

    data_copy["quantity"] = Quantity(data["quantity"])
    return cls(**data_copy)
  
  def to_dict(self) -> dict:
    return {
      "product_id": self.product_id,
      "quantity": self.quantity.value
    }

@dataclass(kw_only=True)
class OrderEntity:
  id: int = None
  items: List[OrderItemEntity]
  discount: float = 0.0
  tax_rate: float = 0.15
  subtotal: float = 0.0
  taxes: float = 0.0
  total: float = 0.0

  @classmethod
  def from_dict(cls, data: dict):
    data_copy = data.copy()

    data_copy["items"] = [OrderItemEntity.from_dict(item) for item in data["items"]]
    return cls(**data_copy)
  
  def to_dict(self) -> dict:
    return {
      "id": self.id,
      "items": [item.to_dict() for item in self.items],
      "discount": self.discount,
      "tax_rate": self.tax_rate,
      "subtotal": self.subtotal,
      "taxes": self.taxes,
      "total": self.total
    }