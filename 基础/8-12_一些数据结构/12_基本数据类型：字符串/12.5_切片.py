'''
与列表切片都会产生新对象
但是字符串不可变 不具备增删改
'''

s = 'hello,python'
s1 = s[:5] #hello start不指定 从0开始切到5(不包括5
s2 = s[6:] #python stop不指定 到最后
s3 = '!'
newstr = s1+s3+s2

print(s1)
print(s2)
print(newstr)

print()  #以下五个都是新的字符串
print(id(s))
print(id(s1))
print(id(s2))
print(id(s3))
print(id(newstr))

print("-------------切片[start:end:step]-------------")
print(s[1:5:1]) #ello
print(s[::2]) #hlopto
print(s[::-1]) #nohtyp,olleh  步长为负值 默认从字符串最后一个元素开始到第一个结束
print(s[-6::1]) #python 从小的数开始 到大的数
