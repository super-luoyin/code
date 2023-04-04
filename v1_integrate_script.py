"""
整合多个脚本至同一个测试用例中
"""
import pytest as pytest
from selenium import webdriver
from time import sleep


class TestLogin(object):    # 正常定义类，但是测试类名必须以Test开头
    """登陆测试"""
    def setup(self):
        self.web = webdriver.Chrome()
        self.web.get("http://baidu.com")
        self.web.maximize_window()
        self.web.implicitly_wait(10)

    def teardown(self):
        sleep(3)
        self.web.quit()

    def test_account_does_not_exist(self):      # 正常定于方法，但是测试方法名必须以test开头
        """账号不存在方法"""
        # web = webdriver.Chrome()
        # web.get("http://baidu.com")
        # web.maximize_window()
        # web.implicitly_wait(10)
        self.web.find_element_by_id("V5test_case_optimization-top-loginbtn").click()
        self.web.find_element_by_xpath("//*[@id='TANGRAM__PSP_11__changePwdCodeItem']").click()
        self.web.find_element_by_xpath("//*[@id='TANGRAM__PSP_11__userName' and @name='userName']").send_keys("123456")
        self.web.find_element_by_xpath("//*[@id='TANGRAM__PSP_11__password' and @name='password']").send_keys("123456")
        sleep(1)
        self.web.find_element_by_xpath(
            "//*[@id='TANGRAM__PSP_11__submit' and @class='pass-button pass-button-submit']").click()
        sleep(3)
        txt = self.web.find_element_by_xpath(
            "//*[@id='TANGRAM__PSP_11__error' and @class='pass-generalError pass-generalError-error']").text
        print(txt)
        # sleep(3)
        # web.quit()

    def test_wrong_password(self):
        """密码错误测试方法"""
        # web = webdriver.Chrome()
        # web.get("http://baidu.com")
        # web.maximize_window()
        # web.implicitly_wait(10)
        self.web.find_element_by_id("s-top-loginbtn").click()
        self.web.find_element_by_xpath("//*[@id='TANGRAM__PSP_11__changePwdCodeItem']").click()
        self.web.find_element_by_xpath("//*[@id='TANGRAM__PSP_11__userName' and @name='userName']").send_keys("17388220547")
        self.web.find_element_by_xpath("//*[@id='TANGRAM__PSP_11__password' and @name='password']").send_keys("123456")
        sleep(1)
        self.web.find_element_by_xpath(
            "//*[@id='TANGRAM__PSP_11__submit' and @class='pass-button pass-button-submit']").click()
        sleep(3)
        txt = self.web.find_element_by_xpath("//*[@class='mod-page-tipInfo-gray2']").text
        print(txt)
        # sleep(3)
        # web.quit()


if __name__ == '__main__':
    pytest.main(['-s', 'v1_integrate_script.py'])
