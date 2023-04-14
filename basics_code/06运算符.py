# 运算操作符
print("运算操作符")
print(9+2)      # 加法运算
print(9-2)      # 减法运算
print(9*2)      # 乘法运算
print(9/2)      # 除法运算
print(11/2)     # 整数运算
print(11 % 2)   # 取余运算
print(2**3)     # 表示的是2的3次方
print(9//-4)    # -3
print(-9//4)    # -3  一正一负的整数公式，向下取值
print(9 % -4)   # -3 公式 余数=被除数-除数*商     9-（-4）*（-3） 9-12--> -3
print(-9 % 4)   # 3 -9-4*(-3)   -9+12-->3
print("-"*100)

# 赋值运算符
print("赋值运算符")
i = 2+3
print(i)
print("链式赋值")
a = b = c = 20      # 链式赋值
print(a, id(a))
print(b, id(b))
print(c, id(c))

# 支持参数赋值
j = 0
print(j)
j += 1
print(j)
j -= 0
print(j)
j *= 2
print(j)
j /= 2
print(j)
j %= 2
print(j)
j **= 2
print(j)
j //= 2
print(j)
if x := 5 < 10:
    print("helloworld")
print(j)

print('-'*50)
# 解包赋值
print("解包赋值")
a, b, c = 1, 2, 3
print(a, b, c)
# a, b = 10, 20, 30    报错，因为左右变量的个数和值的个数不对应
# 交换两个变量的值
a, b = 10, 20
print("交换之前", a, b)
a, b = b, a
print("交换之后", a, b)

print('-'*100)
# 比较运算符
print("比较运算符")
a, b = 10, 20
print("a>b吗?", a > b)
print("a>=b吗?", a >= b)
print("a<b吗?", a < b)
print("a<=b吗?", a <= b)
print("a==b吗?", a == b)
print("a!=b吗?", a != b)
'''一个 = 称为赋值运算符，==称为比较运算符
一个变量由三部分组成，标识，类型，值
== 比较的是值
is 比较的是对象'''
print('-'*50)
x = 10
y = 10
print(x == y)   # 说明，a与b的value 相等
print(x is y)   # 说明，a与b的id标识 相等
lis1 = [11, 22, 33, 44]
lis2 = [11, 22, 33, 44]
print(lis1 == lis2)
print(lis1 is lis2)
print(id(lis1))
print(id(lis2))

# 布尔运算符（逻辑运算符）
q, w = 1, 2
print("---------and 并且----------")
print(q == 1 and w == 2)
print(q == 1 and w != 2)
print(q != 1 and w == 2)
print(q != 1 and w != 2)
print("---------or 或者----------")
print(q == 1 or w == 2)
print(q == 1 or w != 2)
print(q != 1 or w == 2)
print(q != 1 or w != 2)
print("---------not 非----------")
q1 = False
q2 = True
print(not q1)
print(not q2)
print("---------in 与 not in----------")
w1 = "abcdef"
print('s' in w1)
print('s' not in w1)
print('a' in w1)
print('a' not in w1)
# 位运算符
print("位运算符")
n, m = 2, 4
print(n & m)
print(n | m)
print(n ^ m)
print(~n)
print(n << 1)
print(m >> 1)

