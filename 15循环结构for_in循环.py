# for_in循环
"""语法结构
for 自定义的变量 in 可迭代对象:
    循环体

循环体内不需要访问自定义变量，可以将自定义变量代替为下划线
"""
for _ in range(3):
    print("重要的事情说三遍")

num = 0
for i in range(101):
    num += i

print(num)
