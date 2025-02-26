
# Метод для получения количества деталей в корзине
def get_basket_quantity(basket_data, detail_id):
    for detail in basket_data['BasketPositions']:
        if detail['DetailId'] == detail_id:
            return detail['Quantity']
    return 0  # Если деталь не найдена



if __name__ == '__main__':
    from src.basket.basket_api import BasketAPI
    api = BasketAPI()
    basket_data = api.get_basket().json()
    print(get_basket_quantity(basket_data, 50275938))
