
import pytest
import requests
from src.basket.basket_api import BasketAPI
import os
from dotenv import load_dotenv


@pytest.fixture(autouse=True)
def load_environment():
    load_dotenv()
    return {
        'UserId' : int(os.getenv('UserId')),
        'OrganizationId' : int(os.getenv('OrganizationId')),
        'Login' : os.getenv('Login')
    }



def test_basket(load_environment):
    api = BasketAPI(UserId=load_environment['UserId'],
                    OrganizationId=load_environment['OrganizationId'],
                    Login=load_environment['Login'])
    response = api.get_basket()
    assert response.status_code == 200
