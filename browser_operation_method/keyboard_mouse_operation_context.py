# 鼠标操作的方法
"""
说明：在Selenium中将操作鼠标的方法封装在ActionChains类中
实例化对象
mouse = ActionChains(web)
方法
context_click(element)          右击-->模拟鼠标右键点击效果
double_click(element)           双击-->模拟鼠标双击效果
drag_and_drop(source,target)    拖动-->模拟鼠标拖动效果
move_to_element(element)        悬停-->模拟鼠标悬停效果
perform()                       执行-->此方法用来执行以上所有鼠标操作
"""
# 导入模块
from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains

# 实例化浏览器对象
web = webdriver.Chrome()
# 打开网页
web.get("http://baidu.com")
# 实现需求
# 定位目标元素
web1 = web.find_element_by_id("kw")
# 实例化鼠标对象
mouse = ActionChains(web)
# 调用鼠标方法
# 说明：鼠标右键只能展示右键菜单内容，而菜单中的元素无法操作！
mouse.context_click(web1)
# 执行方法：该方法必须调用，否则上述代码无效！！！！！
mouse.perform()
# 观察效果
sleep(3)
# 关闭网页
web.quit()
