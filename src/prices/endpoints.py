import os
from dotenv import load_dotenv
load_dotenv()

class Endpoint:

    def __init__(self):
        pass

    @staticmethod
    def offers_by_detail_endpoint(DetailNumber):
        return f'{os.getenv('HOST')}/Prices/OffersByDetail?DetailNumber={DetailNumber}&UserId={os.getenv('UserId')}&OrganizationId={os.getenv('OrganizationId')}&Login={os.getenv('Login')}'

