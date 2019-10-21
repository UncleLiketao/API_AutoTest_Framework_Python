import json
import os
import requests
from jsonschema import validate
from Common.Params import Params
from Conf.Config import Config


class TestIsConfig:
    def test_repsonse_code(self):
        """
        用例描述：【新版儿童模式】获取画面静止时随机播放内容接口默认参数状态码返回
        :return:
        """
        conf = Config()
        params = Params()

        host = "http://gossapit.xgimi.com"
        api_url = host + "/child/broadcast/list"
        params.add_param("broadcastScene", "1")
        params = params.encrypt_data()
        headers = {"Content-Type": "application/x-www-form-urlencoded"}

        res = requests.post(api_url, params=params, headers=headers)
        assert res.status_code == 200

    def test_jsonschema_validate(self):
        """
        用例描述：【新版儿童模式】获取画面静止时随机播放内容接口默认参数返回数据JsonSchema验证
        :return:
        """
        conf = Config()
        params = Params()

        host = "http://gossapit.xgimi.com"
        api_url = host + "/child/broadcast/list"
        params.add_param("broadcastScene", "1")
        params = params.encrypt_data()
        headers = {"Content-Type": "application/x-www-form-urlencoded"}

        res = requests.post(api_url, params=params, headers=headers)
        schema = json.load(open(conf.json_schema_path + "/child_broadcast_list_schema.json"))
        assert validate(instance=res.json(), schema=schema) is None


if __name__ == '__main__':
    testIsConfig = TestIsConfig()
    testIsConfig.test_repsonse_code()
    testIsConfig.test_jsonschema_validate()
