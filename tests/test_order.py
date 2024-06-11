import allure
import pytest
import requests
import helper
import urls


class TestOrder:
    @allure.title('Создание нового заказа')
    @pytest.mark.parametrize('color', [["BLACK", "GREY"], []])
    def test_create_new_order(self, color):
        body = helper.OrderHelper.create_order_body(color)
        response = requests.post(urls.BASE_URL + urls.ORDER_ENDPOINT, json=body)
        assert response.status_code == 201
        assert 'track' in response.json()

    @allure.title('Получение списка заказов')
    def test_get_orders(self):
        response = requests.get(urls.BASE_URL + urls.ORDER_ENDPOINT)
        assert 'orders' in response.json()
