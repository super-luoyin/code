print("hello\
      work")                # 续行符
print("hello\nworld")       # 换行符
print("12345\t789")
print("1234\t123")          # \t占四个字符，当前的字符不是4的倍数时，先补齐
print("123456\a")           # 执行后电脑有响声
print("hello world taobao\r123456")     # 将\r后面的内容移到字符串开头，并逐一替换开头部分的字符，直至将\r后面的内容全部替换完成
print("222229\b2222")       # \b是退一格，将9退没了
print("\\")
print("\"")
print("\'")
print("\000")
print("hello\vworld")       # 纵向制表符
print("hello\fworld")       # 换页
print("\110\145\154\154\157\40\127\157\162\154\144\41")               # \yyy八进制数
print("\x48\x65\x6c\x6c\x6f\x20\x57\x6f\x72\x6c\x64\x21")              # \xx十六进制数

# 原字符，不希望字符串中的转义字符起作用，就使用原字符，就是在字符串前面加上r，或者R
print(r"hello\n world")
# 注意事项，最后一个字符不能是反斜杠
# print(r' hello\nwo\')
