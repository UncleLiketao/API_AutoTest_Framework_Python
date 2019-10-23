import json
import requests
from Common.params import Params
from Conf.Config import Config
from Common import Assert


class TestCourseDetail:
    def test_response_code(self):
        """
        用例描述：VIP商品二维码接口状态码返回
        :return:
        """
        conf = Config()
        params = Params()
        test = Assert.Assertions()

        host = conf.debug_gossapi_host
        api_url = host + "/vip/productQrCode"
        params.add_param("openid", "kh54gh2j3g563gc673jh")
        params.add_param("mobile", "15770843323")
        params.add_param("product_id", "23")
        params.add_param("service", "edu.pay")
        params.add_param("from", "edu")
        params = params.encrypt_data()
        headers = conf.debug_headers

        res = requests.post(api_url, params=params, headers=headers)
        assert test.assert_code(res.status_code, 200)

    def test_jsonschema_validate(self):
        """
        用例描述：VIP商品二维码接口返回数据JsonSchema验证
        :return:
        """
        conf = Config()
        params = Params()
        test = Assert.Assertions()

        host = conf.debug_gossapi_host
        api_url = host + "/vip/productQrCode"
        params.add_param("openid", "kh54gh2j3g563gc673jh")
        params.add_param("mobile", "15770843323")
        params.add_param("product_id", "23")
        params.add_param("service", "edu.pay")
        params.add_param("from", "edu")
        params = params.encrypt_data()
        headers = conf.debug_headers
        schema = json.load(open(conf.json_schema_path + "/vip_product_pay_status_schema.json"))

        res = requests.post(api_url, params=params, headers=headers)
        assert test.assert_jsonschema(res.json(), schema)


if __name__ == '__main__':
    pass
