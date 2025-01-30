import requests

from src.prices.headers import Header
from src.prices.endpoints import Endpoint

class PriceAPI(Endpoint, Header):
    def __init__(self):
        super().__init__()
    #/Prices/OffersByDetail
    def offers_by_detail(self):
        url = self.get_endpoints()
        headers = self.get_price_headers()
        response = requests.get(url, headers=headers)
        return response
    def check_offers_exist(self):
        url = self.get_endpoints()
        headers = self.get_price_headers()
        response = requests.get(url, headers=headers).json()
        for group in response['Groups']:
            for detail in group['Details']:
                offers = detail.get('Offers',[])
                if not offers:
                    return False
                else:
                    return True

def main():
   price = PriceAPI()
   response = price.offers_by_detail()
   is_exist = price.check_offers_exist()
   print(is_exist)

if __name__ == '__main__':
    main()