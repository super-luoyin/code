"""
三元表达式
"""
a = int(input("请输入一个整数"))
b = int(input("请输入第二个整数"))
# 比较大小
"""
if a >= b:
    print(a, "大于等于", b)
else:
    print(a, "小于", b)
"""
print("使用三元条件表达式进行比较")
# 中间条件表达式正确执行左边的，错误执行右边的
print(str(a) + "大于等于" + str(b) if a >= b else str(a) + "小于" + str(b))

# pass语句
if a == 0:
    pass
else:
    pass
