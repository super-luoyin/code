# tag_name定位就是通过标签名来定位
# 导入模块
from selenium import webdriver
from time import sleep
# 实例化浏览器对象
web = webdriver.Chrome()
# 打开网页
web.get("http://baidu.com")
# 实现效果
# web1 = web.find_element_by_tag_name("input")
# web1.send_keys("4399")
# 观察效果
sleep(3)
# 关闭网站
web.quit()
