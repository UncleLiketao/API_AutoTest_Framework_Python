import json
import requests
from Common.params import Params
from Conf.Config import Config
from Common import Assert


class TestVipProductList:
    def test_response_data_format(self):
        """
        用例描述：VIP商品列表接口状态码返回
        :return:
        """
        conf = Config()
        test = Assert.Assertions()

        host = conf.debug_gossapi_host
        api_url = host + "/vip/productList"
        params = Params().encrypt_data({"partner": "edu", "from": "edu"})
        headers = conf.debug_headers

        res = requests.post(api_url, params=params, headers=headers)
        schema = json.load(open(conf.json_schema_path + "/vip_product_list_schema.json"))
        json_data = res.json()

        assert res.status_code == 200
        assert json_data.get("code") == 200
        assert test.assert_jsonschema(json_data, schema)


if __name__ == '__main__':
    pass
