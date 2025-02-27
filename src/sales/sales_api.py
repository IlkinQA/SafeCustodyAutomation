import requests
from src.sales.headers import Header
from src.sales.endpoints import Endpoints

class SalesAPI:
    def __init__(self):
        pass

    def sale_list(self, start_date, end_date, page_size, page_number, organizationId,sales_grouping, detail_groups=None, detail_number_comparison = None, detail_number = None):
        url = Endpoints.sale_list(start_date=start_date, end_date=end_date, page_size=page_size, page_number=page_number, organizationId=organizationId, sales_grouping=sales_grouping, detail_groups=detail_groups,
                                  detail_number_comparison=detail_number_comparison, detail_number=detail_number)
        header = Header().sales_list_header()
        response = requests.get(url=url, headers=header)
        return response


def lagged_info():
    import logging
    logger = logging.getLogger('API_TESTS')
    ap1 = SalesAPI()
    res = ap1.sale_list(start_date='2024-11-26', end_date='2025-02-26', page_size=20, page_number=1, organizationId=46307, sales_grouping=1)
    logger.info(res.status_code)



if __name__ == '__main__':
    import logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logger = logging.getLogger('API_TESTS')
    try:
        ap1 = SalesAPI()
        res = ap1.sale_list(start_date='2024-11-26', end_date='2025-02-26', page_size=20, page_number=1,
                        organizationId=46307, sales_grouping=1)
        logger.info(f'Status code: {res.status_code}')
        logger.info(f'Status url: {res.url}')
        logger.info(f'Status header: {res.headers}')

    except Exception as e:
        logger.error(e)