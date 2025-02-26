import json

class ReportingPeriodUtils:

    def __init__(self):
        pass

    def expired_reporting_periods_exist(self, index):
        from src.reporting_period.reporting_periods_api import ReportingPeriodAPI
        reporting_period_api = ReportingPeriodAPI()
        expired_reporting_list = reporting_period_api.expired().json()
        try:
            return expired_reporting_list['Periods'][index]
        except IndexError:
            return 'Индекс вне диапазона'


if __name__ == '__main__':
    reporting_period_utils = ReportingPeriodUtils()
    print(reporting_period_utils.expired_reporting_periods_exist(2))


