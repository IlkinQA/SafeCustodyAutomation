import pytest
from src.prices.prices_api import PricesAPI

@pytest.mark.parametrize('detail_number', {'IB11001', 'IB111043'})
def test_prices(price_api, detail_number):
    response = price_api.offers_by_detail(detail_number=detail_number)
    assert response.status_code == 200, response.text


@pytest.mark.parametrize('detail_number, expected_status_code', [('IB11001', 200), ('tyu67', 404)])
def test_prices2(price_api, detail_number, expected_status_code):
    response = price_api.offers_by_detail(detail_number=detail_number)
    assert response.status_code == expected_status_code, f'Actual: {response.text}'