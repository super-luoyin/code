# 1.导包
from time import sleep
from selenium import webdriver
# 2.实例化浏览器对象
web = webdriver.Chrome()
# 3.打开网页：必须包含协议头
web.get('http://www.baidu.com')
# 实现需求
web1 = web.find_element_by_id("kw")
web1.send_keys('4399')
# 4.观察效果
sleep(3)
# 5.关闭网页
web.quit()