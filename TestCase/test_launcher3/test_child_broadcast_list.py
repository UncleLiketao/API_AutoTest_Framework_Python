import allure
import json
import requests
from Common.params import Params
from Conf.Config import Config
from Common import Assert


class TestIsConfig:
    @allure.severity('blocker')
    @allure.story('IsConfig')
    def test_repsonse_code(self):
        """
        用例描述：【新版儿童模式】获取画面静止时随机播放内容接口默认参数状态码返回
        :return:
        """
        conf = Config()
        params = Params()
        test = Assert.Assertions()

        host = conf.debug_gossapi_host
        api_url = host + "/child/broadcast/list"
        params.add_param("broadcastScene", "1")
        params = params.encrypt_data()
        headers = conf.debug_headers

        res = requests.post(api_url, params=params, headers=headers)
        assert test.assert_code(res.status_code, 200)

    @allure.severity('blocker')
    @allure.story('IsConfig')
    def test_jsonschema_validate(self):
        """
        用例描述：【新版儿童模式】获取画面静止时随机播放内容接口默认参数返回数据JsonSchema验证
        :return:
        """
        conf = Config()
        params = Params()
        test = Assert.Assertions()

        host = conf.debug_gossapi_host
        api_url = host + "/child/broadcast/list"
        params.add_param("broadcastScene", "1")
        params = params.encrypt_data()
        headers = conf.debug_headers

        res = requests.post(api_url, params=params, headers=headers)
        schema = json.load(open(conf.json_schema_path + "/child_broadcast_list_schema.json"))
        assert test.assert_jsonschema(res.json(), schema)


if __name__ == '__main__':
    testIsConfig = TestIsConfig()
    testIsConfig.test_repsonse_code()
    testIsConfig.test_jsonschema_validate()
