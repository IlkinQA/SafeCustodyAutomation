import os
from dotenv import load_dotenv
load_dotenv()

class Endpoints:

    get_basket = f'{os.getenv('HOST')}/Basket'
    post_Excel = f'{os.getenv('HOST')}/Basket/AsExcel'
    delete_position = f'{os.getenv('HOST')}/Basket/Position'
    add_position = f'{os.getenv('HOST')}/Basket/Position'
    put_position = f'{os.getenv('HOST')}/Basket/Position'
    clear_basket = f'{os.getenv('HOST')}/Basket/Clear'
    replenishment = f'{os.getenv('HOST')}/Basket/Replenishment'
    load_from_excel = f'{os.getenv('HOST')}/Basket/LoadFromExcel'
    actualize = f'{os.getenv('HOST')}/Basket/Actualize'

def main():
    endpoints = Endpoints()
    print(endpoints.get_basket)

if __name__ == '__main__':
    main()