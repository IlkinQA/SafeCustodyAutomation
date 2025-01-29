import os
from dotenv import load_dotenv
load_dotenv()

class Endpoints:
    # получить список деталей из корзины
    @staticmethod
    def get_basket_token(UserId: int, OrganizationId: int, Login: str) -> str:
        return f'{os.getenv('HOST')}/Basket?UserId={UserId}&OrganizationId={OrganizationId}&Login={Login}'

def main():
    pass
if __name__ == '__main__':
    print(Endpoints.get_basket_token(UserId=1264372, OrganizationId=274116, Login='UAI5981842'))