# 判断字符串操作的方法
"""
方法名称                作用
isidentifier()         判断指定的字符串是不是合法的标识符
isspace()              判断指定的字符串是否全部由空白字符组成（回车，换行，水平制表符）
isalpha()              判断指定的字符串是否全部由字母组成
isdecimal()            判断指定的字符串是否全部由十进制的数字组成
isnumeric()            判断指定的字符串是否全部由数字组成
isalnum()              判断指定的字符串是否全部由字母和数字组成
"""
"""python中合法的标识符
1.第一个字符必须是字母表中字母或下划线
2.标识符的其他的部分由字母、数字和下划线组成
3.标识符对大小写敏感
4.在python3中，可以用中文作为变量名，非ASCll标识符也是允许的
"""
x = 'hello,python'
print("判断以下的字符串是不是合法的标识符")
print('1.', x.isidentifier())
print('2.', 'hello'.isidentifier())
print('3.', '张三'.isidentifier())
print('4.', '张三_123'.isidentifier())

print('-------------------------------------------')
print("判断下列的字符串是不是由（回车，换行，水平制表符）组成")
print('1.', '\t'.isspace())

print('-------------------------------------------')
print("判断下面的字符串是不是全部由字母组成的")
print('1.', 'abc'.isalpha())
print('2.', '张三'.isalpha())

print('-------------------------------------------')
print("判断下面的字符串是否全部由十进制的数字组成")
print('1.', '123'.isdecimal())
print('2.', '123四'.isdecimal())
print('3.', '123Ⅱ'.isdecimal())

print('-------------------------------------------')
print("判断下面的字符串是否全部由数字组成")
print('1.', '123'.isdecimal())
print('2.', '123四'.isdecimal())
print('3.', 'II'.isdecimal())

print('-------------------------------------------')
print("判断指定的字符串是否全部由字母和数字组成")
print('1.', 'abc1'.isalnum())
print('2.', '张三123'.isalnum())
print('2.', 'abc!'.isalnum())
