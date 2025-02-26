from src.report_request.report_request_api import ReportRequestAPI

class ReportRequestUtils:

    def __init__(self):
        pass

    # Метод получения ReportRequestId
    @staticmethod
    def get_report_request_id():
        report_request = ReportRequestAPI()
        return report_request.position_list().json().get('ReportRequestId')


