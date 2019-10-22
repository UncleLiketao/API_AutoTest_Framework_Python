import pytest
import json
import requests
from Common.params import Params
from Conf.Config import Config
from Common import Assert


class TestSaveUserGrade:
    def test_repsonse_code(self):
        """
        用例描述：用户年级关系保存接口默认参数状态码返回
        :return:
        """
        conf = Config()
        params = Params()
        test = Assert.Assertions()

        host = conf.debug_gossapi_host
        api_url = host + "/userEdu/saveUserGrade"
        params.add_param("openid", "ff5d5663695b00f97015588033c196c7")
        params.add_param("gradeId", 3)
        params.add_param("phone", "")
        params = params.encrypt_data()
        headers = conf.debug_headers

        res = requests.post(api_url, params=params, headers=headers)
        assert test.assert_code(res.status_code, 200)

    def test_jsonschema_validate(self):
        """
        用例描述：用户年级关系保存接口默认参数返回数据JsonSchema验证
        :return:
        """
        conf = Config()
        params = Params()
        test = Assert.Assertions()

        host = conf.debug_gossapi_host
        api_url = host + "/userEdu/saveUserGrade"
        params.add_param("openid", "ff5d5663695b00f97015588033c196c7")
        params.add_param("gradeId", 3)
        params.add_param("phone", "")
        params = params.encrypt_data()
        headers = conf.debug_headers

        res = requests.post(api_url, params=params, headers=headers)
        schema = json.load(open(conf.json_schema_path + "/userEdu_saveUserGrade_schema.json"))
        assert test.assert_jsonschema(res.json(), schema)


if __name__ == '__main__':
    pytest.main()
