from unittest import mock
from app.domain.use_cases.product.get_all import GetAllProductsUseCase

def test_product_get_all(domain_products):
    repo = mock.Mock()
    repo.get_all.return_value = domain_products

    get_all_products_use_case = GetAllProductsUseCase(repo)
    result = get_all_products_use_case.execute()

    repo.get_all.assert_called_with()
    assert result == domain_products