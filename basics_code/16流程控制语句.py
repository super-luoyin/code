# break 和continue
for i in range(3):
    pwd = input("请输入正确的密码")
    if pwd == '123456':
        print("密码正确")
        break
    else:
        print("密码错误")

print("-"*50)
# 求一百以内所有的偶数
for j in range(1, 100):
    if j % 2 != 0:
        continue
    print(j, end=' ')
