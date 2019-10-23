import json
import requests
from Common.params import Params
from Conf.Config import Config
from Common import Assert


class TestCourseDetail:
    def test_response_code(self):
        """
        用例描述：图书馆标签详情接口状态码返回
        :return:
        """
        conf = Config()
        params = Params()
        test = Assert.Assertions()

        host = conf.debug_gossapi_host
        api_url = host + "/library/tagDetail"
        params.add_param("libraryId", 4512154)
        params.add_param("page", 1)
        params.add_param("pageSize", 10)
        params = params.encrypt_data()
        headers = conf.debug_headers

        res = requests.post(api_url, params=params, headers=headers)
        assert test.assert_code(res.status_code, 200)

    def test_jsonschema_validate(self):
        """
        用例描述：图书馆标签详情接口返回数据JsonSchema验证
        :return:
        """
        conf = Config()
        params = Params()
        test = Assert.Assertions()

        host = conf.debug_gossapi_host
        api_url = host + "/library/tagDetail"
        params.add_param("libraryId", 4512154)
        params.add_param("page", 1)
        params.add_param("pageSize", 10)
        params = params.encrypt_data()
        headers = conf.debug_headers
        schema = json.load(open(conf.json_schema_path + "/library_tag_detail_schema.json"))

        res = requests.post(api_url, params=params, headers=headers)
        assert test.assert_jsonschema(res.json(), schema)


if __name__ == '__main__':
    pass
