"""
整合多个脚本至同一个测试用例中
"""
import pytest as pytest
from selenium import webdriver
from time import sleep

from test_case_template.utils import DriverUtil, get_alert_msg


class TestLogin(object):    # 正常定义类，但是测试类名必须以Test开头
    """登陆测试"""

    def setup_class(self):
        self.web = DriverUtil.get_driver()      # 获取浏览器对象

    def teardown_class(self):
        DriverUtil.quit_driver()        # 退出浏览器对象

    def setup(self):
        # 1.打开首页
        self.web.get("http://baidu.com")
        # 2.点击登录
        self.web.find_element_by_id("s-top-loginbtn").click()

    def teardown(self):
        pass

    def test_account_does_not_exist(self):      # 正常定于方法，但是测试方法名必须以test开头
        """账号不存在方法"""
        self.web.find_element_by_xpath("//*[@id='TANGRAM__PSP_11__changePwdCodeItem']").click()
        self.web.find_element_by_xpath("//*[@id='TANGRAM__PSP_11__userName' and @name='userName']").send_keys("123456")
        self.web.find_element_by_xpath("//*[@id='TANGRAM__PSP_11__password' and @name='password']").send_keys("123456")
        sleep(1)
        self.web.find_element_by_xpath(
            "//*[@id='TANGRAM__PSP_11__submit' and @class='pass-button pass-button-submit']").click()
        txt = get_alert_msg()
        print(txt)

    def test_wrong_password(self):
        """密码错误测试方法"""
        self.web.find_element_by_xpath("//*[@id='TANGRAM__PSP_11__changePwdCodeItem']").click()
        self.web.find_element_by_xpath(
            "//*[@id='TANGRAM__PSP_11__userName' and @name='userName']").send_keys("17388220547")
        self.web.find_element_by_xpath("//*[@id='TANGRAM__PSP_11__password' and @name='password']").send_keys("123456")
        sleep(1)
        self.web.find_element_by_xpath(
            "//*[@id='TANGRAM__PSP_11__submit' and @class='pass-button pass-button-submit']").click()
        txt = get_alert_msg()
        print(txt)


if __name__ == '__main__':
    pytest.main(['-s', 'v3_encapsulation_script.py'])
