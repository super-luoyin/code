# 密码错误面试用例
# 导入模块
from selenium import webdriver
from time import sleep
# 实例化浏览器对象
web = webdriver.Chrome()
# 打开网页
web.get("http://baidu.com")
web.maximize_window()
web.implicitly_wait(10)
# 实现效果
# 1.点击页面的“登录”按钮，进入登录界面
web.find_element_by_id("s-top-loginbtn").click()
# 2.输入一个存在的用户名
# 选择账号登录
web.find_element_by_xpath("//*[@id='TANGRAM__PSP_11__changePwdCodeItem']").click()
web.find_element_by_xpath("//*[@id='TANGRAM__PSP_11__userName' and @name='userName']").send_keys("17388220547")
# 3.输入错误密码
web.find_element_by_xpath("//*[@id='TANGRAM__PSP_11__password' and @name='password']").send_keys("123456")
# 4.点击登录按钮
sleep(1)
web.find_element_by_xpath("//*[@id='TANGRAM__PSP_11__submit' and @class='pass-button pass-button-submit']").click()
# 5.获取错误提示信息
sleep(3)
txt = web.find_element_by_xpath("//*[@class='mod-page-tipInfo-gray2']").text
print(txt)
# 观察效果
sleep(3)
# 关闭网页
web.quit()
