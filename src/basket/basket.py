import requests
from jsonschema import validate,ValidationError
from src.Data.Schema import basket_schema
import json
from src.bearer.signIn import sigh_in
def get_basket(UserId:str,OrganizationId: str,Login: str,token: str):
    url = f"https://inr-api-01.ixora-auto.ru/SafeCustody/v1/Basket?UserId={UserId}&OrganizationId={OrganizationId}&Login={Login}"

    payload = {}
    headers = {
        'accept': 'text/plain',
        'Authorization': f'Bearer {token}',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    return response

def validate_response(response):
    try:
        validate(instance=response,schema=basket_schema)
        print('Successfully validated')
    except ValidationError as e:
        print("Ответ не соответствует модели:")
        print(f"Ошибка: {e.message}")
        print(f"Полученные данные: {e.instance}")
        print(f"Ожидаемая схема: {e.schema}")

def get_offers(UserId:str,OrganizationId:str,Login:str,token:str,DetailNumber: str):
    url = f"https://inr-api-01.ixora-auto.ru/SafeCustody/v1/Prices/OffersByDetail?UserId={UserId}&OrganizationId={OrganizationId}&Login={Login}&DetailNumber={DetailNumber}"
    payload = {}
    headers = {
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'authorization': f'Bearer {token}',
        'origin': 'http://192.168.218.74',
        'priority': 'u=1, i',
        'referer': 'http://192.168.218.74/',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    return response
def add_positions(*,UserId: int,OrganizationId: int,Login: str,token: str,DetailId: int, PartyCount: int, RegionId: int, Quantity: int = 1):
    url = 'https://inr-api-01.ixora-auto.ru/SafeCustody/v1/Basket/Position'
    payload = json.dumps({
  "UserId": UserId,
  "OrganizationId": OrganizationId,
  "Login": Login,
  "DetailId": DetailId,
  "RegionId": RegionId,
  "PartyCount": PartyCount,
  "Quantity": Quantity,
  "Reference": "string"
})
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'authorization' : f'Bearer {token}',
        'content-type': 'application/json',
        'origin': 'http://192.168.218.74',
        'priority': 'u=1, i',
        'referer': 'http://192.168.218.74/',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
                }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response


def main():
    pass
if __name__ == '__main__':
    res = get_offers(UserId=str('1264372'), OrganizationId=str('274116'), Login=str('UAI5981842'), token=sigh_in(), DetailNumber='IB111157Y')
    print(res.json())