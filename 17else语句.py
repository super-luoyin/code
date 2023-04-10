# else语句
"""与else搭配的三种情况
if ……：      while ……：       for ……：
   ……              ……             ……
else：       else：           else：
   ……              ……             ……
"""
a = 0
while a < 3:
    pwd = input("请输入密码")
    if pwd == '123456':
        print("密码正确")
    else:
        print("密码错误")
    a += 1
else:
    print("对不起，三次密码均输入错误")
