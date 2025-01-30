from src.bearer.signIn import sigh_in

class Header:
    @staticmethod
    def get_basket_header():
        headers = {
            'accept': 'text/plain',
            'Authorization': f'Bearer {sigh_in()}'
        }
        return headers

    @staticmethod
    def add_position_header():
        headers = {
            'accept': '*/*',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Authorization': f'Bearer {sigh_in()}',
            'Content-Type': 'application/json',
        }
        return headers

