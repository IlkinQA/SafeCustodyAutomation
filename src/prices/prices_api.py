import requests

from src.prices.headers import Header
from src.prices.endpoints import Endpoint

class PriceAPI(Endpoint, Header):
    def __init__(self):
        super().__init__()

    def offers_by_detail(self):
        url = self.get_endpoints()
        headers = self.get_price_headers()
        response = requests.get(url, headers=headers)
        return response


def main():
    api = PriceAPI()
    url = api.offers_by_detail()
    print(url)

if __name__ == '__main__':
    main()