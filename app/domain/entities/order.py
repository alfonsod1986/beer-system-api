from datetime import datetime
from dataclasses import dataclass, field
from typing import List
from app.domain.value_objects.price import Price
from app.domain.value_objects.total import Total
from app.domain.value_objects.quantity import Quantity

@dataclass(kw_only=True)
class OrderItemEntity:
  name: str
  price_per_unit: Price
  total: Total

  @classmethod
  def from_dict(cls, data: dict):
    data_copy = data.copy()

    data_copy["price_per_unit"] = Price(data["price_per_unit"])
    data_copy["total"] = Total(data["total"])
    return cls(**data_copy)
  
  def to_dict(self) -> dict:
    return {
      "name": self.name,
      "price_per_unit": self.price_per_unit.value,
      "total": self.total.value
    }

@dataclass(kw_only=True)
class ProductItemEntity:
  name: str
  quantity: Quantity

  @classmethod
  def from_dict(cls, data: dict):
    data_copy = data.copy()

    data_copy["quantity"] = Quantity(data["quantity"])
    return cls(**data_copy)
  
  def to_dict(self) -> dict:
    return {
      "name": self.name,
      "quantity": self.quantity.value
    }

@dataclass(kw_only=True)
class RoundItemEntity:
  created: datetime = datetime.now()
  items: List[ProductItemEntity] = field(default_factory=[])

  @classmethod
  def from_dict(cls, data: dict):
    data_copy = data.copy()

    data_copy["items"] = [ProductItemEntity.from_dict(item) for item in data["items"]]
    data_copy["created"] = datetime.strptime(data["created"],"%Y-%m-%dT%H:%M:%S.%fZ")
    return cls(**data_copy)
  
  def to_dict(self) -> dict:
    return {
      "created": self.created.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
      "items": [item.to_dict() for item in self.items],
    }

@dataclass(kw_only=True)
class OrderEntity:
  id: int = None
  created: datetime = datetime.now()
  paid: bool = False
  items: List[OrderItemEntity] = field(default_factory=[])
  rounds: List[RoundItemEntity] = field(default_factory=[])
  discount: float = 0.0
  tax_rate: float = 0.15
  subtotal: float = 0.0
  taxes: float = 0.0
  total: float = 0.0

  @classmethod
  def from_dict(cls, data: dict):
    data_copy = data.copy()

    data_copy["items"] = [OrderItemEntity.from_dict(item) for item in data["items"]]
    data_copy["rounds"] = [RoundItemEntity.from_dict(item) for item in data["rounds"]]
    data_copy["created"] = datetime.strptime(data["created"], "%Y-%m-%dT%H:%M:%S.%fZ")
    return cls(**data_copy)
  
  def to_dict(self) -> dict:
    return {
      "id": self.id,
      "created": self.created.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
      "paid": self.paid,
      "items": [item.to_dict() for item in self.items],
      "rounds": [r_item.to_dict() for r_item in self.rounds],
      "discount": self.discount,
      "tax_rate": self.tax_rate,
      "subtotal": self.subtotal,
      "taxes": self.taxes,
      "total": self.total
    }