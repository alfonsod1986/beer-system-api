from datetime import datetime
from pydantic import BaseModel, PositiveFloat, PositiveInt
from typing import Optional, List

class OrderItem(BaseModel):
  name: str
  price_per_unit: PositiveFloat
  total: PositiveFloat

class ProductItem(BaseModel):
  name: str
  quantity: PositiveInt

class RoundItem(BaseModel):
  created: datetime = datetime.now()
  items: List[ProductItem] = []

class OrderInput(BaseModel):
  created: Optional[datetime] = datetime.now()
  paid: Optional[bool] = False
  items: Optional[List[OrderItem]] = []
  rounds: Optional[List[RoundItem]] = []
  discount: Optional[float] = 0.0
  tax_rate: Optional[float] = 0.15
  subtotal: Optional[float] = 0.0
  taxes: Optional[float] = 0.0
  total: Optional[float] = 0.0

class OrderOutput(OrderInput):
  id: int

