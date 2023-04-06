# 导入模块
from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains
# 实力化浏览器对象
web = webdriver.Chrome()
web.maximize_window()
web.implicitly_wait(10)
# 打开网页
web.get("http://www.cqsxedu.com")
# 实例化鼠标对象
mouse = ActionChains(web)
# 定位目标元素
web1 = web.find_element_by_link_text("公共服务")
# 调用鼠标方法
mouse.move_to_element(web1)
# 执行方法
mouse.perform()
# 点击网上大厅
web.find_element_by_link_text("网上大厅").click()
# 窗口的切换
handles = web.window_handles
web.switch_to.window(handles[-1])
# 点击登录
web.find_element_by_id("ampLoginBtn").click()
# 登录账号
web.find_element_by_xpath("//*[@id='username' and @name='username']").send_keys("202122251396")
web.find_element_by_xpath("//*[@id='password' and @class='auth_input']").send_keys("121380ld")
web.find_element_by_xpath("//*[@class='auth_login_btn primary full_width']").click()
# cookie_value = {"name": "MOD_AUTH_CAS", "value": "MOD_AUTH_ST-329493-OpOg3wQiuCSoniR1IoNJ1676871890679-5X6Q-cas"}
# web.add_cookie(cookie_value)
# web.refresh()
# 观察效果
sleep(3)
# 关闭网页
web.quit()
