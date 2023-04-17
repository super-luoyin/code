# 元素的显式等待
# 概念；定位指定元素式，如果能定位到元素则直接返回该元素，不促发等待；如果不能定位到该元素，则间隔一段时间后再去定位元素，如果在达到最大时长还是没有找到指定元素，则抛出异常
"""
实现方法
导包，等待类-->from selenium.webdriver.support.wait import WebDriverWait
WebDriverWait(driver, timeout, poll_frequency=0.5)
1.driver: 浏览器驱动对象
2.timeout: 超时的时长，单位：秒
3.poll_frequency: 检测间隔时间，默认为0.5秒
调用方法 until(method): 直到……时
1.method：函数名称，该函数用来实现对元素的定位
2.一般用匿名函数来实现：lambda x: x.find_element_by_id("kw")
element = WebDriverWait(driver, 10, 1).until(lambda x: x.find_element_by_id("kw"))
"""
# 导入模块
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

# 实例化浏览器对象
web = webdriver.Chrome()
# 打开网页
web.get("http://baidu.com")
# 实现效果
# 使用显式等待定位浏览器输入框， 如果元素存在，就输入4399
# web.find_element_by_id("kw").send_keys("4399")
# 设置元素等待
"""
driver:             浏览器对象
timeout:            超时时长
poll_frequency:     定位方法执行时间间隔时长（默认0.5秒）
"""
web_wait = WebDriverWait(web, 10, 1).until(lambda x: x.find_element_by_id("kw"))
# 说明：元素操作方法没有代码提示，需要手写（把WebDriverWait写出来按住ctrl点击名字，找到直接复制）
web_wait.send_keys("4399")
# 观察效果
sleep(3)
# 关闭网页
web.quit()
