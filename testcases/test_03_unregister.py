import allure
import pytest

from api.user import user
from common.logger import logger
from core.result_base import ResultBase
from testcases.test_config import api_data


def unregister_user(username):
    """
    注销账户
    :param username: 用户名
    :return:
    """
    result = ResultBase()
    params = {
        "user_name": username,
    }
    res = user.unregister(params=params)
    result.success = False
    if res.json()["code"] == 0:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["msg"])
    result.msg = res.json()["msg"]
    result.response = res
    logger.info("注销用户 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


@allure.step("步骤3 ==>> 注销用户")
def step_1(username, nickname, password):
    logger.info("Step1 ==>> 注销用户 ==>> {},{},{}".format(username, nickname, password))


@allure.severity(allure.severity_level.NORMAL)
@allure.epic("测试注销接口")
@allure.feature("用户注销模块")
class TestUserUnRegister:

    @allure.story("用例---注销用户")
    @allure.description("该用例为针对用户注销接口的测试")
    @allure.title(
        "测试数据：【{username}，{expect_result}，{expect_code}，{expect_msg}】"
    )
    @pytest.mark.single
    @pytest.mark.parametrize("username, expect_result, expect_code, expect_msg",
                             api_data["test_unregister_user"])
    def test_unregister_user(self, username, expect_result, expect_code, expect_msg):
        result = unregister_user(username)
        assert result.response.json().get("code") == expect_code
        assert expect_msg in result.msg


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_03_unregister.py"])
