import os
from dotenv import load_dotenv
load_dotenv()
import json
class Payload:
    def __init__(self):
        pass
    @staticmethod
    def add_position_payload(payload: dict):
        return payload

    @staticmethod
    def clear_basket_payload():
        return {
            "UserId": 1264372,
            "OrganizationId": 274116,
            "Login": "UAI5981842"
        }
    @staticmethod
    def update_basket_payload(payload: dict):
        return payload

    # данные получаем из параметризации
    @staticmethod
    def clear_position_payload(payload):
        payload = {
            'UserId': int(payload['UserId']),
            'OrganizationId': int(payload['OrganizationId']),
            'Login': payload['Login'],
            'Positions': [
                {
                    'DetailId' : payload['DetailId'],
                    'RegionId' : payload['RegionId'],
                    'PartyCount' : payload['PartyCount']
                }
            ]
        }
        return payload

    @staticmethod
    def replenishment_payload(payload: dict):
        payload = {
            'UserId': int(payload['UserId']),
            'OrganizationId': payload['OrganizationId'],
            'Login': payload['Login'],
        }
        return payload


def main():
    payload = Payload()
    print()

if __name__ == '__main__':
    payload = Payload()
    print(Payload.clear_position_payload({"UserId":1264372,"OrganizationId":274116,"Login":"UAI5981842","DetailId":52800971,"RegionId":64,"PartyCount":1,"Quantity":1}))
