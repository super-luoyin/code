# 元素操作方法
"""
click()             单击元素
send_keys(value)    模拟输入
clear()             清除文本
"""
# 导入模块
from time import sleep
from selenium import webdriver
# 实例化浏览器对象
web = webdriver.Chrome()
# 打开网页
web.get("http://baidu.com")
# 需求：在输入框中输入7k7k小游戏，间隔三秒，修改为4399小游戏，间隔三秒点击搜索按钮，间隔三秒关闭浏览器
# 输入
web1 = web.find_element_by_css_selector("#kw")
web1.send_keys("7k7k小游戏")
sleep(3)
# 注意：在使用操作中，一般对于输入元素都要先执行清空，在执行输入，避免操作错误
web1.clear()
web1.send_keys("4399小游戏")
# 间隔三秒按搜索按钮
sleep(3)
web.find_element_by_xpath("//*[@id='su']").click()
# 观察效果
sleep(3)
# 关闭网页
web.quit()
