# 获取元素信息的常用方法
# 导入模块
from time import sleep
from selenium import webdriver
# 实例化浏览器对象
web = webdriver.Chrome()
# 打开网页
web.get("http://baidu.com")
# 显示效果
# is_displayed()          判断元素是否可见
# 说明：该方法多用于对元素再页面内显示效果判断时使用（元素不显示不意味着一定无法定位）
span = web.find_element_by_id("kw")
print('目标元素是否显示：', span.is_displayed())
# is_enabled()            判断元素是否可用
# 说明：该方法多用于判断目标是否可以进行交互时使用
can_btn = web.find_element_by_id("su")
print('目标元素是否可用：', can_btn.is_enabled())
# is_selected()           判断元素是否被选中，用来检查复选框或者单选框按钮是否被选中
# 场景：如购物车页面，不全选商品，不让结算
check = web.find_element_by_id("kw")
print('目标元素是否被选中：', check.is_selected())
# 扩展：判断条件
# 选中的判断
if check.is_selected():
    pass
# 未选中的判断
if not check.is_selected():
    pass
# 观察效果
sleep(3)
# 关闭网页
web.quit()
