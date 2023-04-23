# 字符串的比较操作
"""
字符串的比较操作
运算符: >,>=,<,<=,==,!=

比较规则:首先比较两个字符串中的第一个字符，如果相等则继续比较下一个字符，
一次比较下去，直到两个字符串中的字符不相等时，其比较结果就是两个字符串的
比较结果，两个字符串的所有后续字符将不再比较

比较原理:两个字符串比较时，比较的是其ordinal value（原始值），调用内置函数
ord可以得到指定字符的ordinal value。与内置函数ord对应的是内置函chr，调用
内置函数chr时指定ordinal value可以得到其对应的字符
"""
print("字符串的比较")
print('apple' > 'app')
print('apple' > 'banana')
print("ord返回的是Unicode值，只不过Unicode值是ASCll的超集")
print(ord('a'), ord('b'))
print(ord('罗'))
print(chr(97), chr(98))
print(chr(32599))

"""
== 和 is 的区别
== 比较的是value
is 比较的是id是否相等
"""
a = b = 'python'
c = 'python'
print(a == b)
print(a == c)
print(b == c)
print(a is b is c)
