# 元组
"""python内置的数据结构之一，是一个不可变序列"""
# 元组的创建方式
"""第一种创建方式，使用（）"""
print('第一种创建方式，使用（）')
x = ('hello', 'world', 1, 'hello')
print(x, type(x))
"""第二种创建方式,省略小括号创建"""
print("第二种创建方式,省略小括号创建")
z = 'hello', 'world', 3
print(z, type(z))
# 注意只有一个元素的时候
print("当只有一个元素的时候要记得在元素后面加逗号！！！！！！！！！")
r1 = 'hello',
print(r1, type(r1))
r2 = ('hello',)
print(r2, type(r2))
"""第三种创建方式，使用内置函数tuple（）"""
print("第三种创建方式，使用内置函数tuple（）")
y = tuple(('hello', 'world', 1))
print(y, type(y))
print("错误写法:y = tuple('hello', 'world', 2)")
"""空元组"""
print("空元组")
o = ()
# o = tuple()
print(o)
"""为什么要将元组设计成不可变序列
在多任务环境下，同时操作对象时不需要加锁
因此，在程序中尽量使用不可变序列
注意事项:元组中存储的是对象的引用
1.如果元组中对象本身不可变对象，则不能在引用其他对象
2.如果元组中的对象是可变对象，则可变对象的引用不允许改变，但数据可以改变
"""
a = (10, [1, 2], 20)
print(a, type(a), id(a))
"""尝试将a[1]修改为100"""
# a[1] = 100
print("尝试将a[1]修改为100")
print("报错TypeError: 'tuple' object does not support item assignment\n元组中是不允许修改元素的")
"""由于[1，2]列表，而列表是可变序列，所以可以向列中添加元素，而列表的内存地址不变"""
print("由于[1，2]列表，而列表是可变序列，所以可以向列中添加元素，而列表的内存地址不变")
a[1].append(3)
print(a, id(a))
"""第一种获取元组的方式，使用索引"""
print("第一种获取元组元素的方式，使用索引")
print(a[0])
print(a[1])
print(a[2])
"""元组的遍历"""
print("元组是可迭代对象，所以可以使用for...in进行遍历")
print("第二种获取元组元素的方式，遍历")
for i in a:
    print(i)
