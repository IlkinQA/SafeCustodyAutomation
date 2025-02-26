import pytest
from src.prices.prices_api import PricesAPI

@pytest.mark.parametrize('detail_number', {'IB11001', 'IB111043'})
def test_prices(price_api, detail_number):
    response = price_api.offers_by_detail(detail_number=detail_number)
    assert response.status_code == 200, response.text