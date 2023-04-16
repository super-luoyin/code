# 演示对文件的写入
"""
一.写入文件使用open函数的”w“模式进行写入
二.写入的方法有:1.wirte(),写入内容；2.flush(),刷新内容到硬盘中
注意:
直接调用write，内容并未真正写入文件，而是会积攒在程序的内存中，称之为缓存区
当调用flush的时候，内容会真正写入文件
这样做是避免频繁的操作硬盘，导致效率下降（攒一堆，一次性写入磁盘）
注意事项
w模式，文件不存在，会创建新文件夹
w模式，文件存在，会清空原有内容
close（）方法， 带有flush（）方法的功能
"""
# 打开文件，不存在的文件
f = open("test1", "w", encoding="UTF-8")
# write导入
f.write("hello,world!!!!!")
# flush刷新
# f.flush()
# close 关闭
f.close()
# 打开一个存在的文件
w = open("test1", "w", encoding="UTF-8")
# write写入，flush刷新
w.write("你好，python")
w.flush()
# close关闭
w.close()





















