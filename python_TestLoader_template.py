# 学习TestLoader测试加载书写方法
# 1.导包
import unittest
# 2.实例化测试加载对象并添加用例      --->得到的是suite对象
# unittest.TestLoader().discover('用例所在的路径', '用例的代码文件名')
# 用例所在的路经，建议使用相对路径，用例的代码文件名可以使用*（任意多个任意字符）通配符
suit = unittest.TestLoader().discover('./case', 'Test*')
# suit = unittest.defaultTestLoader.discover('./case', 'test*')
# 3.实例化运行对象
runner = unittest.TextTestRunner()
# 4.运行对象执行套件对象
runner.run(suit)
# 可以把3，4步变一步
# unittest.TextTestRunner().run(suit)
