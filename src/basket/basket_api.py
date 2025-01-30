import os

import requests
from dotenv import load_dotenv
load_dotenv()
from src.basket.endpoints import Endpoints
from src.basket.headers import Header
from src.bearer.signIn import sigh_in

class BasketAPI:
    def __init__(self):
        pass
    def get_basket(self):
        url = Endpoints.get_basket_token()
        headers = Header().get_basket_header()
        response = requests.get(url, headers=headers)
        return response


def main():
    pass
if __name__ == '__main__':
    basket = BasketAPI()
    print(basket.get_basket().json())