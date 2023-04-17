# 说明：下拉框就是HTML中<select>元素
# 传统方案
# 导入模块
from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains

# 实例化浏览器对象
web = webdriver.Chrome()
# 打开网页
web.get("http://baidu.com")
# 实现需求
# 使用鼠标悬停到设置上在菜单中选择高级搜索，完成对时间的下拉操作
web.maximize_window()
web1 = web.find_element_by_id("V5test_case_optimization-usersetting-top")
mouse = ActionChains(web)
mouse.move_to_element(web1)
mouse.perform()
# 点击高级搜索
web.find_elements_by_class_name("set")[1].click()
sleep(2)
# 下拉选项:选择最近一天
web.find_element_by_class_name('c-select-selected-value').click()
sleep(2)
web.find_elements_by_class_name("c-select-item")[2].click()
# 观察效果
sleep(3)
# 关闭网页
web.quit()
