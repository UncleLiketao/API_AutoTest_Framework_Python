import json
import requests
from Common.params import Params
from Conf.Config import Config
from Common import Assert


class TestCourseSeminarDetail:
    def test_response_data_format(self):
        """
        用例描述：课程表/单课件专题详情接口返回状态码
        :return:
        """
        conf = Config()
        test = Assert.Assertions()

        host = conf.debug_gossapi_host
        api_url = host + "/course/seminarDetail"
        params = Params().encrypt_data({"contentId": "4512154"})
        headers = conf.debug_headers

        res = requests.post(api_url, params=params, headers=headers)
        schema = json.load(open(conf.json_schema_path + "/course_seminar_detail_schema.json"))
        json_data = res.json()

        assert test.assert_code(res.status_code, 200)
        assert test.assert_code(json_data.get("code"), 200)
        assert test.assert_jsonschema(json_data, schema)


if __name__ == '__main__':
    pass
