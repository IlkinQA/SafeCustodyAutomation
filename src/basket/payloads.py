from faker import Faker
import os
from dotenv import load_dotenv
load_dotenv()
fake = Faker()


class Payload:
    add_position = {
        'UserId' : os.getenv('UserId'),
        'OrganizationId' : os.getenv('OrganizationId'),
        'Login' : f'{os.getenv("Login")}',
        'DetailId' : f'{os.getenv("DetailId")}',
        "RegionId": 12090,
        'PartyCount': 1,
        'Quantity': 1,
        'Reference': 'string'
    }
    