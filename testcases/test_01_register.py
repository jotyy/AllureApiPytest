import pytest

from api.user import user
from common.logger import logger
from core.result_base import ResultBase
from testcases.test_config import api_data


def register_user(username, nickname, password):
    """
    注册用户
    :param username: 用户名
    :param nickname: 昵称
    :param password: 密码
    :return: 用户信息
    """
    result = ResultBase()
    header = {
        "Content-Type": "multipart/form-data"
    }
    params = {
        "user_name": username,
        "nickname": nickname,
        "password": password
    }
    res = user.register(headers=header, params=params)
    if res.json()["code"] == 0:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["msg"])
    result.msg = res.json()["msg"]
    result.response = res
    logger.info("注册用户 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def step_1(username, nickname, password):
    logger.info("Step1 ==>> 注册用户 ==>> {},{},{}".format(username, nickname, password))


class TestUserRegister:
    @pytest.mark.parametrize("username, nickname, password, expect_result, expect_code, expect_msg",
                             api_data["test_register_user"])
    def test_register_user(self, username, nickname, password, expect_result, expect_code, expect_msg):
        result = register_user(username, nickname, password)
        assert result.success == expect_result, result.error
        assert result.response.status_code == 200
        assert result.success == expect_result, result.error
        assert result.response.json().get("code") == expect_code
        assert expect_msg in result.msg


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_01_register.py"])
