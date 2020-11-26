import pytest
import allure

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
    params = {
        "user_name": (None, username),
        "nickname": (None, nickname),
        "password": (None, password),
    }
    res = user.register(params=params)
    result.success = False
    if res.json()["code"] == 0:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["msg"])
    result.msg = res.json()["msg"]
    result.response = res
    logger.info("注册用户 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


@allure.step("步骤1 ==>> 注册用户")
def step_1(username, nickname, password):
    logger.info("Step1 ==>> 注册用户 ==>> {},{},{}".format(username, nickname, password))


@allure.severity(allure.severity_level.NORMAL)
@allure.epic("测试注册接口")
@allure.feature("用户注册模块")
class TestUserRegister:

    @allure.story("用例---注册用户")
    @allure.description("该用例为针对用户注册接口的测试")
    @allure.title(
        "测试数据：【{username}，{nickname}，{password}，{expect_result}，{expect_code}，{expect_msg}】"
    )
    @pytest.mark.single
    @pytest.mark.parametrize("username, nickname, password, expect_result, expect_code, expect_msg",
                             api_data["test_register_user"])
    def test_register_user(self, username, nickname, password, expect_result, expect_code, expect_msg):
        result = register_user(username, nickname, password)
        assert result.response.json().get("code") == expect_code
        assert expect_msg in result.msg


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_01_register.py"])
