# 格式化字符串的两种方式
"""
%作占位符
我的名字叫%s，今年%d岁了      %       （name,age）
{}作占位符
我的名字叫{0}今年{1}岁了，我真叫{0}.format(name,age)
f-string
f‘我叫{name}，今年{age}岁’
"""
name = '张三'
age = 18
print("%作占位符")
print('我的名字%s，我的年龄%d' % (name, age))
print("{}作占位符")
print('我的名字{1}，我今年{0}岁了，我真的叫{1}'.format(name, age))
print("f-string")
print(f"我叫{name}，今年{age}岁")

print('*'*100)
print("%设置字符串宽度和精度和保留小数")
print('%10d' % 99)      # 10标识的是宽度
print('%.3f' % 3.14152926)      # 保留三位小数
print('%10.3f' % 3.14152926)    # 一共宽度为10，小数点后三位

print("{}设置字符串宽度和精度和保留小数")
print('{0:.3}'.format(3.1415926))   # .3表示的是一共是三位数
print('{:.3f}'.format(3.1415926))   # .3f表示的是3位小数
print('{:10.3f}'.format(3.1415926)) # 同时设置宽度和精度，一共是10位，3位是小数




