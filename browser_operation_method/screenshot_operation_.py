# 窗口截图
# 说明:把当前操作的页面，截图保存到指定位置
"""
原因:自动化本是由程序去执行的，因此有时候打印的错误信息并不是十分确定，如果在执行出错的时候对当前窗口截图保存，那么通过图片就是可以非常直观地看到出错的原因
应用场景:在自动化测试中，出现错误时，可以通过截图，辅助判定错误原因
说明:在Selenium中，提供了截图方法，我们只需要调用即可
方法:web.get_screenshot_as_file(imgpath)      imgpath:图片保存路径
"""
# 导入模块
from time import sleep, strftime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# 实例化浏览器对象
# web = webdriver.Chrome()
# 打开网页
# web.get("http://baidu.com")
# 实施效果
# web.find_element_by_id("kw").send_keys("4399")
# 截图保存 默认推荐使用.png格式
# web.get_screenshot_as_file('./info.png')
# 说明: jpg虽然可以使用，但是会有使用警告
# web.get_screenshot_as_file('./info.jpg')
# 扩展:指定图片存放路径: 需要手动创造文件夹!!!!!!!!!!!!!!!!
# web.get_screenshot_as_file('./image/tp1.png')
# 扩展:使用时间戳防止文件重名被覆盖
# 说明：Windows 系统文件名不支持特殊符号，尽量只是用下划线
# 如果忘记就按住ctrl点击strftime
# now_time = strftime('%Y%m%d_%H%M%S')
# web.get_screenshot_as_file('./image/tp_{}.png'.format(now_time))
# 扩展:给元素截图
# btn = web.find_element_by_tag_name('tj_login')
# btn.screenshot('./btn.png')
# 扩展长截图
# width = web.execute_script('return document.documentElement.scrollWidth')
# height = web.execute_script('return document.documentElement.scrollWidth')
# web.set_window_size(width, height)
# sleep(1)
# web.save_screenshot('./image/chang.png')
# # 观察效果
# 长截图
web_1 = Options()
web_1.add_argument("headless")
web = webdriver.Chrome(options=web_1)
web.get("http://www.cqzwy203.info:28080/LexianMall/sc/index.html")
width = web.execute_script('return document.documentElement.scrollWidth')
height = web.execute_script('return document.documentElement.scrollHeight')
web.set_window_size(width, height)
sleep(1)
# 截图
web.save_screenshot('ex1.png')
sleep(3)
# 关闭网页
web.quit()
