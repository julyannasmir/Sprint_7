import allure
import requests
import urls
from helper import ChangeTestDataHelper


class CourierApi:
    @staticmethod
    @allure.step("Логин в сервисе скутера")
    def login(body):
        return requests.post(urls.BASE_URL + urls.LOGIN_ENDPOINT, json=body)

    @staticmethod
    @allure.step("Логин в сервисе скутера и возврат id")
    def login_and_get_id(body):
        response = CourierApi.login(body).json()
        return response['id']

    @staticmethod
    @allure.step("Отправка запроса на создание курьера")
    def create_courier(body):
        return requests.post(urls.BASE_URL + urls.CREATE_COURIER_ENDPOINT, json=body)


