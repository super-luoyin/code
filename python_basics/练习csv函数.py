"""csv文件的读取"""
# lst_testdata = []
# with open('testdata.csv', mode='r', encoding='utf-8') as f:
#     next(f, None)
#     for item_f in f:
#         lst_testdata.append(item_f.strip().split(','))
#     print(lst_testdata)
"""csv文件的写入
一、通过创建writer对象，主要用到2个方法
1.writerow，写入一行
2.writerows，写入多行
二、使用DictWriter可以使用字典的方式把数据写入
"""
import csv
"""
a = [[1, 2], [3, 4], [5, 6], [7, 8]]
b = ['编号', '成绩']
with open('表格.csv', 'a', encoding='UTF-8', newline='') as f:
    # 创建writerow对象
    w = csv.writer(f)
    # 写入表头
    w.writerow(b)
    # 写入数据
    w.writerows(a)
"""
a = [{'name':'张三', 'age':'18', 'bh':'001'},
     {'name':'李四', 'age':'19', 'bh':'002'},
     {'name':'王五', 'age':'18', 'bh':'003'}]
b = ['name', 'age', 'bh']
with open('表格.csv', 'a', encoding='UTF-8', newline='') as f:
    w = csv.DictWriter(f,b)
    w.writeheader()
    w.writerows(a)
