import pytest
import requests
from src.prices.prices_api import PricesAPI
import os
from dotenv import load_dotenv
from src.matrix_client.matrix_client_api import MatrixClientApi

# Фикстура для получения товаров на регистре у клиента
@pytest.fixture
def product():
    from src.product.product_api import ProductAPI
    product = ProductAPI()
    return product
# Фикстура для получения списка рекомендованных товаров
@pytest.fixture
def matrix_client():
    matrix = MatrixClientApi()
    return matrix

# Фикстура для создания объекта basketApi
@pytest.fixture(autouse=True)
def basket_api():
    from src.basket.basket_api import BasketAPI
    basket = BasketAPI()
    return basket

@pytest.fixture
def price_api():
    price = PricesAPI()
    return price

# Фикстура данных для добавления детали в к корзину
@pytest.fixture(autouse=True)
def add_payload():
    return {"UserId":1264372,"OrganizationId":274116,"Login":"UAI5981842","DetailId":52800971,"RegionId":64,"PartyCount":1,"Quantity":1}

@pytest.fixture
# Фикстура для получения параметризованных данных
def add_position_payload():
    from src.basket.data.Examples import add_position_data
    return add_position_data


# Фикстура для получения данных о пользователе
@pytest.fixture
def user_data():
    return {
    "UserId": 1264372,
    "OrganizationId": 274116,
    "Login": "UAI5981842",
}

@pytest.fixture
def detail_number_list():
    return ['IB11001', 'IB11015', 'IB2043']