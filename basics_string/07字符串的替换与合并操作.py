# 字符串的操作与合并操作的方法
"""
方法名称            作用
replace()          第一个参数指定被替换的子串，第二个参数指定替换子串的字符串，该方法返回替换后得到的
                    字符串，替换前的字符串不发生变化，调用该方法时可以通过第3个参数指定最大替换次数
join()             将列表或元组中的字符串合并成一个字符串
"""
print("使用replace替换字符串")
x = 'hello,python'
print(x.replace('python', 'java'))
y = 'hello，python,python,python'
print(y.replace('python', 'java', 2))
print("使用join（）将下列字符串进行合并")
print("合并列表字符串")
a = ['hello', 'python', 'java']
print('|'.join(a))
print(''.join(a))
print("合并元组字符串")
b = ('hello', 'java', 'python')
print(''.join(b))
print("合并字符串")
print('*'.join('python'))
