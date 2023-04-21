# 浏览器操作常用的方法
# 导入模块
from time import sleep
from selenium import webdriver
# 实例化浏览器
web = webdriver.Chrome()
# 打开网页
web.get("http://baidu.com")
# 实现需求
web.find_element_by_id("kw").send_keys("4399")
web.find_element_by_id("su").click()
# title 获取页面title current_url    获取当前页面URL
# 场景：浏览器的标题和URL地址属性，可以用来断言
print("关闭前页面:", web.title)
print("关闭前地址:", web.current_url)
# close()                         关闭当前窗口-->模拟点击浏览器关闭按钮
# 说明：在没有实现浏览器页面切换操作之前，close（）方法关闭的是原始页面
# 场景：关闭单个页面时使用
web.close()
# 观察效果
sleep(3)
# 关闭网页
# quit()                          关闭浏览器驱动程序-->关闭所有程序启动的窗口
web.quit()
