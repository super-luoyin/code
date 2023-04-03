# 学习TestSuite测试套件的第二种书写方法
# 导包
import unittest

from unittest_frame_operation.python_TestCase_template import TestDemo
from unittest_frame_operation.python_TestCase_template1 import TestDemo1

# 实例化（创建对象）套件对象
suit = unittest.TestSuite()
# 添加套件对象
# 方法二，将一个测试类中的所有方法进行添加
# 套件对象.addTest(unittest.makeSuite(测试类名))
# 缺点:makeSuit（）不会提示
suit.addTest(unittest.makeSuite(TestDemo))
suit.addTest(unittest.makeSuite(TestDemo1))
# 实例化运行对象
runner = unittest.TextTestRunner()
# 使用运行对象去执行套件对象
runner.run(suit)
