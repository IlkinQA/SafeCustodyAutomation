from src.bearer.signIn import sigh_in

class Header:

    def __init__(self):
        pass

    @staticmethod
    def product_header():
        return {
            'accept' : 'text/plain',
            'Authorization' : f'Bearer {sigh_in()}'
        }