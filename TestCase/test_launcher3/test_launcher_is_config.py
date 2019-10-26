import pytest
import json
import requests
from Common.params import Params
from Conf.Config import Config
from Common import Assert


class TestLauncherIsConfig:
    def test_response_data_format(self):
        """
        用例描述：课程/课程表配置查询接口默认参数状态码返回和返回格式JsonSchema格式验证
        :return:
        """
        conf = Config()
        test = Assert.Assertions()

        host = conf.debug_goss_host
        api_url = host + "/api/v1/launcher/isConfig"
        headers = conf.debug_headers
        params = Params().non_encrypted_data({'sourceId': '10001', 'sourceType': 2})

        res = requests.post(api_url, params=params, headers=headers)
        schema = json.load(open(conf.json_schema_path + "/launcher_is_config_schema.json"))

        assert test.assert_code(res.status_code, 200)
        assert test.assert_jsonschema(res.json(), schema)


if __name__ == '__main__':
    pytest.main()
