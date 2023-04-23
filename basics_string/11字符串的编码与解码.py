# 字符串的编码转换
"""
为什么需要字符串的编码转换
A计算机                                                      B计算机
str在内存中以
Unicode表示----->编码------->byte字节转换-------->解码-------->显示

编码与解码的方式
编码:将字符串转换为二进制数据bytes
解码:将bytes类型的数据转换成字符串类型
"""
a = '轻舟已过万重山'
# 编码
print('编码')
print('在GBK这种编码格式中，一个中文占两个字节')
print(a.encode(encoding='GBK'))
print('在UTF-8这种编码格式中，一个中文占三个字节')
print(a.encode(encoding='UTF-8'))
# 解码
print('解码')
# byte 代表就是一个二进制数据（字节类型的数据）
byte = a.encode(encoding='GBK')        # 编码
print(byte.decode(encoding='GBK'))     # 解码
b = a.encode(encoding='UTF-8')
print(b.decode(encoding='UTF-8'))
