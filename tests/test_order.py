from random import randint
import allure
import pytest
import requests
from faker import Faker
fake = Faker("ru_RU")


class TestOrder:
    @allure.title('Создание нового заказа')
    @pytest.mark.parametrize('color', ["BLACK", "GREY", ["BLACK", "GREY"], ''])
    def test_create_new_order(self, color):
        name = fake.first_name()
        last_name = fake.last_name()
        address = fake.street_name()
        phone = randint(10000000000, 99999999999)
        comment = fake.text()
        metro = randint(0, 40)
        rent = randint(0, 6)

        payload = {
            "firstName": name,
            "lastName": last_name,
            "address": address,
            "metroStation": metro,
            "phone": phone,
            "rentTime": rent,
            "deliveryDate": "2020-06-06",
            "comment": comment,
            "color": [
                color
            ]
        }
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/orders', data=payload)
        assert response.status_code == 201
        assert 'track' in response.json()

    @allure.title('Получение списка заказов')
    def test_get_orders(self):
        response = requests.get('https://qa-scooter.praktikum-services.ru/api/v1/orders')
        assert 'orders' in response.json()
