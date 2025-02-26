import requests
# Метод для получения количества деталей из матрицы
def get_matrix_quantity(matrix_data, DetailId: int):
    for item in matrix_data['items']:
        if item['detailId'] == DetailId:
            return item['quantity']
    return 0 # Если деталь не найдена


if __name__ == '__main__':
    from src.matrix_client.matrix_client_api import MatrixClientApi
    client = MatrixClientApi()
    list_matrix = client.get_matrix_client_by_id(2).json()
    quantity = get_matrix_quantity(list_matrix, 50275938)
    print(quantity)
