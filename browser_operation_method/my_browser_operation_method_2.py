# 浏览器操作常用的方法
# 导入模块
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# 实例化浏览器对象
web = webdriver.Chrome()
# 打开网页
web.get("http://baidu.com")
# 满足需求
web.find_element(By.ID, "kw").send_keys("4399小游戏")
web.find_element_by_id("su").click()
sleep(2)
# back()                          后退-->模拟浏览器后退按钮
web.back()
sleep(2)
# forward()                       前进-->模拟浏览器前进按钮
web.forward()
sleep(2)
# refresh()                       刷新-->模拟浏览器刷新
# 说明：刷新动作是重新向服务器发起当前页面的请求
web.refresh()
# 观察效果
sleep(3)
# 关闭网页
web.quit()
