import pytest
import requests

from api.api_config import BASE_URL


def get_token():
    header = {'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8'}
    params = {
        "user_name": "admin",
        "password": "123456",
    }
    res = requests.post(
        url=BASE_URL + "/login",
        data=params,
        headers=header)
    return res.json()["data"]["token"]


@pytest.fixture(scope="class")
def authorization():
    return {
        "Authorization": "Bearer {}".format(get_token())
    }
