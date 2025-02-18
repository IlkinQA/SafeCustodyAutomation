import os
import requests
from requests import PreparedRequest
from dotenv import load_dotenv

from src.basket.data.Examples import add_position_data

load_dotenv()
from src.basket.payloads import Payload
from src.basket.endpoints import Endpoints
from src.basket.headers import Header
from src.bearer.signIn import sigh_in

class BasketAPI:
    def __init__(self):
        pass
    def get_basket(self):
        url = Endpoints.get_basket()
        headers = Header.get_basket_header()
        response = requests.get(url, headers=headers)
        return response

    def add_position(self, payload: dict):
        url = Endpoints.add_position_endpoint()
        headers = Header.add_position_header()
        response = requests.post(url, headers=headers, json=payload)
        return response

    def clear_basket(self):
        url = Endpoints.clear_basket_endpoint()
        headers = Header.clear_basket_header()
        payload = Payload.clear_basket_payload()
        response = requests.delete(url, headers=headers, json=payload)
        return response

    def update_basket(self, payload: dict):
        url = Endpoints.update_basket_endpoint()
        headers = Header.update_basket_header()
        payload = Payload.update_basket_payload(payload)
        response = requests.request('PUT', url, headers=headers, json=payload)
        return response
    #выдает 502
    def clear_position(self, payload):
        url = Endpoints.clear_position_endpoint()
        headers = Header.clear_position_header()
        payloads = Payload.clear_position_payload(payload)
        response = requests.request('DELETE', url, headers=headers, json=payloads)
        return response

    def replenishment(self, payload: dict):
        url = Endpoints.replenishment_endpoint()
        headers = Header.replenishment_header()
        payload = Payload.replenishment_payload(payload)
        response = requests.request('POST', url, headers=headers, json=payload)
        return response

    def actualize_basket(self):
        pass

def main():
    pass
if __name__ == '__main__':
    from src.basket.data import *
    basket = BasketAPI()
    print(basket.clear_position({"UserId":1264372,"OrganizationId":274116,"Login":"UAI5981842","DetailId":52800971,"RegionId":64,"PartyCount":1,"Quantity":1}))

