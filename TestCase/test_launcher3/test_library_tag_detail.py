import json
import requests
from Common.params import Params
from Conf.Config import Config
from Common import Assert


class TestLibraryTagDetail:
    def test_repsonse_data_format(self):
        """
        用例描述：图书馆标签详情接口状态码返回
        :return:
        """
        conf = Config()
        test = Assert.Assertions()

        host = conf.debug_gossapi_host
        api_url = host + "/library/tagDetail"
        params = Params().encrypt_data({"libraryId": 4512154, "page": 1, "pageSize": 10})
        headers = conf.debug_headers

        res = requests.post(api_url, params=params, headers=headers)
        schema = json.load(open(conf.json_schema_path + "/library_tag_detail_schema.json"))
        assert test.assert_code(res.status_code, 200)
        assert test.assert_jsonschema(res.json(), schema)


if __name__=='__main__':
    pass
