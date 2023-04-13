# 字典
"""
什么是字典
python内置的数据结构之一，与列表一样是一个可变序列
以键值对的方式存储数据，字典是一个无序的序列
字典的实现原理
字典的实现原理与查字典类似，查字典是先根据部首或者拼音
查找对应的页码，python中的字典是根据key查找value所在的位置
"""
"""
字典的特点
字典中的所有的元素都是一个 key-value对，key不允许重复，value可以重复
字典中的元素是无序的
字典中的key必须是不可变对象
字典也可以根据需要动态地伸缩
字典会浪费较大的内存，是一种使用空间换时间的数据结构
"""
a = {'张三': 1, '李四': 2, '王五': 3}
b = {'帅的勒': '我', '厉害的嘞': '你'}
"""创建字典的第一个方法,直接{}"""
print("创建字典的第一个方法,直接{}")
x = {'张三': 100, '李四': 200, '王五': 300}
print(x, type(x))
"""创建字典的第二个方法，使用内置函数dict()"""
print("创建字典的第二个方法，使用内置函数dict()")
y = dict(一=1, 二=2, 三=3)
print(y)
"""空字典"""
print("空字典")
z = {}
#  z = dict()
print(z)
"""
字典元素中的获取
[]取值    如果字典中不存在指定的key，会抛出异常
get()方法 如果字典中不存在指定的key，会返回None
         可以通过参数设置默认的value，以便指定的key不存在时返回
"""
print('第一种方式,使用[]')
print(a['李四'])
print('第二种方式,使用get()方法')
print(a.get('张三'))
print(a.get('孙七'))
print("get()方法当key不存在时指定返回None")
print(a.get('赵六', '没有'))

print('*'*100)
"""
key的判断
in      指定的key在字典中存在返回True
not in  指定的key在字典中不存在返回True
字典元素的删除
del a['张三']
字典元素的新增
a['周八']=4
"""
print("key的判断")
print('张三' in a)
print('张三' not in a)
print('字典的增加')
a['周八'] = 8
print(a)
print('字典的删除')
del a['周八']
print(a)
print('字典的清空')
b.clear()
print(b)
print('字典的改变')
a['张三'] = 3
print(a)

print('*'*100)
"""
获取字典视图的三个方法
keys()      获取字典中所有的key
values()    获取字典中所有的value
items()     获取字典中所有的key，value对
"""
print("获取a中所有的键")
a_key = a.keys()
print(a_key)
print("获取a所有的值")
a_value = a.values()
print(a_value)
print("获取a中所有的键值对")
a_items = a.items()
print(a_items)

print('*'*100)
"""
字典元素的遍历
"""
print("字典元素的遍历")
for a1 in a:
    print(a1, a[a1], a.get(a1))

print('*'*100)
"""
字典生成式
内置函数zip()
用于将可迭代的对象作为参数，将对象中对应的元素
打包成一个元组，然后返回由这些元组组成的列表
{item : price for item,price in zip(items,proces)}
"""
print("字典的生成式")
item = ['张三', '李四', '王五']
price = [3, 4, 5]
c = {item: price for item, price in zip(item, price)}
print(c)
