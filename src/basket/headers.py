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
            'Authorization': f'Bearer {sigh_in()}',
            'Content-Type': 'application/json',
        }
        return headers

    @staticmethod
    def clear_basket_header():
        headers = {
            'accept': '*/*',
            'Authorization': f'Bearer {sigh_in()}',
            'Content-Type': 'application/json'
        }
        return headers

    @staticmethod
    def update_basket_header():
        headers = {
            'accept': '*/*',
            'Authorization': f'Bearer {sigh_in()}',
            'Content-Type': 'application/json'
        }
        return headers

    @staticmethod
    def clear_position_header():
        headers = {
            'accept': '*/*',
            'Authorization': f'Bearer {sigh_in()}',
            'Content-Type': 'application/json'
        }
        return headers

    @staticmethod
    def replenishment_header():
        headers = {
            'accept': '*/*',
            'Authorization': f'Bearer {sigh_in()}',
            'Content-Type': 'application/json'
        }
        return headers

    @staticmethod
    def actualize_basket_header():
        headers = {
            'accept': '*/*',
            'Authorization': f'Bearer {sigh_in()}',
            'Content-Type': 'application/json'
        }
        return headers




