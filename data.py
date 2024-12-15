class Message:
    CREATE_COURIER = '{"ok":true}'
    CREATE_EXISTING_COURIER = "Этот логин уже используется. Попробуйте другой."
    CREATE_COURIER_WITHOUT_LOGIN = "Недостаточно данных для создания учетной записи"
    LOGING_COURIER_WITHOUT_DATA = "Недостаточно данных для входа"
    LOGING_NOT_EXISTING_COURIER = "Учетная запись не найдена"


BASE_URL = 'https://qa-scooter.praktikum-services.ru/api/v1/'
ORDERS_URL = 'orders/'
COURIERS_URL = 'courier/'

ORDER_INFO = {
    "firstName": "Принут",
    "lastName": "Ловков",
    "address": "г. Москва",
    "metroStation": "1",
    "phone": "+79148828232",
    "rentTime": 1,
    "deliveryDate": "2024-11-02T21:00:00.000Z",
    "comment": "Самокат нужен к 9:00",
    "color": ["BLACK"]
}


