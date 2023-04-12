# 字符串的查询操作
"""
方法名称            作用
index（）          查找子串substr第一次出现的位置，如果查找的子串不存在时，则抛出异常
rindex()          查找子串substr最后一次出现的位置，如果查找的字串不存在时，则抛出异常
find（）           查找字串substr第一次出现的位置，如果查找的子串不存在时，则返回-1
rfind（）          查找字串substr最后一次出现的位置，如果查找的字串不存在时，则返回-1
"""
x = 'hello,hello'
print("查询第一次lo出现的位置")
print(x.index('lo'))
print(x.find('lo'))
print("查询第二次lo出现的位置")
print(x.rindex('lo'))
print(x.rfind('lo'))
"""原理
-11 -10 -9  -8  -7  -6  -5  -4  -3  -2  -1
h   e   l   l   o   ,   h   e   l   l   o
0   1   2   3   4   5   6   7   8   9   10
第一次出现    |   |
最后一次出现：                         |   |
"""
print("查询不存在的k值第一次出现的位置")
print("print(x.index('k'))")
print("抛出异常:ValueError: substring not found")
print(x.find('k'))
print("查询不存在的k值最后一次出现的位置")
print("print(x.rindex('k'))")
print("抛出异常:ValueError: substring not found")
print(x.rfind('k'))
