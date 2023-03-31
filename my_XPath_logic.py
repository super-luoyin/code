# 属性和逻辑结合定位
# 导入模块
from selenium import webdriver
from time import sleep
# 实例化浏览器对象
web = webdriver.Chrome()
# 打开网页
web.get("http://baidu.com")
# 属性和逻辑结合: 解决目标元素单个属性和属性值无法定位为一个元素的问题时使用
# 语法: //*[@属性1=’属性值1‘ and @属性2=’属性值2‘]
# 注意: 多个属性值由 and 连接， 每个属性都要以@开头，可以根据需求使用更多的属性值
web1 = web.find_element_by_xpath("//*[@class='s_ipt' and @name='wd']")
web1.send_keys("4399")
# 观察效果
sleep(3)
# 关闭网页
web.quit()
