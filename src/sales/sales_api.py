import requests
from src.sales.headers import Header
from src.sales.endpoints import Endpoints

class SalesAPI:
    def __init__(self):
        pass

    def sale_list(self, start_date, end_date, page_size, page_number, organizationId,sales_grouping, detail_groups=None):
        url = Endpoints.sale_list(start_date=start_date, end_date=end_date, page_size=page_size, page_number=page_number, organizationId=organizationId, sales_grouping=sales_grouping, detail_groups=detail_groups)
        header = Header().sales_list_header()
        response = requests.get(url=url, headers=header)
        return response


if __name__ == '__main__':
    sales_api = SalesAPI()
    response = sales_api.sale_list(start_date='2024-11-26', end_date='2025-02-26', page_size='10', page_number='1', organizationId='46307', sales_grouping='1', detail_groups=330)
    print(response)