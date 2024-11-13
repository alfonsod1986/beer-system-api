from unittest import mock
from app.domain.use_cases.product.get_by_id import GetProductByIdUseCase

def test_product_by_id_founded(domain_products):
  repo = mock.Mock()
  repo.get_by_id.side_effect = lambda id: next((p for p in domain_products if p.id == id), None)

  get_product_by_id_use_case = GetProductByIdUseCase(repo)
  result = get_product_by_id_use_case.execute(1)

  repo.get_by_id.assert_called_with(1)
  assert result == domain_products[0]

def test_product_by_id_none(domain_products):
  repo = mock.Mock()
  repo.get_by_id.side_effect = lambda id: next((p for p in domain_products if p.id == id), None)

  get_product_by_id_use_case = GetProductByIdUseCase(repo)
  result = get_product_by_id_use_case.execute(15)

  repo.get_by_id.assert_called_with(15)
  assert result == None
