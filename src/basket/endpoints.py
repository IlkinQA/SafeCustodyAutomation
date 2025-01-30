import os
from dotenv import load_dotenv
load_dotenv()

class Endpoints:
    # получить список деталей из корзины
    @staticmethod
    def get_basket_token() -> str:
        return f'{os.getenv('HOST')}/Basket?UserId={os.getenv('UserId')}&OrganizationId={os.getenv('OrganizationId')}&Login={os.getenv("Login")}'

def main():
    pass
if __name__ == '__main__':
    print(Endpoints.get_basket_token())