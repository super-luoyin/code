# 登陆界面
from selenium.webdriver.common.by import By
from test_case_template.utils import DriverUtil
from time import sleep


class LoginPage(object):
    def __init__(self):
        self.web = DriverUtil.get_driver()  # 获取浏览器对象
        # 说明:将元素的定位方法及特征封装成属性，能够实现集中化管理目标元素的定位方法及特征值
        self.cik = (By.XPATH, "//*[@id='TANGRAM__PSP_11__changePwdCodeItem']")      # 选择账号登录
        self.name = (By.XPATH, "//*[@id='TANGRAM__PSP_11__userName' and @name='userName']")     # 用户名
        self.pwd = (By.XPATH, "//*[@id='TANGRAM__PSP_11__password' and @name='password']")      # 密码
        self.btn = (By.XPATH, "//*[@id='TANGRAM__PSP_11__submit' and @class='pass-button pass-button-submit']")  # 按钮

    def click_login(self):
        # return self.web.find_element(By.XPATH, "'TANGRAM__PSP_11__changePwdCodeItem']")
        return self.web.find_element(self.cik[0], self.cik[1])

    def find_username(self):
        """定位用户名方法"""
        # return self.web.find_element_by_xpath("//*[@id='TANGRAM__PSP_11__userName' and @name='userName']")
        return self.web.find_element(self.name[0], self.name[1])

    def find_password(self):
        """定位密码方法"""
        # return self.web.find_element_by_xpath("//*[@id='TANGRAM__PSP_11__password' and @name='password']")
        return self.web.find_element(self.pwd[0], self.pwd[1])

    def find_login_btn(self):
        """定位按钮方法"""
        # return self.web.find_element_by_xpath(
        #    "//*[@id='TANGRAM__PSP_11__submit' and @class='pass-button pass-button-submit']")
        return self.web.find_element(self.btn[0], self.btn[1])


class LoginHandle(object):
    """登录操作层"""
    def __init__(self):
        self.login_page = LoginPage()       # 获取对象层对象

    def input_click(self):
        """点击账号登录"""
        self.login_page.click_login().click()

    def input_username(self, name):
        """输入用户名方法"""
        # 说明:在执行输入操作前，应该先执行清空操作
        self.login_page.find_username().clear()
        self.login_page.find_username().send_keys(name)

    def input_password(self, pwd):
        """输入密码"""
        self.login_page.find_password().clear()
        self.login_page.find_password().send_keys(pwd)

    def input_login_btn(self):
        """点击登录按钮方法"""
        sleep(2)
        self.login_page.find_login_btn().click()


class LoginTask(object):
    """登录业务层"""
    def __init__(self):
        self.login_handle = LoginHandle()       # 获取操作层元素

    def login_method(self, name, pwd):
        self.login_handle.input_click()     # 点击账号登录
        self.login_handle.input_username(name)  # 输入用户名
        self.login_handle.input_password(pwd)   # 输入密码
        self.login_handle.input_login_btn()     # 点击按钮
