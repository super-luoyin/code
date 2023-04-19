# 鼠标的悬停操作
# 导入模块
from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains

# 实例化浏览器对象
web = webdriver.Chrome()
# 打开页面
web.get("http://baidu.com")
# 实现效果
# 定位目标元素
web1 = web.find_element_by_id("V5test_case_optimization-usersetting-top")
# 实例化鼠标对象
mouse = ActionChains(web)
# 调用鼠标方法
# 说明：该方法在实际应用中，处理悬停鼠标次才会出现的菜单时使用
# 注意：该方法执行时，不要动鼠标！！！！
mouse.move_to_element(web1)
# 执行方法
mouse.perform()

# 另一种鼠标操作的写法：（在其他编程语言中称为链式编程）
# ActionChains(web).move_to_element(web1).perform()

# 观察效果
sleep(3)
# 关闭网页
web.quit()