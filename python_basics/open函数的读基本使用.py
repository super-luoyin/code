"""演示对文件的读取"""
# 打开文件
# f = open('test', 'r', encoding="UTF-8")
# 读取文件 - read()     读取字节
"""连续调用read，下一个read会在上一个read的结尾处接着读取"""
# print(f"读取10个字节的结果:{f.read(10)}")
# print(f"read读取全部内容的结果是：{f.read()}")
print('*'*50)
# 读取文件 - readLines()
# 每次读取文件都会有指针，此处指针已经在结尾了，所有无法读取到任何东西
# lines = f.readlines()   # 读取文件的全部行，封装到列表中
# print(f"lines对象的类型是:{type(lines)}")
# 为什么没有读取到内容，虽然read和readLines是两个不同的方法，但是他们指向的同一个对象
# print(f"lines对象的内容是:{lines}")
print('*'*50)
# 读取文件 - readline（）     一次读取一行内容
# line1 = f.readline()
# line2 = f.readline()
# line3 = f.readline()
# print(f"第一行数据:{line1}")
# print(f"第二行数据:{line2}")
# print(f"第三行数据:{line3}")
# for循环读取文件行
# for line in f:
#     print(f"每一行数据:{line}")
# 文件的关闭
"""最后通过close，关闭文件对象，也就是关闭对文件的占用
如果不调用close，同时程序也没有停止运行，那么这个文件将一直被python程序占用"""
# f.close()
# with open 语法操作文件
"""with open在执行完其中的语句块的时候会自动的close"""
with open('test', 'r', encoding="UTF-8") as f:
    for line in f:
        print(f"每一行数据:{line}")














