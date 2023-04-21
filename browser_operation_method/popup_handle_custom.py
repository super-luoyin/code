# 弹出框处理（自定义弹出框处理）
# 自定义弹窗
# 说明: 由于自定义弹窗可以通过鼠标右键的检查选项获取元素信息，因此出现自定义弹窗时，直接定义目标元素并操作，移除弹窗即可
# 导入模块
from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains

# 实例化浏览器对象
web = webdriver.Chrome()
# 打开网页
web.get("http://baidu.com")
# 实现需求
web.maximize_window()
# 点击设置
# 定义目标对象
web1 = web.find_element_by_id('s-usersetting-top')
mouse = ActionChains(web)
mouse.move_to_element(web1)
mouse.perform()
web.find_elements_by_class_name("set")[0].click()
sleep(3)
# 关闭弹窗
web.find_element_by_class_name("c-icon s-skin-close").click()
# 观察效果
sleep(3)
# 关闭网页
web.quit()
