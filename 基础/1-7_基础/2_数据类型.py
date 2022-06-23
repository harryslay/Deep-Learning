# 数据类型 整形
n1 = 90
n2 = -76
n3 = 0
print(n1,type(n1))
print(n2,type(n2))
print(n3,type(n3))

print('十进制',118)
print('二进制',0b10101111)
print('八进制',0o176)
print('十六进制',0x176A)

# 浮点数 存储位置不精确
a = 3.14159
print(a ,type(a))
a1=1.1
a2=2.2
print(a1+a2)
print(1.1+2.1) #有时候就很精确 是二进制的底层问题
# 需要处理模块来对多余的小数进行处理
from decimal import Decimal
print(Decimal('1.1')+Decimal('2.2'))

# bool 可以转成整数类型计算 t:1 f:2
f1 = True
f2 = False
print(f1,type(f1))
print(f2,type(f2))
print(f1+1)
print(f2+1)

#char 不可变的字符序列 ''  ""  “”“ ”“”
str1='人生苦短'
print(str1,type(str1))
str2 = "我用python"
print(str2,type(str2))
str3 = """
人生
苦短
"""
print(str3,type(str3)) #或者用三个单引号


