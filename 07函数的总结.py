# 函数的总结
"""
函数的类型                           函数的定义           函数的调用       备注
位置实参                                                    T
将序列中的每个元素都转换为位置实参                               T           使用*
关键字实参                                                  T
将字典中的每个键值对都转换为关键字实参                            T           使用**
默认值形参                               T
关键字形参                               T                               使用*
个数可变的位置形参                         T                               使用*
个数可变的关键字形参                       T                               使用**
"""


def fun(a, b, c):       # a,b,c在函数定义处，所以是形式参数
    print("a", a)
    print("b", b)
    print("c", c)


fun(10, 20, 30)         # 函数调用时的参数传递，称为位置传参
lst = (11, 22, 33)
print("直接传参fun(lst)")
print("会抛出异常TypeError: fun() missing 2 required positional arguments: 'b' and 'c'")
print("应该带*号，将列表中的每个元素都转换为位置实参传入")
fun(*lst)
print("-"*20)
fun(a=100, b=200, c=300)    # 函数的调用，所以是关键字实参
dic = {'a': 111, 'b': 222, 'c': 333}
print("直接传入fun(dic)")
print("会抛出异常TypeError: fun() missing 2 required positional arguments: 'b' and 'c'")
print("应该带**号,将字典中的每个键值对都转换为关键字实参传入")
fun(**dic)

print('*'*150)


def function(a, b=10):      # b是在函数的定义处，所以b是形参，而且进行了赋值，所以b称为默认值形参
    print('a', a)
    print('b', b)


def function1(a, b, c, d):
    print('a', a)
    print('b', b)
    print('c', c)
    print('d', d)


print("位置实参传递")
function1(10, 20, 30, 40)
print("关键字实参传递")
function1(a=11, b=22, c=33, d=44)
print("前两个参数，采用的是位置实参传递，而c，d采用的是关键字实参传递")
function1(12, 23, c=34, d=45)

"""函数定义时的形参的顺序问题"""
print("函数定义时的形参的顺序问题")


def function2(a, b, *, c, d):
    pass
