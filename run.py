import pytest
from Common import Log
from Common import Shell
from Conf import Config

if __name__ == '__main__':
    conf = Config.Config()
    log = Log.MyLog()

    shell = Shell.Shell()
    xml_report_path = conf.xml_report_path
    html_report_path = conf.html_report_path

    # 定义测试集
    args = ['-s', '-q', '--alluredir', xml_report_path]
    pytest.main(args)

    cmd = 'allure generate %s -o %s' % (xml_report_path, html_report_path)

    try:
        shell.invoke(cmd)
    except Exception:
        log.error('执行用例失败，请检查环境配置')
        raise
