# 路径定位
# 导入模块
from selenium import webdriver
from time import sleep
# 实例化浏览器对象
web = webdriver.Chrome()
# 打开网页
web.get("http://baidu.com")
# 绝对路径: 从最外层元素到指定元素之间所有经过元素层级的路径  绝对路径以/html根节点开始，使用/来分隔元素层级
web1 = web.find_element_by_xpath("/html/body/div[1]/div[1]/div[5]/div/div/form/span[1]/input")
web1.send_keys("43")
sleep(2)
# 相对路径: 匹配任意层级的元素，不限制元素的位置  相对路径以//开始
# 注意: 使用相对路径时，需要注意方法参数的内外号嵌套问题
web2 = web.find_element_by_xpath('//*[@id="kw"]')
web2.send_keys("99")
# 观察效果
sleep(3)
# 关闭网页
web.quit()
