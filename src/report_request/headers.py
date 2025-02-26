from src.bearer.signIn import sigh_in

class Header:

    def __init__(self):
        pass

    @staticmethod
    def list_headers():
        return {
            'accept' : 'text/plain',
            'Authorization' : f'Bearer {sigh_in()}'
        }
    @staticmethod
    def unlocking_order_creation_headers():
        return {
            'accept' : '*/*',
            'Authorization' : f'Bearer {sigh_in()}',
            'Content-Type' : 'application/json'
        }
    @staticmethod
    def clear_headers():
        return {
            'accept' : '*/*',
            'Authorization' : f'Bearer {sigh_in()}',
            'Content-Type' : 'application/json'
        }
    @staticmethod
    def position_list_headers():
        return {
            'accept' : 'text/plain',
            'Authorization' : f'Bearer {sigh_in()}'
        }

    @staticmethod
    def add_position_headers():
        return {
            'accept' : '*/*',
            'Authorization' : f'Bearer {sigh_in()}',
            'Content-Type' : 'application/json'
        }

    @staticmethod
    def update_quantity_headers():
        return {
            'accept' : '*/*',
            'Authorization' : f'Bearer {sigh_in()}',
            'Content-Type' : 'application/json'
        }

    @staticmethod
    def delete_position_headers():
        return {
            'accept' : '*/*',
            'Authorization' : f'Bearer {sigh_in()}',
            'Content-Type' : 'application/json'
        }
