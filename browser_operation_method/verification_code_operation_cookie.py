# Selenium操作cookie
"""
说明: selenium中对cookie操作提供相应的方法
方法: 1.get_cookie(name)          -->获取指定cookie
name:为cookie的名称
     2.get_cookie()              -->获取本网站所有本地cookie
     3.add_cookie(cookie_dict)   -->添加cookie
            cookie_dict: 一个字典对象，必选的键包括："name"and"value"
"""
# 导入模块
from selenium import webdriver
from time import sleep
# 实例化浏览器对象
web = webdriver.Chrome()
# 打开网页
web.get("http://baidu.com")
# 窗口最大化
web.maximize_window()

# cookie绕过登录
# 1.整理关键cookie信息为字典数据
# 注意:字典数据的key必须是name和value！！！！！！！！！！！
cookie_value = {'name': 'BDUSS_BFESS','value': 'RSQ250V0M3YTNpcHV2V0lXS1ZPcmpaVzQ0ZWxOUmhGTWNZSWw2V1pIckFsbUJrRUFBQUFBJCQAAAAAAQAAAAEAAAA46nsN0sXN~LO-sKM1AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAJOWTACTlkRz'}
# 2.调用方法，添加cookie信息
web.add_cookie(cookie_value)
# 3.刷新页面->发送cookie信息给服务器进行验证！！！！！！！！！！！！！！！
web.refresh()
# 注意：
# 1.本地浏览器登录的账号，不能退出，否则cookie信息过期，需要重新获取
# 2. 不同项目的能够进行登录功能绕过的cookie字段信息都不相同，具体需要询问开发
# 3. 利用cookie绕过登录，则不能对登录功能本身进行测试
# 4.个别项目如果想要绕过登录，有可能需要添加多个cookie字段
# 展示效果
sleep(3)
# 退出浏览器
# web.quit()





