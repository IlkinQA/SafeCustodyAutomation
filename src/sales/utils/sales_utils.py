from src.sales.sales_api import SalesAPI
import requests
import json
class SalesUtils:
    def __init__(self):
        pass

    @staticmethod
    def check_detail_group_id(sales_list_response: requests, expected_group_id):
        """
           Проверяет, что все объекты в списке Details имеют заданный DetailGroupId.

           :param sales_list_response: Список объектов Details
           :param expected_group_id: Ожидаемое значение DetailGroupId
           :return: True, если все DetailGroupId равны expected_group_id, иначе False
           """
        data = sales_list_response.json()
        return all(detail['DetailGroupId'] == expected_group_id for detail in data['Details'])

    @staticmethod
    def check_detail_number(sales_list_response: requests, expected_detail_number):
        data = sales_list_response.json()
        return all(detail['DetailNumber'] == expected_detail_number for detail in data['Details'])



if __name__ == '__main__':
    sales_api = SalesAPI()
    res = sales_api.sale_list(start_date='2024-11-26', end_date='2025-02-26', page_size=20, page_number=1,
                              organizationId=46307, sales_grouping=1, detail_number_comparison='Equal', detail_number='IB2071')
    print(SalesUtils.check_detail_number(res, 'IB2071'))