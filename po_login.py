# 登陆界面
from test_case_template.utils import DriverUtil


class LoginPage(object):
    def __init__(self):
        self.web = DriverUtil.get_driver()  # 获取浏览器对象

    def click_login(self):
        return self.web.find_element_by_xpath("//*[@id='TANGRAM__PSP_11__changePwdCodeItem']")

    def find_username(self):
        """定位用户名方法"""
        return self.web.find_element_by_xpath("//*[@id='TANGRAM__PSP_11__userName' and @name='userName']")

    def find_password(self):
        """定位密码方法"""
        return self.web.find_element_by_xpath("//*[@id='TANGRAM__PSP_11__password' and @name='password']")

    def find_login_btn(self):
        """定位按钮方法"""
        return self.web.find_element_by_xpath(
            "//*[@id='TANGRAM__PSP_11__submit' and @class='pass-button pass-button-submit']")


class LoginHandle(object):
    """登录操作层"""
    def __init__(self):
        self.login_page = LoginPage()       # 获取对象层对象

    def input_click(self):
        """点击账号登录"""
        self.login_page.click_login().click()

    def input_username(self, name):
        """输入用户名方法"""
        self.login_page.find_username().send_keys(name)

    def input_password(self, pwd):
        """输入密码"""
        self.login_page.find_password().send_keys(pwd)

    def input_login_btn(self):
        """点击登录按钮方法"""
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
