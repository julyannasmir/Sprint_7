import allure
import helper
from courier_api import CourierApi


class TestCreateCourier:
    @allure.title('Успешное создание курьера')
    def test_register_new_courier(self):
        body = helper.RegisterNewCourierHelper.create_courier_body()
        response = CourierApi.create_courier(body)
        assert response.status_code == 201
        assert str(response.json()) == "{'ok': True}"
        CourierApi.delete_created_courier(body)

    @allure.title('Создание двух одинаковых курьеров')
    def test_create_two_identical_couriers(self):
        body = helper.RegisterNewCourierHelper.create_courier_body()
        CourierApi.create_courier(body)
        response_2 = CourierApi.create_courier(body)
        assert response_2.status_code == 409
        assert response_2.json()['message'] == 'Этот логин уже используется. Попробуйте другой.'
        CourierApi.delete_created_courier(body)

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
    def test_create_courier_without_firstname(self):
        body = helper.RegisterNewCourierHelper.create_courier_body()
        body_without_field = helper.ChangeTestDataHelper.delete_field_from_created_courier_body(body, 'firstName')
        response = CourierApi.create_courier(body_without_field)
        assert response.status_code == 201
        assert str(response.json()) == "{'ok': True}"
        CourierApi.delete_created_courier(body_without_field)


