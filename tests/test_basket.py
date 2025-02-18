
import pytest
import requests

import os
from dotenv import load_dotenv

from src.basket.basket_api import BasketAPI


@pytest.fixture(autouse=True)
def load_environment():
    load_dotenv()
    return {
        'UserId' : int(os.getenv('UserId')),
        'OrganizationId' : int(os.getenv('OrganizationId')),
        'Login' : os.getenv('Login')
    }
# Фикстура для создания объекта basketApi
@pytest.fixture(autouse=True)
def basket():
    from src.basket.basket_api import BasketAPI
    basket = BasketAPI()
    return basket
# Функция для получения параметризованных данных
def add_position_payload():
    from src.basket.data.Examples import add_position_data
    return add_position_data

@pytest.fixture(autouse=True)
def add_payload():
    return {"UserId":1264372,"OrganizationId":274116,"Login":"UAI5981842","DetailId":52800971,"RegionId":64,"PartyCount":1,"Quantity":1}

def get_basket(create_object):
    response = create_object.get_basket()
    # Проверяем, работает ли метод получения корзины
    if response.status_code == 200:
        return True # Возвращаем значение True, если корзина доступна

@pytest.mark.parametrize('payload', add_position_payload())
def test_add_position( payload, basket):
    assert get_basket(basket) == True
    response = basket.add_position(payload)
    assert response.status_code == 204
    yield
    basket.clear_basket()

#доделать
def test_clear_position(add_payload):
    basket = BasketAPI()
    add_response = basket.add_position(add_payload)
    assert add_response.status_code == 204, f'Method add_position failed. Response code: {add_response.status_code}'
    clear_position_response = basket.clear_position(add_payload)
    assert clear_position_response.status_code == 204, f'Method clear_position failed. Response code: {clear_position_response.status_code}.'

