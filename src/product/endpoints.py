import os
from dotenv import load_dotenv
load_dotenv()

class Endpoint:

    def __init__(self):
        pass

    @staticmethod
    def product_endpoint():
        return f'{os.getenv("HOST")}/Product?PageNumber=1&PageSize=50&UserId=1264372&OrganizationId=274116&Login=UAI5981842'
