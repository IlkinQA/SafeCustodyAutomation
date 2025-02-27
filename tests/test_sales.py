import json

from src.sales.sales_api import SalesAPI
import pytest
import requests
from src.sales.utils.sales_utils import SalesUtils

@pytest.fixture(autouse=True)
def sale_api():
    sales_api = SalesAPI()
    return sales_api

# Получение списка деталей
def test_get_sales_list(sale_api):
    api_response = sale_api.sale_list(start_date='2024-11-26', end_date='2025-02-26', page_size=20, page_number=1, organizationId=46307, sales_grouping=1)
    assert api_response.status_code == 200, f'api response {api_response.status_code} != 200'

# Получение списка деталей с фильтрацией по группировке деталей
def test_filter_sales_list_by_detail_group(sale_api):
    api_response = sale_api.sale_list(start_date='2024-11-26', end_date='2025-02-26', page_size=20, page_number=1, organizationId=46307, sales_grouping=1, detail_groups=562)
    assert api_response.status_code == 200, f'api response {api_response.status_code} != 200'
    assert SalesUtils.check_detail_group_id(api_response,562) == True, f'api response {api_response.json()} != 200'

# Получение списка деталей с фильтрацией по номеру детали
def test_filter_sales_list_by_detail_id(sale_api):
    api_response = sale_api.sale_list(start_date='2024-11-26', end_date='2025-02-26', page_size=20, page_number=1,
                                      organizationId=46307, sales_grouping=1, detail_number='IB2071', detail_number_comparison='Equal')

    assert api_response.status_code == 200, f'api response {api_response.status_code} != 200'
    assert SalesUtils.check_detail_number(api_response,'IB2071') == True, f'api response {api_response.json()} != 200'
