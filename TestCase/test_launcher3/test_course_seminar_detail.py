import json
import requests
from Common.params import Params
from Conf.Config import Config
from Common import Assert


class TestCourseSeminarDetail:
    def test_repsonse_data_format(self):
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

        assert test.assert_jsonschema(res.json(), schema)
        assert test.assert_code(res.status_code, 200)


if __name__ == '__main__':
    pass
