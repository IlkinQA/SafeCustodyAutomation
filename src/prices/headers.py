import os
from dotenv import load_dotenv
load_dotenv()
from src.bearer.signIn import sigh_in

class Header:
    @staticmethod
    def get_price_headers():
        headers = {
            'accept': 'text/plain',
            'Authorization': f'Bearer {sigh_in()}'
        }
        return headers