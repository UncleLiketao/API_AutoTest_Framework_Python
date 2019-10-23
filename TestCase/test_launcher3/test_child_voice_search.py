import json
import requests
from Common.params import Params
from Conf.Config import Config
from Common import Assert


class TestChildVoiceSearch:
    def test_repsonse_code(self):
        """
        用例描述：【新版儿童模式】语音搜索接口默认参数状态码返回
        :return:
        """
        conf = Config()
        params = Params()
        test = Assert.Assertions()

        host = conf.debug_gossapi_host
        api_url = host + "/child/voice/search"
        params.add_param("film", "小猪佩奇")
        params.add_param("filmType", "动画片")
        params.add_param("fileSubType", "开心")
        params.add_param("filmTag", "动作")
        params.add_param("filmLanguage", "英语")
        params.add_param("filmArea", "美国")
        params.add_param("newest", "1")
        params.add_param("hottest", "1")
        params.add_param("highScore", "1")
        params.add_param("gender", "1")
        params.add_param("ageDuration", "1")
        params.add_param("page", "1")
        params.add_param("pageSize", "1")
        params.add_param("uiMode", "4")
        params.add_param("guide", "")
        params.add_param("guideTips", "")
        params.add_param("keyWords", "")


        params = params.encrypt_data()
        headers = conf.debug_headers

        res = requests.post(api_url, params=params, headers=headers)
        assert test.assert_code(res.status_code, 200)

    def test_jsonschema_validate(self):
        """
        用例描述：【新版儿童模式】过滤器内容默认参数返回数据JsonSchema验证
        :return:
        """
        conf = Config()
        params = Params()
        test = Assert.Assertions()

        host = conf.debug_gossapi_host
        api_url = host + "/child/voice/search"
        params.add_param("film", "小猪佩奇")
        params.add_param("filmType", "动画片")
        params.add_param("fileSubType", "开心")
        params.add_param("filmTag", "动作")
        params.add_param("filmLanguage", "英语")
        params.add_param("filmArea", "美国")
        params.add_param("newest", "1")
        params.add_param("hottest", "1")
        params.add_param("highScore", "1")
        params.add_param("gender", "1")
        params.add_param("ageDuration", "1")
        params.add_param("page", "1")
        params.add_param("pageSize", "1")
        params.add_param("uiMode", "4")
        params.add_param("guide", "")
        params.add_param("guideTips", "")
        params.add_param("keyWords", "")
        params = params.encrypt_data()
        headers = conf.debug_headers

        res = requests.post(api_url, params=params, headers=headers)
        schema = json.load(open(conf.json_schema_path + "/child_voice_search_schema.json"))
        assert test.assert_jsonschema(res.json(), schema)


if __name__ == '__main__':
    pass
