# 学习测试夹具Fixture的书写方法
"""方法级别（掌握）
在每个测试方法（用例代码）执行前后都会自动调用的结构
"""
"""代码演示
def setUp(self):
    在每个测试方法执行之前都会执行
    pass
def tearDown(self):
    在每个测试方法执行之后都会执行
    pass
"""
"""类级别（掌握）
在每个测试类中所有方法执行前后都会自动调用的结构
"""
"""代码演示
@classmethod
def setUpClass(cls):
    在每个测试类执行之前都会执行
    pass
@classmethod
def tearDownClass(cls):
    在每个测试类执行之后都会执行
    pass
"""
"""模块级别（了解）
在每个代码文执行前后都会自动调用的结构
"""
"""代码演示
模块级别需要写在类的外边直接定义函数即可
def setUpModule():
    在每个测试类执行之前都会执行
    pass
def tearDownModule():
    在每个测试类执行之后都会执行
    pass
"""
import unittest


class TestLuo(unittest.TestCase):
    def setUp(self) -> None:
        print("打开网页")

    def tearDown(self) -> None:
        print("关闭网页")

    @classmethod
    def setUpClass(cls) -> None:
        print("打开浏览器")

    @classmethod
    def tearDownClass(cls) -> None:
        print("关闭浏览器")

    def test_1(self):
        print("测试方法1")

    def test_2(self):
        print("测试方法2")
