"""
查询 大小写转换 内容对齐 字符串分割 字符串判断（字母数字？
"""

'''
查询方法：
1 index() 查找淄川第一次出现的位置，如果查找的子串不存在抛出valueError
2 rindex() 查找子串最后一次穿线的位置 同上↑
3 find() 查找子串第一次出现的位置 找不到返回-1
3 rfind() 查找子串最后一次出现的位置 找不到返回-1
'''

s = 'hello,hello'
print(s.index('lo')) #3
print(s.find('lo')) #3
print(s.rindex('lo')) #9
print(s.rfind('lo')) #9

# print(s.index('k')) #ValueError: substring not found
print(s.find('k')) #-1

'''大小写转换方法
    upper() 所有的都转成大写 产生一个新的对象
    lower() 所有的都转小写     ↑
    swapcase() 大小写互换
    capitalize() 第一个转大小，其余转小写
    title() 每个单词第一个转大写，每个单词其余转小写 
'''
print(s,id(s))
a = s.upper()
print(a,id(a))
b = s.lower() #新产生的 地址不同 没驻留
print(b,id(b))
c = s.swapcase()
print(c)
d = s.capitalize()
print(d) #Hello,hello

print(s.title()) #Hello,Hello


'''字符串内容对齐
1 center() 居中对齐，2个参数：指定宽度，指定填充符（默认空格  如果设置的宽度小于原实际宽度就返回原字符串
2 ljsut() 左对齐， 同上↑
3 rjust() 右对齐 ↑
4 zfill() 右对齐，左边用0填充，只接受一个参数，用于指定宽度 ↑
'''
print()
s = "hello,python"
print(s.center(20,'*'))
print(s.center(21,'*'))

print(s.ljust(20,'*'))
print(s.ljust(10,'*')) #返回原字符
print(s.rjust(20,'*'))
print(s.rjust(20))

print(s.zfill(20))
print(s.zfill(10))

print('-8910'.zfill(8)) #-0008910 填到-之后


'''字符串分割
1 split() 从左侧开始分割 默认分隔符为空格 sep参数是指定分隔符 maxsplit指定最大分割次数
2 rsplit() 从右侧开始劈分 ↑
'''
print()
s = 'hello |world ,|Python'
lst=s.split()
print(lst) #['hello', '|world', ',|Python']
lst=s.split(sep=',')
print(lst) #['hello |world ', '|Python']
lst = s.split('|',maxsplit=1)
print(lst) #['hello ', 'world ,|Python']

print(s.rsplit())


'''判断字符串
1 isidentifier() 判断字符串是不是合法的标识符
2 isspace() 判断是否全部由空白字符组成（回车、换行、水平制表符
3 isalpha() 判断字符串是否全部由字母组成
4 isdecimal() 判断字符串是否全部由十进制数字组成
5 isnumeric() 判断字符串是否全部由数字组成
6 isalnum() 判读是否全部由字母和数字组成
'''
print()
s = 'hello,python'
print(s.isidentifier()) #f
print('hello'.isidentifier()) #t
print('张三'.isidentifier()) #t
print('张三_123'.isidentifier()) #t

print('\t'.isspace()) #t
print('abc'.isalpha()) #t
print('张三'.isalpha()) #t
print('张三1'.isalpha()) #f

print('123'.isdecimal()) #t
print('123四'.isdecimal()) #f
print('ⅡⅡ'.isdecimal()) #f

print('123'.isnumeric()) #t
print('123四'.isnumeric()) #t
print('ⅡⅡ'.isnumeric()) #t

print('abc1'.isalnum()) #t
print('张三1'.isalnum()) #t
print('张三1！'.isalnum()) #f