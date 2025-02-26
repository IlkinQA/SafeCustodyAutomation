import requests
from src.report_request.headers import Header
from src.report_request.endpoints import Endpoint
from src.report_request.payloads import Payload


class ReportRequestAPI:
    def __init__(self):
        pass

    # Получение списка заявок с фильтрацией и пагинацией
    def get_report_request_list(self, start_date, end_date):
        url = Endpoint.list_endpoints(start_date=start_date, end_date=end_date)
        headers = Header().list_headers()
        response = requests.get(url, headers=headers)
        return response
    # Формирование пустых отчётов за прошлые периоды за которые не было отчётов
    def unlocking_order_creation(self):
        url = Endpoint.unlocking_order_creation_endpoint()
        headers = Header().unlocking_order_creation_headers()
        payload = Payload.unlocking_order_creation_payload()
        response = requests.post(url, headers=headers, data=payload)
        return response

    # получить список позиций заявки с фильтрацией. ReportingPeriodId
    def position_list(self):
        url = Endpoint.position_list()
        headers = Header().position_list_headers()
        response = requests.get(url, headers=headers)
        return response

    # Очистка всех позиций в форме создания отчета
    # Необходимо доработать
    def clear(self):
        url = Endpoint.clear_endpoint()
        headers = Header().clear_headers()
        payload = Payload.clear_payload()
        response = requests.delete(url, headers=headers, data=payload)
        return response

    #Добавить позицию в форму создания заявки на отчет
    def add_position(self,DetailId, Quantity):
        url = Endpoint.add_position_endpoint()
        headers = Header().add_position_headers()
        payload = Payload.add_position_payload(DetailId=DetailId, Quantity=Quantity)
        response = requests.post(url, headers=headers, data=payload)
        return response
    # Удалить конкректную деталь в форме создания заявки на отчет
    # Не работает, доделать
    def delete_position(self,detail_id: int, report_request_id: int):
        url = Endpoint.delete_position_endpoint()
        headers = Header().delete_position_headers()
        payload = Payload.delete_position_payload(detail_id=detail_id, report_request_id=report_request_id)
        response = requests.delete(url, headers=headers, json=payload)
        return response


if __name__ == '__main__':
    api = ReportRequestAPI()
    response = api.delete_position(detail_id=50427613, report_request_id=144)
    print(response)
