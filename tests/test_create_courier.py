import allure
import requests
import random
import string


class TestCreateCourier:
    @allure.title('Создание курьера')
    def test_register_new_courier(self):
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

        assert response.status_code == 201

    @allure.title('Нельзя создать двух одинаковых курьеров')
    def test_create_two_identical_couriers(self):
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)
        response_2 = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

        assert response_2.status_code == 409

    @allure.title('Создание курьера без логина без логина')
    def test_create_courier_without_login(self):
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

        password = generate_random_string(10)
        first_name = generate_random_string(10)

        payload = {
            "password": password,
            "firstName": first_name
        }

        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

        assert response.status_code == 400

    @allure.title('Создание курьера без пароля')
    def test_create_courier_without_pass(self):
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

        login = generate_random_string(10)
        first_name = generate_random_string(10)

        payload = {
            "login": login,
            "firstName": first_name
        }

        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

        assert response.status_code == 400

    @allure.title('Корректный код ответа')
    def test_create_courier_status_code(self):
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

        assert response.status_code == 201

    @allure.title('Корректное тело ответа')
    def test_create_courier_response_body(self):
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

        assert str(response.json()) == "{'ok': True}"

    @allure.title('Запрос без одного поля')
    def test_create_courier_without_firstname(self):
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

        login = generate_random_string(10)
        password = generate_random_string(10)

        payload = {
            "login": login,
            "password": password
        }

        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

        assert response.status_code == 201

    @allure.title('если создать пользователя с логином, который уже есть, возвращается ошибка.')
    def test_create_two_identical_couriers_response_body(self):
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)
        response_2 = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

        assert response_2.json()['message'] == 'Этот логин уже используется. Попробуйте другой.'

