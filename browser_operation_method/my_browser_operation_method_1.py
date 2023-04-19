# 浏览器操作常用的方法
# 通过条用Selenium的APL来实现浏览器的操作
"""
maximize_window()               最大化浏览器窗口-->模拟浏览器最大化按钮
set_window_size(width,height)   设置浏览器窗口大小-->设置浏览器宽，高（像素大小）
set_window_position(x,y)        设置浏览器窗口位置-->设置浏览器位置
back()                          后退-->模拟浏览器后退按钮
forward()                       前进-->模拟浏览器前进按钮
refresh()                       刷新-->模拟浏览器刷新
close()                         关闭当前窗口-->模拟点击浏览器关闭按钮
quit()                          关闭浏览器驱动程序-->关闭所有程序启动的窗口
title                           获取页面title
current_url                     获取当前页面URL
"""
# 导入模块
from time import sleep
from selenium import webdriver
# 实例化浏览器对象
web = webdriver.Chrome()
# 打开网页
web.get("http://baidu.com")
# 1.maximize_window()               最大化浏览器窗口-->模拟浏览器最大化按钮
# 说明：如果能够再打开页面时，全屏显示页面，就是尽最大可能加载更多的页面元素，提高可定位性
web.maximize_window()
sleep(2)
# 2.set_window_size(width,height)   设置浏览器窗口大小-->设置浏览器宽，高（像素大小）
# 场景：查看页面是否可以自适应（Web 和 App端切换）时使用
web.set_window_size(500, 500)
sleep(2)
# 3.set_window_position(x,y)        设置浏览器窗口位置-->设置浏览器位置
# Web/App项目页面布局都是以屏幕的左上角作为坐标原点（0，0）
web.set_window_position(300, 300)
# 观察效果
sleep(3)
# 关闭网页
web.quit()
