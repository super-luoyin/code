# 学习TestSuite测试套件的第一种书写方法
# 导包（unittest）
import unittest

from unittest_frame_operation.python_TestCase_template import TestDemo
from unittest_frame_operation.python_TestCase_template1 import TestDemo1

# 实例化（创建对象）套件对象
suit = unittest.TestSuite()
# 使用套件对象添加用例对象
# 方法一,套件对象.addTest（测试类名（‘方法名’））     建议方法名直接去复制，不要手写
suit.addTest(TestDemo('test_method1'))
suit.addTest(TestDemo('test_method2'))
suit.addTest(TestDemo1('test_method1'))
suit.addTest(TestDemo1('test_method2'))
# 实例化运行对象
runner = unittest.TextTestRunner()
# 使用运行对象去执行套件对象
# 运行对象run（套件对象）
runner.run(suit)
