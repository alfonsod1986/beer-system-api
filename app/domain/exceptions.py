class ProductNotFoundError(Exception):
  def __init__(self, id: int):
    super().__init__(f"Product with ID {id} not found")