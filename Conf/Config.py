# -*- coding: utf-8 -*-
# @Time    : 2018/7/25 上午10:46
# @Author  : WangJuan
# @File    : Config.py

from configparser import ConfigParser
from Common import Log
import os


class Config:
    # path
    path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

    def __init__(self):
        """
        初始化
        """
        self.config = ConfigParser()
        self.log = Log.MyLog()

        self.xml_report_path = Config.path_dir + '/Report/xml'
        self.html_report_path = Config.path_dir + '/Report/html'
        self.json_schema_path = Config.path_dir + '/TestCase/JSONschema'
        self.debug_gossapi_host = "http://gossapit.xgimi.com"
        self.debug_goss_host = "http://goss.t.xgimi.com"
        self.debug_headers = {"Content-Type": "application/x-www-form-urlencoded"}

    def get_conf(self, title, value):
        """
        配置文件读取
        :param title:
        :param value:
        :return:
        """
        return self.config.get(title, value)

    def set_conf(self, title, value, text):
        """
        配置文件修改
        :param title:
        :param value:
        :param text:
        :return:
        """
        self.config.set(title, value, text)
        with open(self.conf_path, "w+") as f:
            return self.config.write(f)

    def add_conf(self, title):
        """
        配置文件添加
        :param title:
        :return:
        """
        self.config.add_section(title)
        with open(self.conf_path, "w+") as f:
            return self.config.write(f)
