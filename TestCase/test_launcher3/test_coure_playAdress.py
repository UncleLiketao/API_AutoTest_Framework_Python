import json
import requests
from Common.params import Params
from Conf.Config import Config
from Common import Assert


class TestCourse:
    def test_repsonse_code(self):
        """
        用例描述：播放地址接口默认参数状态码返回
        :return:
        """
        conf = Config()
        params = Params()
        test = Assert.Assertions()

        host = conf.debug_gossapi_host
        api_url = host + "/course/playAddress"
        params.add_param("openId", "8c3484c9889525d2edb171b996686ecd")
        params.add_param("coursewareId", "451511")

        params = params.encrypt_data()
        headers = conf.debug_headers

        res = requests.post(api_url, params=params, headers=headers)
        assert test.assert_code(res.status_code, 200)

    def test_jsonschema_validate(self):
        """
        用例描述：播放地址接口默认参数返回数据JsonSchema验证
        :return:
        """
        conf = Config()
        params = Params()
        test = Assert.Assertions()

        host = conf.debug_gossapi_host
        api_url = host + "/course/playAddress"
        params.add_param("openId", "8c3484c9889525d2edb171b996686ecd")
        params.add_param("coursewareId", "451511")

        params = params.encrypt_data()
        headers = conf.debug_headers

        res = requests.post(api_url, params=params, headers=headers)
        schema = json.load(open(conf.json_schema_path + "/course_playAddress_schema.json"))
        assert test.assert_jsonschema(res.json(), schema)


if __name__=='__main__':
    pass
