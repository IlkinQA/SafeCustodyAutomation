from src.bearer.signIn import sigh_in
class Header:

    def __init__(self):
        pass

    @staticmethod
    def reporting_period_header():
        return {
            'accept' : 'text/plain',
            'Authorization' : f'Bearer {sigh_in()}'
        }

    @staticmethod
    def expired_header():
        return {
            'accept' : 'text/plain',
            'Authorization' : f'Bearer {sigh_in()}'
        }

    @staticmethod
    def without_report_header():
        return {
            'accept' : 'text/plain',
            'Authorization' : f'Bearer {sigh_in()}'
        }

    @staticmethod
    def position_list_header():
        return {
            'accept': 'text/plain',
            'Authorization': f'Bearer {sigh_in()}'
        }
