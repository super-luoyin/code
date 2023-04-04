# 公共方法模块
from selenium import webdriver
from time import sleep


def get_alert_msg():
    """获取弹窗的方法"""
    sleep(3)
    msg = DriverUtil.get_driver().find_element_by_xpath("//*[@class='mod-page-tipInfo-gray2']").text
    return msg


class DriverUtil(object):
    """浏览器对象管理类"""
    __web = None      # 浏览器对象变量初始化状态

    @classmethod
    def get_driver(cls):
        """获取浏览器对象方法"""
        if cls.__web is None:
            cls.__web = webdriver.Chrome()
            cls.__web.get("http://baidu.com")
            cls.__web.maximize_window()
            cls.__web.implicitly_wait(10)
        return cls.__web

    @classmethod
    def quit_driver(cls):
        """退出浏览器对象方法"""
        if cls.__web:    # 等价于: if self.web is not None:
            sleep(3)
            cls.__web.quit()
            cls.__web = None     # 保险手段:移除对象后，保留对象变量，以备下一次使用


if __name__ == '__main__':
    DriverUtil.get_driver()
    DriverUtil.quit_driver()
