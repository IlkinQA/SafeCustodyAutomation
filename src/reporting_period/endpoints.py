import os
from dotenv import load_dotenv
load_dotenv()

class Endpoints:
    def __init__(self):
        pass

    @staticmethod
    def reporting_periods_endpoint():
        return f'{os.getenv('HOST')}/ReportingPeriod?UserId={os.getenv("UserId")}&OrganizationId={os.getenv("OrganizationId")}&Login={os.getenv("Login")}'

    @staticmethod
    def expired_endpoint():
        return f'{os.getenv('HOST')}/ReportingPeriod/Expired?UserId={os.getenv("UserId")}&OrganizationId={os.getenv("OrganizationId")}&Login={os.getenv("Login")}'

    @staticmethod
    def without_report_endpoint():
        return f'{os.getenv('HOST')}/ReportingPeriod/WithoutReport?UserId={os.getenv("UserId")}&OrganizationId={os.getenv("OrganizationId")}&Login={os.getenv("Login")}'

    @staticmethod
    def position_list_endpoint():
        return f'{os.getenv('HOST')}/ReportingPeriod/Position/List?PageNumber=1&PageSize=15&UserId={os.getenv("UserId")}&OrganizationId={os.getenv("OrganizationId")}&Login={os.getenv("Login")}'