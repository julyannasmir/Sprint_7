import allure
import helper
from courier_api import CourierApi


class TestCreateCourier:
    @allure.title('Успешное создание курьера')
    def test_register_new_courier(self, courier):
        response = CourierApi.create_courier(courier)
        assert response.status_code == 201
        assert str(response.json()) == "{'ok': True}"

    @allure.title('Создание двух одинаковых курьеров')
    def test_create_two_identical_couriers(self, courier):
        CourierApi.create_courier(courier)
        response_2 = CourierApi.create_courier(courier)
        assert response_2.status_code == 409
        assert response_2.json()['message'] == 'Этот логин уже используется. Попробуйте другой.'

    @allure.title('Создание курьера без логина')
    def test_create_courier_without_login(self):
        body = helper.RegisterNewCourierHelper.create_courier_body()
        body_without_login = helper.ChangeTestDataHelper.delete_field_from_created_courier_body(body, 'login')
        response = CourierApi.create_courier(body_without_login)
        assert response.status_code == 400

    @allure.title('Создание курьера без пароля')
    def test_create_courier_without_pass(self):
        body = helper.RegisterNewCourierHelper.create_courier_body()
        body_without_pass = helper.ChangeTestDataHelper.delete_field_from_created_courier_body(body, 'password')
        response = CourierApi.create_courier(body_without_pass)
        assert response.status_code == 400

    @allure.title('Создание курьера без необязательного поля')
    def test_create_courier_without_firstname(self, courier):
        body_without_field = helper.ChangeTestDataHelper.delete_field_from_created_courier_body(courier, 'firstName')
        response = CourierApi.create_courier(body_without_field)
        assert response.status_code == 201
        assert str(response.json()) == "{'ok': True}"


