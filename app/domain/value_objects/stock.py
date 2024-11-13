class Stock:
  def __init__(self, value: int):
    if not isinstance(value, int) or value < 0:
      raise ValueError("Stock must be a non-negative integer")
    self.__value = value
  
  @property
  def value(self):
    return self.__value
  
  def __eq__(self, other):
    if isinstance(other, Stock):
      return self.__value == other.__value
    return False