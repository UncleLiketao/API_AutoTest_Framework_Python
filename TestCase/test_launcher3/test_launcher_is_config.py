import pytest
import json
import requests
from Common.params import Params
from Conf.Config import Config
from Common import Assert


class TestLauncherIsConfig:
    def test_repsonse_code(self):
        """
        用例描述：课程/课程表配置查询接口默认参数状态码返回
        :return:
        """
        conf = Config()
        params = Params()
        test = Assert.Assertions()

        host = conf.debug_goss_host
        api_url = host + "/api/v1/launcher/isConfig"
        params.add_param("sourceId", "1000")
        params.add_param("sourceType", 2)
        params = params.encrypt_data()
        headers = conf.debug_headers

        res = requests.post(api_url, params=params, headers=headers)
        assert test.assert_code(res.status_code, 200)

    def test_jsonschema_validate(self):
        """
        用例描述：课程/课程表配置查询接口默认参数返回数据JsonSchema验证
        :return:
        """
        conf = Config()
        params = Params()
        test = Assert.Assertions()

        host = conf.debug_goss_host
        api_url = host + "/api/v1/launcher/isConfig"
        params.add_param("sourceId", "1000")
        params.add_param("sourceType", 2)
        params = params.encrypt_data()
        headers = conf.debug_headers

        res = requests.post(api_url, params=params, headers=headers)
        schema = json.load(open(conf.json_schema_path + "/launcher_is_config_schema.json"))
        assert test.assert_jsonschema(res.json(), schema)


if __name__ == '__main__':
    pytest.main()
