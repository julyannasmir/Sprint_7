import allure
import helper
from courier_api import CourierApi


class TestCreateCourier:
    @allure.title('Успешная авторизация курьера')
    def test_login_courier(self, courier):
        CourierApi.create_courier(courier)
        response = CourierApi.login(courier)
        assert response.status_code == 200
        assert 'id' in response.json()

    @allure.title('Авторизация без логина')
    def test_login_courier_without_login(self, courier):
        CourierApi.create_courier(courier)
        login_body = helper.ChangeTestDataHelper.get_login_body(courier)
        body_without_login = helper.ChangeTestDataHelper.delete_field_from_created_courier_body(login_body, 'login')
        response = CourierApi.login(body_without_login)
        assert response.status_code == 400

    @allure.title('Авторизация без пароля')
    def test_login_courier_without_pass(self, courier):
        CourierApi.create_courier(courier)
        body_without_password = helper.ChangeTestDataHelper.delete_field_from_created_courier_body(courier, 'password')
        response = CourierApi.login(body_without_password)
        assert response.status_code == 400

    @allure.title('Авторизация с некорректным логином')
    #
    def test_login_courier_incorrect_login(self, courier):
        CourierApi.create_courier(courier)
        modified_courier_body = helper.ChangeTestDataHelper.change_field_in_created_courier_body(courier, 'login', 'incorrect_login')
        response = CourierApi.login(modified_courier_body)
        assert response.status_code == 404
        assert response.json()['message'] == 'Учетная запись не найдена'

    @allure.title('Авторизация с некорректным паролем')
    #
    def test_login_courier_incorrect_pass(self, courier):
        CourierApi.create_courier(courier)
        modified_courier_body = helper.ChangeTestDataHelper.change_field_in_created_courier_body(courier, 'password', '123')
        response = CourierApi.login(modified_courier_body)
        assert response.status_code == 404
        assert response.json()['message'] == 'Учетная запись не найдена'
