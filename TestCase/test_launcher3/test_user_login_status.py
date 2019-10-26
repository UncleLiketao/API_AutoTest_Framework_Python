import json
import requests
from Common.params import Params
from Conf.Config import Config
from Common import Assert


class TestUserLoginStatus:
    def test_response_data_format(self):
        """
        用例描述：用户登录状态接口状态码返回
        :return:
        """
        conf = Config()
        test = Assert.Assertions()

        host = conf.debug_gossapi_host
        api_url = host + "/user/loginStatus"
        params = Params().encrypt_data({"key": None})  # TODO: key的来源为/vip/productQrCode接口
        headers = conf.debug_headers

        schema = json.load(open(conf.json_schema_path + "/user_login_status_schema.json"))
        res = requests.post(api_url, params=params, headers=headers)
        json_data = res.json()

        assert test.assert_code(res.status_code, 200)
        assert test.assert_code(json_data.get("code"), 200)
        assert test.assert_jsonschema(json_data, schema)


if __name__ == '__main__':
    pass
