from app.domain.use_cases.product.get_all import GetAllProductsUseCase
from app.domain.use_cases.product.get_by_id import GetProductByIdUseCase
from app.domain.use_cases.product.create import CreateProductUseCase
from app.domain.use_cases.product.update import UpdateProductUseCase
from app.domain.use_cases.product.delete import DeleteProductUseCase
from app.domain.entities.product import ProductEntity
from typing import List

class ProductService:
  def __init__(
    self,
    get_all_products_use_case: GetAllProductsUseCase,
    get_product_by_id_use_case: GetProductByIdUseCase,
    create_product_use_case: CreateProductUseCase,
    update_product_use_case: UpdateProductUseCase,
    delete_product_use_case: DeleteProductUseCase,
  ):
    self.__get_all_products_use_case = get_all_products_use_case
    self.__get_product_by_id_use_case = get_product_by_id_use_case
    self.__create_product_use_case = create_product_use_case
    self.__update_product_use_case = update_product_use_case
    self.__delete_product_use_case = delete_product_use_case
  
  def get_all(self) -> List[ProductEntity]:
    return self.__get_all_products_use_case.execute()
  
  def get_by_id(self, id: int) -> ProductEntity | None:
    return self.__get_product_by_id_use_case.execute(id)
    
  
  def create(self, product: ProductEntity) -> ProductEntity:
    return self.__create_product_use_case.execute(product)
  
  def update(self, id: int, product: ProductEntity) -> ProductEntity:
    return self.__update_product_use_case.execute(id, product)
  
  def delete(self, id: int) -> bool:
    return self.__delete_product_use_case.execute(id)