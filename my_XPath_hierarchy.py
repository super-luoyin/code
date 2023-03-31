# 层级与属性结合定位
# 导入模块
from selenium import webdriver
from time import sleep
# 实例化浏览器对象
web = webdriver.Chrome()
# 打开网页
web.get("http://baidu.com")
# 层级与属性结合: 目标元素无法直接定位，可以考虑先定位其父层级或者祖辈层级，在获取目标元素
# 使用场景: 同一件商品不同位置
# 语法: 父层级定位策略/目标元素定位策略
# web1 = web.find_element_by_xpath("//form[@id='form']/span[1]/input")
web1 = web.find_element_by_xpath("//form//span//*[@id='kw']")
web1.send_keys("4399")
# 观察效果
sleep(3)
# 关闭网页
web.quit()
