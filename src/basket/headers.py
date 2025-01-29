from src.bearer.signIn import sigh_in

class Header:
    @staticmethod
    def get_basket_header():
        headers = {
            'accept': 'text/plain',
            'Authorization': f'Bearer {sigh_in()}'
        }
        return headers
