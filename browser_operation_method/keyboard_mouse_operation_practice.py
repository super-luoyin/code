# 鼠标练习操作
# 导入模块
from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains

# 实例化浏览器对象
web = webdriver.Chrome()
# 打开网页
web.get("http://baidu.com")
# 实现需求
# 百度网页里面悬停鼠标到设置，进入设置菜单里面的搜索设置，把每页十条改为每页五十条
web.maximize_window()
# 定位目标元素
move = web.find_element_by_id("V5test_case_optimization-usersetting-top")
# 实例化鼠标方法
mouse = ActionChains(web)
# 调用方法
mouse.move_to_element(move)
mouse.perform()
sleep(2)
dianji = web.find_element_by_xpath("//div//a[@class='setpref first']//*[@class='set']")
mouse.double_click(dianji)
mouse.perform()
sleep(2)
xuanzhong1 = web.find_element_by_xpath("//span[@id='se-setting-3']//span[@class='setting-radio-wrap search-radio-wrap']//*[@class='setting-radio-label']")
xuanzhong1.click()
# 观察效果
sleep(3)
# 关闭网页
web.quit()
