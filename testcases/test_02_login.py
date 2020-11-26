import allure
import pytest

from api.user import user
from common.logger import logger
from core.result_base import ResultBase
from testcases.test_config import api_data


def login_user(username, password):
    """
    用户登录
    :param username: 用户名
    :param password: 密码
    :return:
    """
    result = ResultBase()
    header = {'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8'}
    params = {
        "user_name": username,
        "password": password,
    }
    res = user.login(data=params, headers=header)
    result.success = False
    if res.json()["code"] == 0:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["msg"])
    result.msg = res.json()["msg"]
    result.response = res
    logger.info("用户登录 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


@allure.step("步骤2 ==> 用户登录")
def step_2(username, password):
    logger.info("Step2 ==>> 用户登录 ==>> {},{}".format(username, password))


@allure.severity(allure.severity_level.NORMAL)
@allure.epic("测试登录接口")
@allure.feature("用户登录模块")
class TestUserLogin:

    @allure.story("用例---登录用户")
    @allure.description("该用例为针对用户登录接口的测试")
    @allure.title(
        "测试数据：【{username}，{password}，{expect_result}，{expect_code}，{expect_msg}】"
    )
    @pytest.mark.single
    @pytest.mark.parametrize("username, password, expect_result, expect_code, expect_msg",
                             api_data["test_login_user"])
    def test_login_user(self, username, password, expect_result, expect_code, expect_msg):
        result = login_user(username, password)
        assert result.response.json().get("code") == expect_code
        assert expect_msg in result.msg


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_02_login.py"])
