import json
import requests
from Common.params import Params
from Conf.Config import Config
from Common import Assert


class TestGradeList:
    def test_response_data_format(self):
        """
        用例描述：年级列表接口默认参数状态码返回和返回格式JsonSchema格式验证
        :return:
        """
        conf = Config()
        test = Assert.Assertions()

        host = conf.debug_gossapi_host
        api_url = host + "/grade/list"
        params = Params().encrypt_data()
        headers = conf.debug_headers

        res = requests.post(api_url, params=params, headers=headers)
        schema = json.load(open(conf.json_schema_path + "/grade_list_schema.json"))

        assert test.assert_code(res.status_code, 200)
        assert test.assert_jsonschema(res.json(), schema)


if __name__ == '__main__':
    pass
