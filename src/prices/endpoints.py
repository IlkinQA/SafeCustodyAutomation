import os
from dotenv import load_dotenv
load_dotenv()

class Endpoint:
    offers_by_detail = f'{os.getenv("HOST")}/Prices/OffersByDetail'