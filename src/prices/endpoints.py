import os
from dotenv import load_dotenv
load_dotenv()

class Endpoint:

    @staticmethod
    def get_endpoints() -> str:
        return (f'{os.getenv('HOST')}/Prices/OffersByDetail?DetailNumber={os.getenv("DetailId")}'
                f'&UserId={os.getenv("UserId")}&OrganizationId={os.getenv("OrganizationId")}&Login={os.getenv("Login")}')