import allure
import random
import string
from faker import Faker
fake = Faker("ru_RU")


class ChangeTestDataHelper:
    @staticmethod
    @allure.step('Удаление поля из тела запроса на создание курьера')
    def delete_field_from_created_courier_body(body, key):
        body1 = body.copy()
        del body1[key]
        return body1

    @staticmethod
    @allure.step('Получение тела для логина курьера')
    def get_login_body(body):
        login_body = ChangeTestDataHelper.delete_field_from_created_courier_body(body, 'firstName').copy()
        return login_body

    @staticmethod
    @allure.step('Изменение поля в теле запроса на создание курьера')
    def change_field_in_created_courier_body(body, key, value):
        body1 = body.copy()
        body1[key] = value
        return body1


class RandomData:
    @staticmethod
    @allure.step('Генерация рандомной строки')
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string


class RegisterNewCourierHelper:
    @staticmethod
    @allure.step('Создание тела запроса для создания курьера')
    def create_courier_body():

        login = RandomData.generate_random_string(10)
        password = RandomData.generate_random_string(10)
        first_name = RandomData.generate_random_string(10)

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        return payload


class OrderHelper:
    @staticmethod
    @allure.step('Создание тела запроса для заказа')
    def create_order_body(color):
        name = fake.first_name()
        last_name = fake.last_name()
        address = fake.street_name()
        phone = random.randint(10000000000, 99999999999)
        comment = fake.text()
        metro = random.randint(0, 40)
        rent = random.randint(0, 6)

        payload = {
            "firstName": name,
            "lastName": last_name,
            "address": address,
            "metroStation": metro,
            "phone": phone,
            "rentTime": rent,
            "deliveryDate": "2020-06-06",
            "comment": comment,
            "color": color
        }
        return payload



