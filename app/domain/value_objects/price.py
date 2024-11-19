class Price:
  def __init__(self, value: float):
    if not isinstance(value, (float, int)) or value <= 0:
      raise ValueError("Price must be a positive float")
    self.__value = value
  
  @property
  def value(self):
    return self.__value
  
  def __eq__(self, other):
    if isinstance(other, Price):
      return self.__value == other.__value
    return False