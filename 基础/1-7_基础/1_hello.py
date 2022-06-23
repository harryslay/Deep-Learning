print("hello \npython")
print("hello\tpython!") # \t制表符 具体空多少看之前有没有完全被占满
print("hello\rpython!!") # \r回车 把之前覆盖掉
print("hello\bpython!!!") # \b退一个格 把o覆盖掉了

print('http:\\\\www.baidu.com') # 转义字符 \写成两个\\
print('老师：\'大家好\'')
# 原字符，不希望字符串中的转义字符起作用 在字符串前加r或R
print(r'hello\nworld') #\n不起作用
# print(r'hello\nworld\') #最后一个字符不能是\ 报错

# 8bit=1 byte
# 1024byte = 1kb。。。mb gb

print(chr(0b100111001011000)) #0b:二进制之前
print(ord('乘')) # 返回字符的int类型

import  keyword
print(keyword.kwlist) #关键字

name = 'mary'
print(name)
print('标识',id(name))  # 地址
print('类型',type(name))
print('值',name)
name = 'olivia'
print(name)