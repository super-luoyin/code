"""
一、追加写入文件使用open函数的”a”模式进行写入
二、追加写入的方法有（和w模式一致）
wirte（）写入内容
flush（）刷新内容到硬盘中
注意事项:
a模式，文件不存在，会创建新的文件
a模式，文件存在，会在原有内容后面继续写入
可以使用“\n”来写出换行符
"""
# 打开文件
f = open("test1", "a", encoding="UTF-8")
# write写入
f.write("\nhello.world")
# flush刷新
f.flush()
# close关闭
f.close()

















