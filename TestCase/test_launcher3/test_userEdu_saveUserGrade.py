import pytest
import json
import requests
from Common.params import Params
from Conf.Config import Config
from Common import Assert


class TestSaveUserGrade:
    def test_response_data_format(self):
        """
        用例描述：用户年级关系保存接口默认参数状态码返回
        :return:
        """
        conf = Config()
        test = Assert.Assertions()

        host = conf.debug_gossapi_host
        api_url = host + "/userEdu/saveUserGrade"
        params = Params().encrypt_data({"openid": "ff5d5663695b00f97015588033c196c7", "gradeId": 3, "phone": ""})
        headers = conf.debug_headers

        res = requests.post(api_url, params=params, headers=headers)
        schema = json.load(open(conf.json_schema_path + "/userEdu_saveUserGrade_schema.json"))
        json_data = res.json()

        assert test.assert_code(res.status_code, 200)
        assert test.assert_code(json_data.get("code"), 200)
        assert test.assert_jsonschema(json_data, schema)


if __name__ == '__main__':
    pytest.main()
