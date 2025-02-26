

# Метод для получения количества деталей в наличии у клиента
def get_product_quantity_by_detail_id(data, detail_id):
    for detail in data.get("Details", []):
        if detail.get("DetailId") == detail_id:
            return detail.get("Quantity")
    return None  # Если деталь не найдена


if __name__ == '__main__':
    from src.product.product_api import ProductAPI
    product_api = ProductAPI()
    data_product = product_api.product().json()
    quantity = get_product_quantity_by_detail_id(data_product, 50275938)
    print(quantity)