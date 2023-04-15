# 字符串的大小写转换操作的方法
"""
方法名称            作用
upper()            把字符串中所有字符都转换成大写字母
lower()            把字符串中所有字符都转换成小写字母
swapcase()         把字符串中所有大写字母都转换成小写字母，把所有小写字母都转成大写字母
capitalize()       把第一个字符转换为大写，把其余字符转换为小写
title()            把每个单词的第一个字符转换为大写，把每个单词的剩余字符转换为小写
"""
x = 'hello,python'
y = 'Hello,World,python'
print("使用upper（）方法把所有字符都转换成大写字母")
print("转换成大写后，会产生一个新的字符串对象")
a = x.upper()
print('原字符串', x, id(x))
print('改变后的字符串', a, id(a))
print("使用lower（）方法把所有字符都转换成大写字母")
print("转换成小写后，会产生一个新的字符串对象")
b = x.lower()
print('原字符串', x, id(x))
print('改变后的字符串', b, id(b))
print("使用swapcase()方法，把字符串中所有大写字母都转换成小写字母，把所有小写字母都转成大写字母")
print('原字符串', y, id(y))
print('改变后的字符串', y.swapcase(), id(y.swapcase()))
print("使用title（）方法,把每个单词的第一个字符转换为大写，把每个单词的剩余字符转换为小写")
print('原字符串', y, id(y))
print('改变后的字符串', y.title(), id(y.title()))
print("使用capitalize（）方法,把第一个字符转换为大写，把其余字符转换为小写")
print('原字符串', x, id(x))
print('改变后的字符串', x.capitalize(), id(x.capitalize()))
