import os
from dotenv import load_dotenv
load_dotenv()
import json

class Payload:
    def __init__(self):
        pass

    @staticmethod
    def unlocking_order_creation_payload():
        return {
            "UserId": int(os.environ.get("UserId")),
            "OrganizationId": int(os.environ.get("OrganizationId")),
            "Login": str(os.environ.get("Login")),
        }

    @staticmethod
    def clear_payload():
        from src.report_request.utils.report_request_utils import ReportRequestUtils
        report_request_id = int(ReportRequestUtils().get_report_request_id())
        return {
            "UserId": int(os.environ.get("UserId")),
            "OrganizationId": int(os.environ.get("OrganizationId")),
            "Login": str(os.environ.get("Login")),
            'ReportRequestId' : int(report_request_id)
        }

    @staticmethod
    def add_position_payload(detail_id: int, quantity: int, report_request_id: int):
        return json.dumps({
            "UserId": int(os.environ.get("UserId")),
            "OrganizationId": int(os.environ.get("OrganizationId")),
            "Login": str(os.environ.get("Login")),
            'ReportRequestId' : int(report_request_id),
            'DetailId' : detail_id,
            'Quantity' : quantity
        })

    @staticmethod
    def update_quantity_payload(detail_id: int, quantity: int, report_request_id: int):
        return json.dumps({
            "UserId": int(os.environ.get("UserId")),
            "OrganizationId": int(os.environ.get("OrganizationId")),
            "Login": str(os.environ.get("Login")),
            'ReportRequestId' : int(report_request_id),
            'DetailId' : detail_id,
            'Quantity' : quantity
        })

    @staticmethod
    def delete_position_payload(detail_id: int, report_request_id: int):
        return json.dumps({
            "UserId": int(os.environ.get("UserId")),
            "OrganizationId": int(os.environ.get("OrganizationId")),
            "Login": str(os.environ.get("Login")),
            'ReportRequestId' : int(report_request_id),
            'DetailId' : detail_id
        })



if __name__ == '__main__':
    payload = Payload.delete_position_payload(detail_id=50427613, report_request_id=144)
    print(payload)