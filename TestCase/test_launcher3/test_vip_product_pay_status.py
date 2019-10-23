import json
import requests
from Common.params import Params
from Conf.Config import Config
from Common import Assert


class TestVipProductPayStatus:
    def test_repsonse_data_format(self):
        """
        用例描述：VIP商品支付状态接口状态码返回
        :return:
        """
        conf = Config()
        test = Assert.Assertions()

        host = conf.debug_gossapi_host
        api_url = host + "/vip/productPayStatus"
        params = Params().encrypt_data({"key": None}) # TODO
        headers = conf.debug_headers

        res = requests.post(api_url, params=params, headers=headers)
        schema = json.load(open(conf.json_schema_path + "/vip_product_pay_status_schema.json"))
        assert test.assert_code(res.status_code, 200)
        assert test.assert_jsonschema(res.json(), schema)


if __name__ == '__main__':
    pass
