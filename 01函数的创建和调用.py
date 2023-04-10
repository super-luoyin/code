# 函数的创建和调用
"""
什么是函数
函数就是执行特定任和以完成特定功能的一段代码
为什么需要函数
1.复用代码
2.隐藏实现细节
3.提高可维护性
4.提高可读性便于调试
函数的创建
def 函数名 （[传入参数]）:
    函数体
    [return xxx]
"""


def add(a, b):
    c = a + b
    return c


x = add(3, 4)
print(x)
