# 公共方法模块:习惯命名 utils
from selenium import webdriver
from time import sleep


class DriverUtil(object):    # 正常定义类，但是测试类名必须以Test开头
    """浏览器对象管理类"""
    # 说明:对象变量只需要在类定义内容使用，因此定义为私有
    __web = None      # 浏览器对象变量初始化状态

    @classmethod
    def get_driver(cls):
        """获取浏览器对象方法"""
        # 说明:为了防止在同一次测试过程中，调用获取浏览器对象方法时，
        # 都会创建一个新的浏览器对象，因此有必要先判断对象是否存在，不存在时在创建！
        if cls.__web is None:
            cls.__web = webdriver.Chrome()
            cls.__web.get("http://baidu.com")
            cls.__web.maximize_window()
            cls.__web.implicitly_wait(10)
        return cls.__web

    @classmethod
    def quit_driver(cls):
        """退出浏览器对象方法"""
        # 说明:必须保证浏览器对象存在，才能执行退出操作
        if cls.__web:    # 等价于: if self.web is not None:
            sleep(3)
            cls.__web.quit()
            cls.__web = None     # 保险手段:移除对象后，保留对象变量，以备下一次使用


if __name__ == '__main__':
    # my_web = DriverUtil()
    # my_web.get_driver()
    # my_web.quit_driver()
    DriverUtil.get_driver()
    DriverUtil.quit_driver()
