from unittest import mock
from app.domain.use_cases.product.delete import DeleteProductUseCase

def test_product_delete(domain_products):
  repo = mock.Mock()
  repo.delete.return_value = True

  delete_product_use_case = DeleteProductUseCase(repo)
  result = delete_product_use_case.execute(1)

  repo.delete.assert_called_with(1)
  assert result == True