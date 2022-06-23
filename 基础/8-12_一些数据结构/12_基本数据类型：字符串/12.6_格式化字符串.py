'''
格式化字符串
 %占位符
 {}占位符
 f-string
'''
name='ee'
age=19
age1='19'
# 我叫ee，今年19岁
# print('我叫'+name+'，今年'+age1+'岁') #+用来进行字符串的拼接 全是str类型才可以拼接

print('我叫%s，今年%d岁'%(name,age))

print('我叫{0}，今年{1}岁'.format(name,age))

print(f'我叫{name}，今年{age}岁')

'''表示精度和宽度

'''

print('%10d' % 99) #表示宽度
print('hellohello')
print('%.3f' % 3.1415926) #保留精度
print('%10.3f' % 3.1415926) #保留精度和宽度

print("{:.3}".format(3.1415926)) #只有一个可以不写索引  .3表示一共只有3位
print("{0:.3f}".format(3.1415926)) #只有一个可以不写索引  .3f三位小数
print("{0:10.3f}".format(3.1415926)) #一共十位 .3f三位小数


