# 滚动条操作
# 在HTML页面中，由于前端技术框架的原因，页面元素为动态显示，元素根据滚动条的下拉而被加载
# 页面注册同意条款，需要滚动条到最底层，才能点击同意
"""
实现方式
说明：selenium中并没有直接提供操作滚动条的方法，但是他提供了可执行javaScript脚本的方法，所以我们可以通过javaScript脚本来达到滚动条的目的
1.设置JavaScript脚本控制滚动条
js = "window.scrollTo(0,10000)"
(0:左边距；10000:上边距：单位像素）
2.selenium调用执行JavaScript脚本的方法
web.execute_script(js)
"""
# 导入模块
from time import sleep
from selenium import webdriver
# 实例化浏览器对象
web = webdriver.Chrome()
# 打开网页
web.get("http://taobao.com")
sleep(2)
# 实现效果
# 第一步准备js代码：    1000只是一个尽可能大的值，不是准确值
js_down = "window.scrollTo(0,1000)"
# 第二步执行js代码
web.execute_script(js_down)
sleep(2)
# 向上
js_up = "window.scrollTo(0,0)"
web.execute_script(js_up)
# 观察效果
sleep(3)
# 关闭网页
web.quit()
