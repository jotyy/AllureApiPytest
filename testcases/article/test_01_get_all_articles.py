import allure
import pytest

from api.article import article
from common.logger import logger
from core.result_base import ResultBase
from testcases.conftest import api_data


def get_all_articles(header):
    result = ResultBase()
    res = article.getAllArticles(headers=header)
    if res.json()["code"] == 0:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["msg"])
    result.msg = res.json()["msg"]
    result.response = res
    logger.info("获取所有文章 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


@allure.step("Step1 ==>> 获取所有文章")
def step_1(header):
    logger.info("Step1 ==>> 获取所有文章")


@allure.severity(allure.severity_level.NORMAL)
@allure.epic("测试注销接口")
@allure.feature("文章模块")
class TestGetAllArticles:

    @allure.story("用例---获取所有文章")
    @allure.description("该用例为针对用户注销接口的测试")
    @allure.title(
        "测试数据：【{expect_result}，{expect_code}，{expect_msg}】"
    )
    @pytest.mark.single
    @pytest.mark.parametrize("expect_result, expect_code, expect_msg",
                             api_data["test_get_all_articles"])
    def test_get_all_articles(self, authorization, expect_result, expect_code, expect_msg):
        result = get_all_articles(authorization)
        assert result.response.json().get("code") == expect_code
        assert expect_msg in result.msg


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_01_get_all_articles.py"])
