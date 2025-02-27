import os
import urllib

from dotenv import load_dotenv
load_dotenv()

class Endpoints:

    def __init__(self):
        pass

    @staticmethod
    def sale_list(*, start_date, end_date, page_number, page_size, organizationId, sales_grouping, detail_groups = None, detail_number_comparison = None, detail_number = None):
        base_url = os.getenv("HOST") + '/Sales/List'
        params = {
            'StartDate': start_date,
            'EndDate': end_date,
            'PageNumber': page_number,
            'PageSize': page_size,
            'OrganizationId': organizationId,
            'SalesGrouping': sales_grouping
        }
        # Если выполняем фильтрацию по группе деталей, добавляем дополнительные параметры к url
        if detail_groups:
            params['DetailGroups'] = detail_groups
            query_string = '&'.join(f'{key}={value}' for key, value in params.items())
            return f'{base_url}?{query_string}'

        # Если выполняем фильтрацию по номеру детали, добавляем дополнительные параметры к url
        if detail_number_comparison and detail_number:
            params['DetailNumber'] = detail_number
            params['DetailNumberComparison'] = detail_number_comparison
            query_string = '&'.join(f'{key}={value}' for key, value in params.items())
            return f'{base_url}?{query_string}'

        query_string = '&'.join(f'{key}={value}' for key, value in params.items())
        return f'{base_url}?{query_string}'


if __name__ == '__main__':
    endpoints = Endpoints()
    print(endpoints.sale_list(start_date='2024-11-26', end_date='2025-02-26', page_size='10', page_number='1', organizationId='46307', sales_grouping='1'))