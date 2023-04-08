"""
多分支结构
"""
"""语法结构:
if 条件表达式1:
    条件执行体1
elif 条件表达式2:
    条件执行体2
elif 条件表达式N:
    条件执行体N    
else:
    条件执行体N+1
"""
score = int(input("请输入成绩"))
# if score <= 90 and score <= 100
if 90 <= score <= 100:
    print("A级")
elif 80 <= score <= 89:
    print("B级")
elif 70 <= score <= 79:
    print("C级")
elif 60 <= score <= 69:
    print("D级")
elif 0 <= score <= 59:
    print("E级")
else:
    print("对不起，成绩有误，不在成绩的有效范围内")
