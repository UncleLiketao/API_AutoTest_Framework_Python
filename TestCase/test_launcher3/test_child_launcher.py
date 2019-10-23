import json
import requests
from Common.params import Params
from Conf.Config import Config
from Common import Assert


class TestChildLauncher:
    def test_repsonse_data_format(self):
        """
        用例描述：【新版儿童模式】桌面主页接口默认参数状态码返回
        :return:
        """
        conf = Config()
        test = Assert.Assertions()

        host = conf.debug_gossapi_host
        api_url = host + "/child/launcher"
        headers = conf.debug_headers
        params = Params().encrypt_data({"gender": 1, "ageDuration": 2})

        res = requests.post(api_url, params=params, headers=headers)
        schema = json.load(open(conf.json_schema_path + "/child_launcher_schema.json"))

        assert test.assert_code(res.status_code, 200)
        assert test.assert_jsonschema(res.json(), schema)


if __name__=='__main__':
    pass
