from pydantic import BaseModel, PositiveFloat, PositiveInt
from typing import Optional

class ProductInput(BaseModel):
  name: str
  description: Optional[str] = None
  price: PositiveFloat
  stock: PositiveInt = 0


class ProductOutput(ProductInput):
  id: int