# 鼠标拖拽操作
"""
源元素     source = web.find_element_by_id("xxx")
目标地址    target = web.find_element_by_id("xxx")
调用方法    mouse.drag_and_drop(source, target)
"""
# 导入模块
from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains

# 实例化浏览器对象
web = webdriver.Chrome()
# 打开网页
web.get("http://baidu.com")
# 实现效果
source = web.find_element_by_xpath("//div//div//*[@class='c-icon']")
target = web.find_element_by_id("kw")
# 实例化鼠标对象
mouse = ActionChains(web)
# 调用方法
mouse.drag_and_drop(source, target)
# 执行方法
mouse.perform()
# 观察效果
sleep(3)
# 关闭网页
web.quit()
