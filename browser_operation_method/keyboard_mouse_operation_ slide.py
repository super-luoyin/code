# 滑块操作
# 导入模块
from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains
# 实例化浏览器对象
web = webdriver.Chrome()
# 打开浏览器
web.get("http://baidu.com")
web.maximize_window()
web.implicitly_wait(10)
mouse = ActionChains(web)
web.find_element_by_id("s-top-loginbtn").click()
web.find_element_by_id("TANGRAM__PSP_11__changePwdCodeItem").click()
web.find_element_by_xpath("//*[@id='TANGRAM__PSP_11__userName' and @name='userName']").send_keys("123456")
web.find_element_by_xpath("//*[@id='TANGRAM__PSP_11__password' and @name='password']").send_keys("123456")
web.find_element_by_id("TANGRAM__PSP_11__submit").click()
# 定位滑块
a = web.find_element_by_xpath("/html/body/div[10]/div[1]/div/div[2]/div[2]/p")
# 长按滑块
mouse.click_and_hold(a)
mouse.perform()
# 滑动长度
mouse.move_by_offset(150, 0)
mouse.perform()
# 释放
mouse.release()
mouse.perform()
# 观察效果
sleep(3)
# 关闭浏览器
web.quit()