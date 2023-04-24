"""
单分支结构
"""
"""语法结构:
    if 条件表达式 :
        条件执行体
"""
num = 10000
x = int(input("请输入取款金额"))
if num >= x:
    num -= x
    print("你的余额还剩", num)
