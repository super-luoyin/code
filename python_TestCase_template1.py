# 学习TestCase（测试用例）模块的书写方法
# 导包
import unittest


# 自定义测试类，需要继承unittest模块中的TestCase类即可
class TestDemo1(unittest.TestCase):
    # 书写测试方法，即用例代码(目前没有真正的测试代码，使用print代替)
    # 书写要求，测试方法，必须以test_开头（本质是以test开头）
    def test_method1(self):
        print("测试方法1")

    def test_method2(self):
        print("测试方法2")

# 执行用例（方法）
# 将光标放在 类名后面 运行，会执行类中的所有的测试方法
# 将光标放在 方法名的后面 运行，只执行当前的方法
