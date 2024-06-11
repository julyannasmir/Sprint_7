import allure
import helper
from courier_api import CourierApi


class TestCreateCourier:
    @allure.title('Успешная авторизация курьера')
    def test_login_courier(self):
        body = helper.RegisterNewCourierHelper.create_courier_body()
        CourierApi.create_courier(body)
        response = CourierApi.login(body)
        assert response.status_code == 200
        assert 'id' in response.json()
        CourierApi.delete_created_courier(body)

    @allure.title('Авторизация без логина')
    def test_login_courier_without_login(self):
        body = helper.RegisterNewCourierHelper.create_courier_body()
        CourierApi.create_courier(body)
        login_body = helper.ChangeTestDataHelper.get_login_body(body)
        body_without_login = helper.ChangeTestDataHelper.delete_field_from_created_courier_body(login_body, 'login')
        response = CourierApi.login(body_without_login)
        assert response.status_code == 400
        CourierApi.delete_created_courier(body)

    @allure.title('Авторизация без пароля')
    def test_login_courier_without_pass(self):
        body = helper.RegisterNewCourierHelper.create_courier_body()
        CourierApi.create_courier(body)
        body_without_password = helper.ChangeTestDataHelper.delete_field_from_created_courier_body(body, 'password')
        response = CourierApi.login(body_without_password)
        assert response.status_code == 400
        CourierApi.delete_created_courier(body)

    @allure.title('Авторизация с некорректным логином')
    #
    def test_login_courier_incorrect_login(self):
        body = helper.RegisterNewCourierHelper.create_courier_body()
        CourierApi.create_courier(body)
        modified_courier_body = helper.ChangeTestDataHelper.change_field_in_created_courier_body(body, 'login', 'incorrect_login')
        response = CourierApi.login(modified_courier_body)
        assert response.status_code == 404
        assert response.json()['message'] == 'Учетная запись не найдена'
        CourierApi.delete_created_courier(body)

    @allure.title('Авторизация с некорректным паролем')
    #
    def test_login_courier_incorrect_pass(self):
        body = helper.RegisterNewCourierHelper.create_courier_body()
        CourierApi.create_courier(body)
        modified_courier_body = helper.ChangeTestDataHelper.change_field_in_created_courier_body(body, 'password', 'incorrect_password')
        response = CourierApi.login(modified_courier_body)
        assert response.status_code == 404
        assert response.json()['message'] == 'Учетная запись не найдена'
        CourierApi.delete_created_courier(body)