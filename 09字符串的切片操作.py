# 字符串的切片操作
"""字符串是不可变类型
不具备增删改等操作
切片操作将产生新的对象
"""
x = 'hello,python'
x1 = x[:5]          # 由于没有指定起始位置，所以从0开始
x2 = x[6:]          # 由于没有指定结束位置，所以切到字符串的最后一个元素
b = '!'
c = x1+b+x2
print(c, id(c))
print(x, id(x))
print(x1, id(x1))
print(x2, id(x2))
print(b, id(b))
print("---------------切片[statr:end:step]-----------------")
print(x[1:5:1])         # 从1开始截到5（不包含5），步长为1
print(x[::2])           # 默认从0开始，没有写结果，默认到字符串的最后一个元素，步长为2，两个元素之间的索引间隔为2
print(x[::-1])          # 默认从字符串的最后一个元素开始，到字符串的第一个元素结束，因为步长为负数
print(x[-6::1])         # 从索引为-6开始，到字符串的最后一个元素结束，步长为1
