import os
from dotenv import load_dotenv
load_dotenv()

class Endpoint:

    def __init__(self):
        pass

    # Эндпоинт для получения списка заявок
    @staticmethod
    def list_endpoints(start_date, end_date):
        return (f'{os.getenv('HOST')}/ReportRequest/List?StartDate={start_date}&EndDate={end_date}&'
                f'PageNumber=1&PageSize=10&UserId={os.getenv('UserId')}&OrganizationId={os.getenv('OrganizationId')}&Login={os.getenv("Login")}')
    # Эндпоинт для создания пустого отчета
    @staticmethod
    def unlocking_order_creation_endpoint():
        return (f'{os.getenv("HOST")}/ReportRequest/UnlockingOrderCreation?')

    # Метод очистки всех позиций
    @staticmethod
    def clear_endpoint():
        return (f'{os.getenv("HOST")}/ReportRequest/Position/Clear')

    @staticmethod
    def position_list():
        return (f'{os.getenv("HOST")}/ReportRequest/Position/List?PageNumber=1&PageSize=15&UserId={os.getenv("UserId")}&OrganizationId={os.getenv("OrganizationId")}&Login={os.getenv("Login")}')

    @staticmethod
    def add_position_endpoint():
        return (f'{os.getenv("HOST")}/ReportRequest/Position')

    @staticmethod
    def update_quantity_endpoint():
        return (f'{os.getenv("HOST")}/ReportRequest/Position/Quantity')

    @staticmethod
    def delete_position_endpoint():
        return (f'{os.getenv("HOST")}/ReportRequest/Position')

if __name__ == '__main__':
    endpoint = Endpoint()
    print(endpoint.add_position_endpoint())