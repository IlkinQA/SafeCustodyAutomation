import os
from dotenv import load_dotenv
load_dotenv()
from src.prices.prices_api import PriceAPI
class Payload:
    def __init__(self):
        pass
    @staticmethod
    def add_position_payload():
        price = PriceAPI()
        price_offers = price.offers_by_detail().json()

        payload = {
            'UserId' : int(os.getenv('UserId')),
            'OrganizationId' : int(os.getenv('OrganizationId')),
            'Login' : os.getenv('Login'),
            'DetailId' : int(price_offers['Groups'][0]['Details'][0]['DetailId']), # нужно сравнить с методом получения предложений
            'RegionId' : int(price_offers['Groups'][0]['Details'][0]['Offers'][0]['RegionId']),
            'PartyCount' : 1,
            'Quantity' : 1,
            'Reference' : int(price_offers['Groups'][0]['Details'][0]['DetailId'])
        }
        return payload


def main():
    payload = Payload()
    print(payload.add_position_payload())

if __name__ == '__main__':
    main()
