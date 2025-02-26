import json

from src.sales.sales_api import SalesAPI
import pytest
import requests


def test_get_sales_list():
    from src.sales.utils.sales_utils import SalesUtils
    sales_api = SalesAPI()
    api_response = sales_api.sale_list(start_date='2024-11-26', end_date='2025-02-26', page_size=20, page_number=1, organizationId=46307, sales_grouping=1, detail_groups=562)
    assert api_response.status_code == 200, f'api response {api_response.status_code} != 200'
    assert SalesUtils.check_detail_group_id(api_response,562) == True, f'api response {api_response.json()} != 200'
