from http.client import responses

import pytest
import requests
from src.basket.basket_api import BasketAPI
from src.basket.utils.basket_utils import get_basket_quantity
from src.product.utils.product_utils import get_product_quantity_by_detail_id
from src.matrix_client.utils.matrix_client_utils import get_matrix_quantity

# Функция для получения параметризованных данных
def add_position_payload():
    from src.basket.data.Examples import add_position_data
    return add_position_data

@pytest.mark.parametrize('payload', add_position_payload())
def test_add_position(payload, basket):
    response = basket.add_position(payload=payload)
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

def test_replenishment(basket_api, product, user_data):
    # перед тестом очищаем корзину
    basket_api.clear_basket()
    assert basket_api.replenishment(user_data).status_code == 204, 'Method replenishment failed.'