# 弹出框处理（系统弹出框处理）
# 应用场景: 页面操作过程中，一旦出现弹窗，如果不进行处理，则后续操作无法执行
# 弹窗分类: 1.系统弹窗（js实现） 2.自定义弹窗（前端代码封装）
"""
弹出框处理
1.alert         警告框
2.confirm       确认框
3.prompt        提示框
说明: Selenium中对处理弹出框的操作，有专业的处理方法，并且处理的方法都一样
获取弹出框对象
alert = driver.switch_to.alert
调用
alert.text          -->返回alert/confirm/prompt中的文字信息
alert.accept()      -->接受对话框选项
alert.dismiss()     -->取消对话框选项
"""
# 导入模块
from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains

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
# 点击搜索设置
web.find_elements_by_class_name("set")[0].click()
sleep(3)
# link = web.find_element_by_link_text('设置').click()
# web.find_element_by_link_text('搜索设置').click()
# 点击保存设置
# 注意: 凡是通过JS实现的系统弹窗，无法通过鼠标右键检查选项获取元素信息！！！！
web.find_element_by_class_name("prefpanelgo").click()
# 切换到弹窗: 只要是系统弹窗，无论哪一种，处理方式都是以下的步骤！！！！
# web.switch_to_alert()         #调用的方法上面如果存在黑线，意为该方法已经过期，将来会被移除，不推荐使用
alert = web.switch_to.alert
# 获取弹窗信息（可选）:获取弹窗信息必须在处理弹窗操作之前！！！
print("弹窗信息:", alert.text)
sleep(2)
# 去除弹窗（同意或者移除）
# alert.accept()      # 同意
alert.dismiss()       # 移除
# 观察效果
sleep(3)
# 关闭网页
web.quit()
