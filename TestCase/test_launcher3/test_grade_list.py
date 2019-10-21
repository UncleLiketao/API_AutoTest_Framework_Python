# -*- coding: utf-8 -*-
# @Time    : 2019/10/17 下午4:14
# @Author  : LiKeTao
# @File    : test_grade_list.py
import json
import os
import requests
from jsonschema import validate
from Common.Params import Params
from Conf.Config import Config

schema_path = os.path.abspath('..') + '\\' + 'JSONSchema' + '\\'
print(schema_path)


class TestGradeList:
    def test_repsonse_code(self):
        """
        用例描述：年级列表接口默认参数状态码返回
        :return:
        """
        host = "http://gossapit.xgimi.com"
        api_url = host + "/grade/list"
        params = Params().encrypt_data()
        headers = {"Content-Type": "application/x-www-form-urlencoded"}

        res = requests.post(api_url, params=params, headers=headers)
        assert res.status_code == 200

    def test_jsonschema_validate(self):
        """
        用例描述：年级列表接口默认参数返回数据JsonSchema验证
        :return:
        """
        conf = Config()
        host = "http://gossapit.xgimi.com/"
        api_url = host + "grade/list"
        params = Params().encrypt_data()
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        schema = json.load(open(conf.json_schema_path + "/grade_list_schema.json"))

        res = requests.post(api_url, params=params, headers=headers)
        assert validate(instance=res.json(), schema=schema) is None


if __name__ == '__main__':
    testGradeList = TestGradeList()
    testGradeList.test_repsonse_code()
    testGradeList.test_jsonschema_validate()
