# 列表
"""
列表的特点
1.列表元素按顺序有序排列
2.索引映射唯一个数据
3.列表可以存储重复数据
4.任意数据类型混存
5.根据需要动态分配和回收内存
索引  -3      -2      -1
数据  hello   world   123456
索引  0       1       2
"""
a = [10, 20, 30, 40, 50, 60, 70, 80, 90]
b = [1, 2, 3]
c = ["一", "二", "三"]
"""创建列表的第一种方法,直接[]"""
print("创建列表的第一种方法,直接[]")
x = ["hello", "world", 123456]
print("列表元素按顺序有序排列")
print(x)
print("索引映射唯一个数据")
print(x[0], x[-3])
"""创建列表的第二种方法,使用内置函数"""
print("创建列表的第二种方法,使用内置函数")
y = list(["hello", "world", 123456, "hello", "world"])
"""空列表"""
print("空列表")
z = []
# z = list()
print(z)

print("*"*100)
"""index()方法
语法:str.index(指定检索的字符串, 开始位置，结束位置(不包括结束位置))
获取列表中的索引
1.如查找列表中存在N个相同元素，只返回相同元素中的第一个元素的索引
2.如果查询的元素在列表中不存在，则会抛出异常
3.还可以指定的start和stop之间进行查找
"""
print("如果列表中有相同元素，只返回相同元素中的第一个元素的索引")
print(y.index('hello'))
print("如果查询的元素在列表中不存在，则会抛出异常")
# print(y.index('hahaha'))  ValueError: 'hahaha' is not in list
# print(y.index('hello', 1, 3)) ValueError: 'hello' is not in list
print(y.index("hello", 1, 4))

print('*'*100)
"""获取列表中的单个元素
正向索引从0到N-1  举例 x[0]
逆向索引从-N到-1  举例 x[-N]
指定索引不存在     抛出异常

获取列表中的多个元素
语法格式:列表名[start  :      atop    :   step]
                开始   结束(不包括结束)   步长
        切片结果        与列表片段的拷贝  
        切片范围        (start, stop)
        step默认为1     简写为[start:stop]
                       [:stop:step]     切片的第一个元素默认是列表的第一个元素
        step为正数                                                              从start开始往后计算切片
切片操作                 [start::step]    切片的最后一个元素默认是列表的最后一个元素
                        [:stop:step]     切片的第一个元素默认是列表的最后一个元素
         step为负数                                                             从stop开始往前计算切片
                        [start::step]    切片的最后一个元素默认是列表的第一个元素
"""
print("切片操作，步长为正数")
print(a[1:7:2])
print("切片操作，步长为负数")
print(a[8::-1])

print('*'*100)
"""列表的增加
方法          操作描述
append（）    在列表的末尾添加一个元素
extend（）    在列表的末尾至少添加一个元素
insert（）    在列表的任意位置添加一个元素
切片          在列表的任意位置添加至少一个元素
"""
print("在b列表中添加一个元素")
print("增加元素之前", b, id(b))
b.append(4)
print("增加元素之后", b, id(b))
print("用append方法，将c放进b里")
b.append(c)
print(b, "说明是将c作为一个元素添加到列表的末尾")
print("用extend方法将c添加到b里面去")
b.extend(c)
print(b, "向列表末尾依次添加多个元素")
print("使用insert方法在任意位置添加元素")
b.insert(4, "帅的嘞")
print(b)
# 使用切片方法在末尾添加元素
print("使用切片的方法添加元素")
b[len(b):] = c
print(b, id(b))

print('*'*100)
"""列表的删除操作
            一次删除一个元素
remove（）   重复元素只删除第一个
            元素不存在抛出异常
            删除一个指定索引位置上的元素
pop（）      指定元素不存在抛出异常
            不指定索引，删除列表中最后一个元素
切片          一次至少删除一个元素
clear        清空列表
del          根据索引删除列表（可以直接删除列表）
"""
print("把b列表中的c元素移除")
b.remove(c)
print(b)
print("如果删除的元素不存在会抛出异常")
# print(b.remove(c))        ValueError: list.remove(x): x not in list
print("pop()根据索引删除元素")
b.pop(3)
print(b)
print("如果指定的索引不存在，将会抛出异常")
# print(b.pop(20))        IndexError: pop index out of range
print("如果不指定索引，会默认删除最后一个元素")
b.pop()
print(b)
print("使用切片的方法，但是将产生一个新的列表对象")
b1 = b[7:9]
print("原列表", b)
print("切片后的列表", b1)
print("不产生新的列表对象，而是删除原列表中的内容")
b[7:9] = []
print(b)
print("使用del语句删除某个元素")
del b[3]
print(b)
print("使用del语句删除多个元素")
del b[3:6]
print(b)
print("使用del语句清空列表")
del b[:]
print(b)
print("使用del语句删除列表")
del b
print("使用clear清空列表")
c.clear()
print(c)

print("*"*100)
"""列表的修改操作
为指定索引的元素赋予一个新值
为指定的切片赋予一个新值
"""
print("修改a中索引为二的值")
a[2] = 100
print(a)
print("修改多个值")
a[0:3] = [12, 23, 101, 33]
print(a)

print('*'*100)
"""列表的查询
判断指定元素是否在列表中存在
元素 in 列表名
元素 not in 列表名
列表元素的遍历
for 迭代变量  in 列表名 :
        操作
"""
print("列表的遍历")
for i in a:
    print(i)

print("*"*100)
"""列表元素的排序操作
sort（）方法语法
list.sort(key=None, reverse=False)
key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序
reverse -- 排序规则，reverse = True 降序， reverse = False 升序（默认)
内置函数sorted（）语法
sorted(iterable, cmp=None, key=None, reverse=False)
iterable -- 可迭代对象。
cmp -- 比较的函数，这个具有两个参数，参数的值都是从可迭代对象中取出，此函数必须遵守的规则为，大于则返回1，小于则返回-1，等于则返回0。
key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
reverse -- 排序规则，reverse = True 降序 ， reverse = False 升序（默认）。
区别:sort改变的是原列表，sorted原列表不发生改变
"""
print("开始排序，调用sort方法，默认是升序排序")
print("排序前的列表", a, id(a))
a.sort()
print("排序后的列表", a, id(a))
print("通过关键字参数，将列表中的元素进行降序排序")
a.sort(reverse=True)
print(a)
print("使用sorted排序")
a1 = sorted(a)
print(a1)
print("使用关键字参数排序")
a2 = sorted(a, reverse=True)
print(a2)

print('*'*100)
"""
列表生成式简称“生成列表的公式”
语法格式：
[i*i for i in range(1,10)]
"""
print("列表生成式")
n = [j for j in range(1, 10)]
print(n)
print("列表中的元素的值为2，4，6，8……")
m = [j*2 for j in range(1, 6)]
print(m)
