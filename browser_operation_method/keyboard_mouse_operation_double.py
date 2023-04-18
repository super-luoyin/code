# 鼠标双击操作
# 导入模块
from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains

# 实例化浏览器对象
web = webdriver.Chrome()
# 打开网页
web.get("http://baidu.com")
# 实现需求
web1 = web.find_element_by_id("kw")
web1.send_keys("4399")
sleep(3)
# 说明：使用快捷键ctl + A，也能实现全选
# 实例化鼠标对象
mouse = ActionChains(web)
# 调用鼠标动作
mouse.double_click(web1)
# 执行方法
mouse.perform()
# 观察效果
sleep(3)
# 关闭网页
web.quit()
