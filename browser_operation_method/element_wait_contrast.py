# 隐式等待和显式等待的对比
"""
对比          元素个数        调用方式                异常类型
隐式等待        全局          浏览器对象的调用          NoSuchElementException
显式等待        单个          实例化对象调方法          TimeoutException
强制等待        全局          方法                    NoSuchElementException
"""