from data import BASE_URL, ORDERS_URL, ORDER_INFO
import json
import requests
import allure


class OrderMethods:

    def __init__(self):
        self.order_data = ORDER_INFO

    @allure.step('Создание заказа')
    def post_create_order(self):
        headers = {"Content-type": "application/json"}
        response = requests.post(f'{BASE_URL}{ORDERS_URL}', data=json.dumps(self.order_data), headers=headers)
        return response

    @allure.step('Получение списка заказов')
    def get_list_orders(self):
        params = {
            "limit": 1,
            "page": 0,
            "nearestStation": ["1", "2"]
        }
        response = requests.get(f'{BASE_URL}{ORDERS_URL}', json=params)
        return response