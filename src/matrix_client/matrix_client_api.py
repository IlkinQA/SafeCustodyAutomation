import requests
from src.matrix_client.headers import Headers
from src.matrix_client.payloads import Payload
from src.matrix_client.endpoints import Endpoints

class MatrixClientApi:
    def __init__(self):
        pass

    def get_matrix_client_by_id(self, matrix_client_id):
        """
        :param matrix_client_id:  
        :return:
        """
        url = Endpoints.get_matrix_by_id(matrix_client_id)
        headers = Headers().get_matrix_by_id_headers()
        response = requests.get(url, headers=headers)
        return response


if __name__ == '__main__':
    client = MatrixClientApi()
    response = client.get_matrix_client_by_id(2)
    print(response.json())