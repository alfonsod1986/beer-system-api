from dependency_injector import containers, providers
from app.infrastructure.repositories.in_memory.product import ProductInMemoryRepository
from app.domain.use_cases.product.get_all import GetAllProductsUseCase
from app.domain.use_cases.product.get_by_id import GetProductByIdUseCase
from app.domain.use_cases.product.create import CreateProductUseCase
from app.domain.use_cases.product.update import UpdateProductUseCase
from app.domain.use_cases.product.delete import DeleteProductUseCase
from app.application.services.product import ProductService

class Container(containers.DeclarativeContainer):
  wiring_config = containers.WiringConfiguration(packages=["app.infrastructure.rest.fastapi.v1.routes"])

  #Repositories
  product_repository = providers.Singleton(
    ProductInMemoryRepository,
    filepath="data/products.json",
  )

  #Use Cases
  get_all_products_use_case = providers.Factory(
    GetAllProductsUseCase,
    repository=product_repository,

  )
  
  get_product_by_id_use_case = providers.Factory(
    GetProductByIdUseCase,
    repository=product_repository,
  )

  create_product_use_case = providers.Factory(
    CreateProductUseCase,
    repository=product_repository,
  )

  update_product_use_case = providers.Factory(
    UpdateProductUseCase,
    repository=product_repository,
  )

  delete_product_use_case = providers.Factory(
    DeleteProductUseCase,
    repository=product_repository,
  )

  #Services
  product_service = providers.Factory(
    ProductService,
    get_all_products_use_case=get_all_products_use_case,
    get_product_by_id_use_case=get_product_by_id_use_case,
    create_product_use_case=create_product_use_case,
    update_product_use_case=update_product_use_case,
    delete_product_use_case=delete_product_use_case,
  )