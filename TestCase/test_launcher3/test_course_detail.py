import json
import requests
from Common.params import Params
from Conf.Config import Config
from Common import Assert


class TestCourseDetail:
    def test_response_data_format(self):
        """
        用例描述：课程详情接口状态码返回
        :return:
        """
        conf = Config()
        test = Assert.Assertions()

        host = conf.debug_gossapi_host
        api_url = host + "/course/detail"
        headers = conf.debug_headers
        params = Params().encrypt_data({"contentId": "4512154"})
        print(params)

        schema = json.load(open(conf.json_schema_path + "/course_detail_schema.json"))
        res = requests.post(api_url, params=params, headers=headers)
        assert test.assert_code(res.status_code, 200)
        assert test.assert_jsonschema(res.json(), schema)


if __name__ == '__main__':
    pass
