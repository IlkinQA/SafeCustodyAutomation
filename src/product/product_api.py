from src.product.headers import Header
from src.product.endpoints import Endpoint
import requests

class ProductAPI:

    def __init__(self):
        pass

    def product(self):
        url = Endpoint.product_endpoint()
        header = Header().product_header()
        request = requests.get(url, headers=header)
        return request



if __name__ == '__main__':
    api = ProductAPI()
    request = api.product()
    print(request.json())
