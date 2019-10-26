import json
import requests
from Common.params import Params
from Conf.Config import Config
from Common import Assert


class TestCoursePlayAddress:
    def test_response_data_format(self):
        """
        用例描述：播放地址接口默认参数状态码返回
        :return:
        """
        conf = Config()
        test = Assert.Assertions()

        host = conf.debug_gossapi_host
        api_url = host + "/course/playAddress"
        headers = conf.debug_headers
        params = Params().encrypt_data({"openId": "8c3484c9889525d2edb171b996686ecd",
                                        "coursewareId": "451511"})

        res = requests.post(api_url, params=params, headers=headers)
        schema = json.load(open(conf.json_schema_path + "/course_playAddress_schema.json"))
        json_data = res.json()
        assert test.assert_code(res.status_code, 200)
        assert test.assert_code(json_data.get("code"), 200)
        assert test.assert_jsonschema(json_data, schema)


if __name__ == '__main__':
    pass
