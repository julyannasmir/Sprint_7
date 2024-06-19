import pytest
import requests

import helper
import urls
from courier_api import CourierApi


@pytest.fixture()
def courier():
    courier = helper.RegisterNewCourierHelper.create_courier_body()
    yield courier
    if 'firstName' in courier:
        courier = helper.ChangeTestDataHelper.get_login_body(courier)
    courier_id = CourierApi.login_and_get_id(courier)
    requests.delete(urls.BASE_URL + urls.DELETE_COURIER_ENDPOINT + str(courier_id))
