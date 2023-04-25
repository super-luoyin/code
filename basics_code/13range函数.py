"""
range内置函数的使用
参数说明:range(start,stop[, step])
start:计数从start开始。默认是从0开始
stop:计数到stop结束。但是不包括stop
step:步长，默认是1
"""
# 第一种创建方式，给一个参数
a = range(10)
print(a, type(a))
print(list(a))  # 用于查看range对象中的整数序列
# 第二种创建方式，给两个参数
b = range(1, 10)
print(list(b))
# 第三种创建方式，给三个参数
c = range(1, 10, 2)
print(list(c))
# 判断指定的整数，在序列中是否存在
print(10 in a)
print(10 not in a)
