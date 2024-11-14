class Quantity:
  def __init__(self, value: int):
    if not isinstance(value, int) or value <= 0:
      raise ValueError("Quantity must be a positive integer")
    self.__value = value
  
  @property
  def value(self):
    return self.__value
  
  def __eq__(self, other):
    if isinstance(other, Quantity):
      return self.__value == other.__value
    return False