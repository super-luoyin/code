import time

print("加载中", end='')        # print函数中end的用法
for i in range(1, 6):
    print('.', end='')
    time.sleep(0.5)

print()                       # print函数sep的用法
print("1", "2", "3")
print("1", "2", "3", sep=',')
