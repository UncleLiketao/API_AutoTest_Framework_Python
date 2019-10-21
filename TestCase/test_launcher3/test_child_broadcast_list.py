import json
import os
import requests
from jsonschema import validate
from Common.params import Params

schema_path = os.path.abspath('..') + '\\' + 'JSONSchema' + '\\'
print(schema_path)


class TestIsConfig:
    def test_repsonse_code(self):
        """
        用例描述：【新版儿童模式】获取画面静止时随机播放内容接口默认参数状态码返回
        :return:
        """
        host = "http://gossapit.xgimi.com"
        api_url = host + "/child/broadcast/list"
        params = Params()
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
        host = "http://gossapit.xgimi.com"
        api_url = host + "/child/broadcast/list"
        params = Params()
        params.add_param("broadcastScene", "1")
        params = params.encrypt_data()
        headers = {"Content-Type": "application/x-www-form-urlencoded"}

        res = requests.post(api_url, params=params, headers=headers)
        schema = json.load(open(schema_path + "child_broadcast_list_schema.json"))
        assert validate(instance=res.json(), schema=schema) is None


if __name__ == '__main__':
    testIsConfig = TestIsConfig()
    testIsConfig.test_repsonse_code()
    testIsConfig.test_jsonschema_validate()
