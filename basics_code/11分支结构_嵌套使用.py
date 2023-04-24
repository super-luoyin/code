"""
嵌套的使用
"""
"""语法结构:
if 条件表达式:
    if 内层条件表达式:
        内层条件执行体1
    else:
        内存条件执行体2
else:
    条件执行体
"""
x = input("你是会员吗y/n")
y = int(input("请输入购物金额"))
if x == 'y':
    if y >= 200:
        print("打折后的价格是", 0.8*y)
    elif y >= 100:
        print("打折后的价格是", 0.9*y)
    else:
        print("付款金额为", y)
else:
    if y >= 200:
        print("打折后的价格是", 0.95*y)
    else:
        print("付款金额为", y)

