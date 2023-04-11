# 函数的返回值
"""
函数的返回值
1、如果函数没有返回值[函数执行完毕之后，不需要给调用处提供数据]   return可以忽略不写
2、函数的返回值，如果是1个，直接返回类型
3、函数的返回值，如果是多个，返回的结果为元组
"""


def fun(num):
    a = []
    b = []
    for i in num:
        if i % 2:
            a.append(i)
        else:
            b.append(i)
    return a, b


x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(fun(x))


def fun1():
    print("hello")


fun1()


def fun2():
    return 'hello'


print(fun2())


def fun3():
    return 'hello', 'world'


print(fun3())
