import os

import requests
from dotenv import load_dotenv
load_dotenv()
from src.basket.endpoints import Endpoints
from src.basket.headers import Header
from src.bearer.signIn import sigh_in

class BasketAPI:
    def __init__(self,UserId: int, OrganizationId: int, Login: str,  DetailId = None):
        self.DetailId = DetailId
        self.UserId = UserId
        self.OrganizationId = OrganizationId
        self.Login = Login

    def get_basket(self):
        url = Endpoints.get_basket_token(self.UserId, self.OrganizationId, self.Login)
        headers = Header().get_basket_header()
        response = requests.get(url, headers=headers)
        return response


def main():
    pass
if __name__ == '__main__':
    basket = BasketAPI(
        UserId=1264372,
        OrganizationId=274116,
        Login='UAI5981842'
    )
    print(basket.get_basket())