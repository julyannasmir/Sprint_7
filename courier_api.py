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

    @staticmethod
    @allure.step("Удаление созданного курьера")
    def delete_created_courier(body):
        if 'firstName' in body:
            body = ChangeTestDataHelper.get_login_body(body)
        courier_id = CourierApi.login_and_get_id(body)
        return requests.delete(urls.BASE_URL + urls.DELETE_COURIER_ENDPOINT + str(courier_id))

