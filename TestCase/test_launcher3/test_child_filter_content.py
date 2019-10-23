import json
import requests
from Common.params import Params
from Conf.Config import Config
from Common import Assert


class TestChildFilterContent:
    def test_repsonse_code(self):
        """
        用例描述：【新版儿童模式】过滤器内容接口默认参数状态码返回
        :return:
        """
        conf = Config()
        params = Params()
        test = Assert.Assertions()

        host = conf.debug_gossapi_host
        api_url = host + "/child/filter/content"
        params.add_param("source", "iqiyi")
        params.add_param("dockId", "1")
        params.add_param("filters", [{"k": "筛选id", "v": "筛选值"}])
        params.add_param("page", "1")
        params.add_param("pageSize", "10")
        params.add_param("gender", "1")
        params.add_param("ageDuration", "1")


        params = params.encrypt_data()
        headers = conf.debug_headers

        res = requests.post(api_url, params=params, headers=headers)
        assert test.assert_code(res.status_code, 200)

    def test_jsonschema_validate(self):
        """
        用例描述：【新版儿童模式】过滤器内容默认参数返回数据JsonSchema验证
        :return:
        """
        conf = Config()
        params = Params()
        test = Assert.Assertions()

        host = conf.debug_gossapi_host
        api_url = host + "/child/filter/content"
        params.add_param("source", "iqiyi")
        params.add_param("dockId", "1")
        params.add_param("filters", [{"k": "筛选id", "v": "筛选值"}])
        params.add_param("page", "1")
        params.add_param("pageSize", "10")
        params.add_param("gender", "1")
        params.add_param("ageDuration", "1")
        params = params.encrypt_data()
        headers = conf.debug_headers

        res = requests.post(api_url, params=params, headers=headers)
        schema = json.load(open(conf.json_schema_path + "/child_filter_content_schema.json"))
        assert test.assert_jsonschema(res.json(), schema)


if __name__ == '__main__':
    pass
