# 元素属性定位
# 导入模块
from selenium import webdriver
from time import sleep
# 实例化浏览器对象
web = webdriver.Chrome()
# 打开网页
web.get("http://baidu.com")
# 利用元素属性策略: 该方法可以使用目标元素的任意一个属性和属性值（需要保证唯一性)
# 语法1: //标签名[@属性名=’属性值‘]
# 注意:与class_name 方法不同的是，如果使用具有多个值的class属性，则需要传入全部的属性值
web1 = web.find_element_by_xpath("//input[@id='kw']")
web1.send_keys("43")
sleep(2)
# 语法2: //*[@属性名=’属性值‘]
web2 = web.find_element_by_xpath("//*[@name='wd']")
web2.send_keys("99")
# 观察效果
sleep(3)
# 关闭网页
web.quit()
