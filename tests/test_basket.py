import pytest
import requests
from src.bearer.signIn import sigh_in
from src.basket.basket import get_basket
from src.basket.basket import add_positions


@pytest.fixture(autouse=True)
def bearer():
    return sigh_in()
@pytest.fixture(autouse=True)
def get_user_data():
    return {
        'UserId' : 1264372,
        'OrganizationId' : 274116,
        'Login' : 'UAI5981842'
    }
@pytest.fixture(autouse=True)
def get_detail_data():
    return {
    'DetailId' : 'IB111043'
    }

def test_get_basket(bearer, get_user_data):
    basket = get_basket(UserId=str(get_user_data['UserId']), OrganizationId=str(get_user_data['OrganizationId']), Login=get_user_data['Login'],token=bearer)
    assert basket.status_code != 401 or basket.status_code == 400, f'Status code {basket.status_code}'

def test_add_position(bearer, get_user_data,get_detail_data):
    response = add_positions(UserId=get_user_data['UserId'],OrganizationId=get_user_data['OrganizationId'],
                             Login=get_user_data['Login'],token=bearer,DetailId=get_detail_data['DetailId'],PartyCount=1,Quantity=1,RegionId=12090)
    assert response.status_code != 400, f'Status code {response.status_code}'
    assert response.status_code == 403, f'Status code {response.status_code} \n Check your role!'
