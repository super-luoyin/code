# 首页页面
from test_case_template.utils import DriverUtil


class IndexPage(object):
    """首页对象层"""

    def __init__(self):
        self.web = DriverUtil.get_driver()      # 获取浏览器对象

    def find_login(self):
        return self.web.find_element_by_id("s-top-loginbtn")


class IndexHandle(object):
    """首页操作层"""
    def __init__(self):
        self.index_page = IndexPage()       # 获取对象层对象

    def click_login(self):
        """点击登录方法"""
        self.index_page.find_login().click()


class IndexTask(object):
    """首页业务层"""
    def __init__(self):
        self.index_handle = IndexHandle()       # 获取操作层对象

    def go_to_login(self):
        # 跳转登录页面方法
        self.index_handle.click_login()




