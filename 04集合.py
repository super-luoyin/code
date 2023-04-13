# 集合
"""什么是集合
python语言提供的内置数据结构
与列表，字典一样都是属于可变类型
集合是没有value的字典
集合是无序的
"""
a = {1, 2, 3, 4, 5}
"""第一种创建方式使用{}"""
print("第一种创建方式使用{}")
print("集合中的元素不允许重复")
x = {1, 2, 3, 4, 5, 6, 7}  # 集合中的元素不允许重复
print(x)
"""第二种创建方式使用set（）"""
print("第二种创建方式使用set（）")
y = set(range(6))
print(y)
"""空集合"""
z = set()
# z = {''}
print(z, type(z))

print('*' * 100)
print('其他类型转换为集合类型')
# 列表转化为集合类型
print("列表转化为集合类型")
y2 = set([1, 3, 4, 2, 5, 5])  # 证明集合是无序的,且不会重复
print(y2)
# 元组转化为集合类型
print('元组转化为集合类型')
y3 = set((1, 2, 3, 4, 65, 4, 7))
print(y3)
# 字符串转集合类型
print('字符串转集合类型')
y4 = set('python')
print(y4)

print('*'*100)
"""集合元素的判断操作(集合的查找)"""
print(5 in a)       # True
print(5 not in a)   # False
"""集合的增加
方法          描述
add()        一次中添加一个元素
update()     至少添加一个元素
"""
print("使用add()方法")
a.add(6)
print(a)
print("使用update方法")
a.update({7, 8, 9})
print(a)
print("还可以将列表和元组中的元素添加到集合中")
a.update([10, 20, 30])
a.update((40, 50, 60))
print(a)
"""集合的删除
方法              描述
remove()         一次删除一个指定元素，如果指定的元素不存在抛出异常
discard()        一次删除一个指定元素，如果指定的元素不存在不抛出异常
pop()            一次只能删除一个任意元素
clear()          清空集合
"""
print("使用remove方法")
a.remove(60)
print(a)
# a.remove(666)     KeyError: 666
print("使用remove方法删除一个不存在的数会抛出异常, KeyError: 不存在的数")
print("使用discard方法")
a.discard(50)
print(a)
print("使用discard方法删除一个不存在的数不会抛出异常")
a.discard(666)
print("pop方法是删除最后一个元素，因为集合是无序的所以不知道删谁，是随机的")
a.pop()
print(a)
print("并且pop方法不能指定参数，否则会报错")
print('TypeError: set.pop() takes no arguments (1 given)')
print("使用clear清空元素")
a.clear()
print(a)

print('*'*100)
"""
A{1，2，3，4，5，6}      B{1,2,3}
两个集合是否相等                可以使用运算符==或!=进行判断
一个集合是否是另一个集合的子集     可以调用方法issubset进行判断  B是A的子集
一个集合是否是另一个集合的超集     可以调用方法issuperset进行判断 A是B的超集
两个集合是否没有交集             可以调用方法isdisjoint进行判断 
"""
print("集合间的关系")
print("两个集合是否相等")
b = {10, 20, 30, 40}
b1 = {30, 40, 20, 10}
print(b == b1)
print(b != b1)
b3 = {10, 20, 30, 40, 50, 60}
b4 = {10, 20, 30, 40}
b5 = {10, 20, 90}
b6 = {100, 200, 300}
print("一个集合是否是另一个集合的子集")
print(b4.issubset(b3))
print(b5.issubset(b3))
print("一个集合是否是另一个集合的超集")
print(b3.issuperset(b4))
print(b3.issuperset(b5))
print("两个集合是否没有交集 ")
print("没有交集为True")
print(b4.isdisjoint(b5))    # False
print(b4.isdisjoint(b6))    # 没有交集为True

print('*'*100)
"""集合的数学操作
A {1，2，3，4}     B{3，4，5，6}
交集  {3，4}                   intersection()和&等价
并集  {1，2，3，4，5，6}         union()和|等价
差集  {1，2}                   difference()和-等价
对称差集{1，2，5，6}             symmetric_difference()和^等价
"""
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
"""交集"""
print("交集:intersection()和&等价")
print(A.intersection(B))
print(A & B)
"""并集"""
print("并集:union()和|等价")
print(A.union(B))
print(A | B)
"""差集"""
print("差集:difference()和-等价")
print(A.difference(B))
print(A - B)
"""对称差集"""
print("对称差集:symmetric_difference()和^等价")
print(A.symmetric_difference(B))
print(A ^ B)

print('*'*100)
"""集合生成式
语法格式：
{i*i for i in range(1,10)}
"""
print("集合生成式")
e = {i*i for i in range(10)}
print(e, type(e))
