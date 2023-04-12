# 变量的作用域
"""变量的作用域
根据变量的有效范围可以分为
局部变量
在函数内定义并使用的变量，只在函数内部有效，局部变量使用global声明，这个变量就会变成全局变量
全局变量
函数体外定义的变量，可作用于函数内外
"""
a = 'hello'


def fun():
    return a+' python'


a1 = fun()
print(a1)       # 在没有局部变量时，使用全局变量，且函数内部不能改变全局变量的值
print(a)


print("使用global函数，使自定义的函数可以改全局变量的值")


def fun1():
    global a
    a = a+' world'
    return a


x = fun1()
print(x)
print(a)

print("想要在函数外面输出函数内的值也要用到global")
print("想调用局部变量的前提是使用这个变量，不使用是调用不了的")


def fun2():
    global age
    age = 20
    print(age)


fun2()
print(age)
