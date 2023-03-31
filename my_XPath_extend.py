# XPath的延伸
# 导入模块
from selenium import webdriver
from time import sleep
# 实例化浏览器对象
web = webdriver.Chrome()
# 打开网页
web.get("http://baidu.com")
# XPath的延伸
# //*[text()="xxx"] 文本内容是xxx的元素
# //*[text()="文本信息"] 通过文本信息定位目标元素（要求全部文本内容）
# web1 = web.find_element_by_xpath("//*[text()='新闻']")
# web1.click()
# //*[contains(@attribute,'xxx')] 属性中含有xxx的元素
# //*[contains(@属性名，‘属性值的部分内容’)] : 通过给定属性值的部分内容进行元素定位
# web2 = web.find_element_by_xpath("//*[contains(@id,'k')]")
# web2.send_keys("4399")
# //*[starts-with(@attribute,'xxx')] 属性以xxx开头的元素
# //*[starts-with(@属性名，‘属性值的开头部分内容’)] : 通过给定属性值的开头部分内容进行元素定位
web3 = web.find_element_by_xpath("//*[starts-with(@class,'s_i')]")
web3.send_keys("4399")
# 观察效果
sleep(3)
# 关闭网页
web.quit()
