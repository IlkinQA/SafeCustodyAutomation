import requests
from src.prices.endpoints import Endpoint
from src.prices.headers import Headers
class PricesAPI:
    def __init__(self):
        pass

    def offers_by_detail(self, detail_number):
        url = Endpoint.offers_by_detail_endpoint(detail_number)
        headers = Headers.offers_by_detail_header()
        response = requests.get(url, headers=headers)
        return response


if __name__ == "__main__":
    pass