# frame切换
"""
frame: HTML页面中的一种框架，主要作用是在当前页面中指定区域显示另一页面元素
frame切换方法
说明：在selenium中封装了如何切换frame框架的方法
方法：
1.web.switch_to.frame(frame_reference)      -->切换到指定frame的方法
frame_reference: 可以为frame框架的name、id或者定位到的frame元素
2.web.switch_to.default_content()           -->恢复默认页面方法
注意：如果元素可以获取，但是代码执行无法定位，则需要手动从目标元素对应的代码开始向上查找，是否存在iframe标签
"""
# 导入模块
from time import sleep
from selenium import webdriver
# 实例化浏览器对象
web = webdriver.Chrome()
# 打开网页
web.get("http://baidu.com")
# 说明：如果目标元素存在于frame中，就需要先执行切换frame操作，在定位元素
# 切换frame： 传入的是能够代表 frame 元素唯一的特征值
"""
web.switch_to.frame("element")
web.find_element_by_id('id').send_keys('lala')
web.find_element_by_id('id2').send_keys('haha')
"""
# frame 切换到 frame       注意：frame不能直接切换到frame！！！！！！！！！！！！！
# 第一步 切换回默认页面，如果连续切换多个frame，必须先回到默认页面，才能实现切换下一个frame!!!!!!!!!!!!
web.switch_to.default_content()
# 第二步 切换frame       按住ctrl键点击frame查看更多使用方法
web.switch_to.frame("element")
web.find_element_by_id('id').send_keys('lala')
web.find_element_by_id('id').send_keys('haha')
# 观察效果
sleep(3)
# 关闭网页
web.quit()
