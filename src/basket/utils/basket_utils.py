import requests
# Метод для получения количества деталей из матрицы
def get_matrix_quantity(matrix_data, DetailId: int):
    for item in matrix_data['items']:
        if item['detailId'] == DetailId:
            return item['quantity']
    return 0 # Если деталь не найдена

# Метод для получения количества деталей в наличии у клиента
def get_product_quantity(product_data, detail_id):
    for detail in product_data['BasketPositions']:
        if detail['DetailId'] == detail_id:
            return detail['Quantity']
    return 0  # Если деталь не найдена

# Метод для получения количества деталей в корзине
def get_basket_quantity(basket_data, detail_id):
    for detail in basket_data['BasketPositions']:
        if detail['DetailId'] == detail_id:
            return detail['Quantity']
    return 0  # Если деталь не найдена

if __name__ == '__main__':
    requests_matrix_json = {
    "pagedInfo": {
        "currentPage": 1,
        "totalPages": 1,
        "pageSize": 50,
        "totalCount": 2,
        "hasPrevious": False,
        "hasNext": False
    },
    "items": [
        {
            "id": 8681,
            "makerId": 2670,
            "makerName": "IBERIS",
            "detailId": 50427481,
            "detailNumber": "IB4031",
            "detailName": "СТУПИЦА КОЛЕСА ПЕР FORD FOCUS II (DA_) (ABS)",
            "detailGroupId": 498,
            "detailGroupName": "03.10 Ступица",
            "matrixId": 2,
            "matrixName": "test2",
            "quantity": 6
        },
        {
            "id": 11131,
            "makerId": 2670,
            "makerName": "IBERIS",
            "detailId": 50275938,
            "detailNumber": "IB2043",
            "detailName": "КАТУШКА ЗАЖИГАНИЯ A4 III (8EC, B7), A6 VW GOLF, PASSAT, POLO",
            "detailGroupId": 364,
            "detailGroupName": "10.02 Катушки зажигания",
            "matrixId": 2,
            "matrixName": "test2",
            "quantity": 3
        }
    ]
}

    requests = get_matrix_quantity(requests_matrix_json, 50275938)
    print(requests)