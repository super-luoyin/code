"""
Select类
说明：select类是selenium为操作select标签特殊封装的
实例化对象
select = Select(element)
element: <select>标签对应的元素，通过元素定位方式获取
例如：web.find_element_by_id("kw")
操作方法：
select_by_index(index)              -->根据option索引来定位，从0开始
select_by_value(value)              -->根据option属性 value值来定位
select_by_visible_text(text)        -->根据option显示文本来定位
Select类实现步骤分析
1.导包Select类 --> from selenium.webdriver.support.select import Select
2.实例化Select类 select = Select(web.find_element_by_id("kw"))
3.调用方法：select.select_by_index(index)
"""
# 导入模块
from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

# 实例化浏览器对象
web = webdriver.Chrome()
# 打开网页：必须包含协议头
web.get("http://baidu.com")
# 实现需求
# 使用鼠标悬停到设置上在菜单中选择高级搜索，完成对时间的下拉操作
web.maximize_window()
web1 = web.find_element_by_id("s-usersetting-top")
mouse = ActionChains(web)
mouse.move_to_element(web1)
mouse.perform()
# 点击高级搜索
web.find_elements_by_class_name("set")[1].click()
# sleep(2)
# # 定位下拉框元素
# sel = web.find_element_by_class_name("c-select-selected-value")
# # 实例化下拉框选择对象
# se = Select(sel)
# # 通过索引选择目标元素
# se.select_by_index(2)
# sleep(2)
# se.select_by_value("kw")
# sleep(2)
# se.select_by_visible_text("百度")
# 观察效果
sleep(3)
# 关闭网页
web.quit()
