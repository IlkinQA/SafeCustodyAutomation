from src.bearer.signIn import sigh_in

class Headers:

    def __init__(self):
        pass

    @staticmethod
    def offers_by_detail_header():
        return {
            'accept' : 'text/plain',
            'Authorization' : f'Bearer {sigh_in()}'
        }