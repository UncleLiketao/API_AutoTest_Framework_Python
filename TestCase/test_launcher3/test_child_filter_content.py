import json
import requests
from Common.params import Params
from Conf.Config import Config
from Common import Assert


class TestChildFilterContent:
    def test_response_data_format(self):
        """
        用例描述：【新版儿童模式】过滤器内容接口默认参数状态码返回
        :return:
        """
        conf = Config()
        test = Assert.Assertions()

        host = conf.debug_gossapi_host
        api_url = host + "/child/filter/content"
        params = Params().encrypt_data({"source": "iqiyi", "dockId": "1", "filters": [{"k": "1", "v": "1"}],
                                        "page": "1", "pageSize": "10", "gender": "1", "ageDuration": "1"})
        headers = conf.debug_headers

        res = requests.post(api_url, params=params, headers=headers)
        print(res.json())
        schema = json.load(open(conf.json_schema_path + "/child_filter_content_schema.json"))

        assert test.assert_code(res.status_code, 200)
        assert test.assert_jsonschema(res.json(), schema)


if __name__ == '__main__':
    pass
