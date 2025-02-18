import os
from dotenv import load_dotenv
load_dotenv()

class Endpoints:
    # получить список деталей из корзины
    @staticmethod
    def get_basket() -> str:
        return f'{os.getenv('HOST')}/Basket?UserId={os.getenv('UserId')}&OrganizationId={os.getenv('OrganizationId')}&Login={os.getenv("Login")}'

    @staticmethod
    def add_position_endpoint():
        return f'{os.getenv('HOST')}/Basket/Position'

    @staticmethod
    def clear_basket_endpoint():
        return f'{os.getenv('HOST')}/Basket/Clear'

    @staticmethod
    def update_basket_endpoint():
        return f'{os.getenv('HOST')}/Basket/Position'

    @staticmethod
    def clear_position_endpoint():
        return f'{os.getenv('HOST')}/Basket/Position'

    @staticmethod
    def replenishment_endpoint():
        return f'{os.getenv('HOST')}/Basket/Replenishment'

    @staticmethod
    def actualize_basket_endpoint():
        return f'{os.getenv('HOST')}/Basket/Actualize'




def main():
    pass
if __name__ == '__main__':
    print(Endpoints.add_position_endpoint())