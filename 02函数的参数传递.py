# 函数的参数传递
"""
函数调用的参数传递                    add(10, 20)
位置传参                                 |   |
根据形参对应的位置进行实参传递      def add(10, 20)

关键字传参                         add(b = 10, a = 20)
根据形参名称进行实参传递           def add(a,b)
"""


def add(a, b):      # a,b称为形式参数，简称形参，形参的位置是在函数的定义处
    c = a + b
    return c


x = add(10, 20)     # 10，20称为实际参数的值，简称实参。实参的位置是函数的调用处
print(x)


y = add(b=10, a=20)     # 左侧的变量的名称为 关键字参数
print(y)
