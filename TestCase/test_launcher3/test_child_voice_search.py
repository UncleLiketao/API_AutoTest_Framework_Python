import json
import requests
from Common.params import Params
from Conf.Config import Config
from Common import Assert


class TestChildVoiceSearch:
    def test_response_data_format(self):
        """
        用例描述：【新版儿童模式】语音搜索接口默认参数状态码返回
        :return:
        """
        conf = Config()
        test = Assert.Assertions()

        host = conf.debug_gossapi_host
        api_url = host + "/child/voice/search"
        headers = conf.debug_headers
        params = Params().encrypt_data({"film": "小猪佩奇", "filmType": "动画片", "fileSubType": "开心", "filmTag": "动作",
                                        "filmLanguage": "英语", "filmArea": "美国", "newest": "1", "hottest": "1",
                                        "highScore": "1", "gender": "1", "ageDuration": "1", "page": "1",
                                        "pageSize": "1",
                                        "uiMode": 4, "guide": "", "guideTips": "", "keyWords": ""})

        res = requests.post(api_url, params=params, headers=headers)
        schema = json.load(open(conf.json_schema_path + "/child_voice_search_schema.json"))

        assert test.assert_code(res.status_code, 200)
        assert test.assert_jsonschema(res.json(), schema)


if __name__ == '__main__':
    pass
