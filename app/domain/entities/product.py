from dataclasses import dataclass
from app.domain.value_objects.price import Price
from app.domain.value_objects.stock import Stock

@dataclass(kw_only=True)
class ProductEntity:
  id: int = None
  name: str
  description: str = None
  price: Price
  stock: Stock

  @classmethod
  def from_dict(cls, data: dict):
    data_copy = data.copy()

    data_copy["price"] = Price(data["price"])
    data_copy["stock"] = Stock(data["stock"])
    return cls(**data_copy)
  
  def to_dict(self) -> dict:
    return {
      "id": self.id,
      "name": self.name,
      "description": self.description,
      "price": self.price.value,
      "stock": self.stock.value,
    }