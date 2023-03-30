# 导入模块
from selenium import webdriver
from time import sleep
# 实例化浏览器对象
web = webdriver.Chrome()
# 打开网页
web.get("http://baidu.com")
# 实现效果
# 注意
# 如果元素的 class 属性值存在多个值，只能使用其中的任意一个！！！！！！！！！！！！！！！！！！！！
web1 = web.find_element_by_class_name("s_ipt")
web1.send_keys('4399')
# 观察效果
sleep(3)
# 关闭网页
web.quit()
