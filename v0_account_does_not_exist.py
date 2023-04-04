"""账号不存在测试用例"""
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
# 2.输入一个不存在的用户名
# 选择账号登录
web.find_element_by_xpath("//*[@id='TANGRAM__PSP_11__changePwdCodeItem']").click()
web.find_element_by_xpath("//*[@id='TANGRAM__PSP_11__userName' and @name='userName']").send_keys("1738822yz")
# 3.输入密码
web.find_element_by_xpath("//*[@id='TANGRAM__PSP_11__password' and @name='password']").send_keys("123456")
# 4.点击登录按钮
sleep(4)
web.find_element_by_xpath("//*[@id='TANGRAM__PSP_11__submit' and @class='pass-button pass-button-submit']").click()
# 5.获取错误提示信息
sleep(3)
txt = web.find_element_by_xpath("//*[@id='TANGRAM__PSP_11__error' and @class='pass-generalError pass-generalError-error']").text
print(txt)
# 观察效果
sleep(3)
# 关闭浏览器
web.quit()
