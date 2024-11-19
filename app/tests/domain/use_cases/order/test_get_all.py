from unittest import mock
from app.domain.use_cases.order.get_all import GetAllOrdersUseCase

def test_product_get_all(domain_products):
    repo = mock.Mock()
    repo.get_all.return_value = domain_products

    get_all_orders_use_case = GetAllOrdersUseCase(repo)
    result = get_all_orders_use_case.execute()

    repo.get_all.assert_called_with()
    assert result == domain_products