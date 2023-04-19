# 键盘操作
"""
selenium中把键盘的按键都封装在Keys类中
ctrl键再选中Keys可以查看所有的按键
常用按键操作
send_keys(Keys.BACK_SPACE)      删除键（BackSpace）
send_keys(Keys.SPACE)           空格键（Space）
send_keys(Keys.TAB)             制表键（Tab）
send_keys(Keys.ESCAPE)          回退键（Esc）
send_keys(Keys.ENTER)           回车键（Enter）
send_keys(Keys.CONTROL, 'a')    全选（Ctrl+A）
send_keys(Keys.CONTROL, 'c')    复制（Ctrl+C）
"""
# 导入模块
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 实例化浏览器对象
web = webdriver.Chrome()
# 打开网页
web.get("http://baidu.com")
# 实现需求
# 输入4399，暂停两秒
web1 = web.find_element_by_id("kw")
web1.send_keys("4399")
sleep(2)
# 全选4399，暂停两秒
web1.send_keys(Keys.CONTROL, 'a')
sleep(2)
# 复制4399，并删除，暂停两秒
web1.send_keys(Keys.CONTROL, 'c')
web1.send_keys(Keys.BACK_SPACE)
sleep(2)
# 在粘贴回来
web1.send_keys(Keys.CONTROL, 'v')
# 观察效果
sleep(3)
# 关闭网页
web.quit()
