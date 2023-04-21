# 获取元素信息的常用方法
"""
size                    返回元素大小
text                    获取元素的文本
get_attribute("xxx")    获取属性值，传递的参数为元素的属性名
is_displayed()          判断元素是否可见
is_enabled()            判断元素是否可用
is_selected()           判断元素是否被选中，用来检查复选框或者单选框按钮是否被选中
1.size，text： 为属性，调用时没有括号
2.带括号的为方法
"""
# 导入模块
from time import sleep
from selenium import webdriver
# 实例化浏览器对象
web = webdriver.Chrome()
# 打开网页
web.get("http://baidu.com")
# 实现效果
# size 返回元素大小
# 场景: 用于判断页面元素布局尺寸是否合理时使用
username = web.find_element_by_id("kw")
print('目标元素的尺寸为：', username.size)
# text 获取元素的文本
# 场景: 用于切换页面后，对页面内容特定元素的文本信息的获取（用作断言使用）
btn = web.find_element_by_tag_name("input")
print('目标元素的文本为：', btn.text)
# get_attribute("xxx")    获取属性值，传递的参数为元素的属性名
# 场景：有些情况下，需要获取目标元素的特定属性值作为判断依据或数据
# 语法：元素对象.get_attribute("属性名")
like = web.find_element_by_link_text("新闻")
print('目标元素的地址为：', like.get_attribute('href'))
# 观察效果
sleep(3)
# 关闭网页
web.quit()
