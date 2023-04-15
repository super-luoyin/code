# 字符串的劈分操作的方法
"""
方法名称            作用
                   从字符串的左边开始劈分，默认劈分字符是空格字符串，返回的值是一个列表
split()            以通过参数sep指定劈分字符串是劈分符
                   通过单独参数maxsplit指定劈分字符串时的最大劈分次数，在经过最大次劈分之后，剩余的字串会单独作为一部分

                   从字符串的右边开始劈分，默认的劈分字符串是空格字符串，返回的值都是一个列表
rsplit()           以通过参数sep指定劈分字符串是劈分符
                   通过参数maxsplit指定劈分字符串时的最大劈分次数，在经过最大次劈分之后，剩余的字串会单独做为一部分
"""
x = 'hello world python'
y = 'hello|world|python'
print("split()方法演示")
a = x.split()
print(a)
print("以|为劈分符，劈分y")
print(y.split(sep='|'))
print('最大劈分y一次')
print(y.split(sep='|', maxsplit=1))
print("rsplit（）方法演示")
print(x.rsplit())
print(y.rsplit(sep='|'))
print("最大劈分y一次")
print(y.rsplit(sep='|', maxsplit=1))
