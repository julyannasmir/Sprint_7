import allure
import requests
from Helper import RegisterNewCourierHelper


class TestCreateCourier:
    @allure.title('Авторизация курьера')
    def test_login_courier(self):
        login_pass = RegisterNewCourierHelper.register_new_courier_and_return_login_password()
        payload = {
            "login": login_pass[0],
            "password": login_pass[1],
        }
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=payload)
        assert response.status_code == 200
        assert 'id' in response.json()

    @allure.title('Авторизация без логина')
    def test_login_courier_without_login(self):
        login_pass = RegisterNewCourierHelper.register_new_courier_and_return_login_password()
        payload = {
            "password": login_pass[1]
        }
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=payload)
        assert response.status_code == 400

    @allure.title('Авторизация без пароля')
    def test_login_courier_without_pass(self):
        login_pass = RegisterNewCourierHelper.register_new_courier_and_return_login_password()
        payload = {
            "password": login_pass[1]
        }
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=payload)
        assert response.status_code == 400

    @allure.title('система вернёт ошибку, если неправильно указать логин')
    #
    def test_login_courier_incorrect_login(self):
        login_pass = RegisterNewCourierHelper.register_new_courier_and_return_login_password()
        payload = {
            "login": data.RegisterNewCourierHelper.generate_random_string(10),
            "password": login_pass[1],
        }
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=payload)
        assert response.status_code == 404
        assert response.json()['message'] == 'Учетная запись не найдена'

    @allure.title('система вернёт ошибку, если неправильно указать пароль')
    #
    def test_login_courier_incorrect_pass(self):
        login_pass = RegisterNewCourierHelper.register_new_courier_and_return_login_password()
        payload = {
            "login": login_pass[0],
            "password": data.RegisterNewCourierHelper.generate_random_string(10),
        }
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=payload)
        assert response.status_code == 404
        assert response.json()['message'] == 'Учетная запись не найдена'