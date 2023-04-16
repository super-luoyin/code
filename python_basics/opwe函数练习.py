"""通过文件读取操作，读取此文件， 统计itheima出现的次数"""
from itertools import count
f = open("word", 'r', encoding="UTF-8")
# 方法1   with open
"""s = 0
with open("word") as w:
    for line in w:
        a = line.count("itheima")
        s += a
    print(s)
"""
# 方法2 读取全部内容，通过字符串的count方法统计itheima单词数量
"""lines = f.read()
num = lines.count("itheima")
print(num)
"""
# 方法2 读取内容，一行一行读取
num = 0
for line in f:
    line = line.strip()     # 去除开头和结尾的空格以及换行符
    words = line.split(" ")
    for word in words:
        if word == "itheima":
            num += 1
print(num)
# 关闭文件
f.close()
