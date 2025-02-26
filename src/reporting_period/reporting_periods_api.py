import requests
from src.reporting_period.headers import Header
from src.reporting_period.endpoints import Endpoints

class ReportingPeriodAPI:

    def __init__(self):
        pass

    # Получить список всех периодов для отчета
    def reporting_periods(self):
        url = Endpoints.expired_endpoint()
        header = Header().expired_header()
        response = requests.get(url, headers=header)
        return response
    # Получить список прошедших периодов для отчета
    def expired(self):
        url = Endpoints.expired_endpoint()
        header = Header().expired_header()
        response = requests.get(url, headers=header)
        return response
    # Получить список периодов за которые не было отчета
    def without_report(self):
        url = Endpoints.without_report_endpoint()
        header = Header().without_report_header()
        response = requests.get(url, headers=header)
        return response

if __name__ == '__main__':
    api = ReportingPeriodAPI()
    response = api.reporting_periods().json()
    print(response)