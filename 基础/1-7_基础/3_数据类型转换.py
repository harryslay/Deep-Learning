#coding:utf-8
# 中文编码声明注释 指定源码文件的编码格式 另存为可以看到
# 数据类型转换
name='lisa'
age =20
print(type(name),type(age))
print('我叫'+name+'，今年'+str(20)+'岁') #把int转成str类型 不然报错
print(str())

# str()将其他类型转成str类型
a = 10
b = 198.8
c = False
print(type(a),type(b),type(c))
a = str(a) #这样赋值了才会真正的改变原类型
print(str(a),str(b),str(c), type(a),type(b),type(c))

# int()将其他类型转成int
s1='123' #字符串为数字串 可以转
f1 = 91.23 #只截取整数部分
ff = True # 1
s2 = 'hello'
s3 = '12.123' #字符串浮点数不能转
print(type(s1),type(f1),type(ff),type(s2),type(s3))
print(int(f1),type(int(f1))) #小数取整
# print(int(s2),type(int(s2))) #报错 字符串字母不能转
# print(int(s3),type(int(s3))) #报错 字符串浮点数不能转

# float()将其他类型转成float
s1='123' #字符串为数字串 可以转
ff = True # 1
i = 98
s2 = 'hello'
s3 = '12.123' #字符串浮点数不能转
print(float(s1),type(float(s1))) #123.0
print(float(ff),type(float(ff))) #1.0
# print(float(s2),type(float(s2))) #字符串非数字串不能转
print(float(i),type(float(i))) #98.0
print(float(s3),type(float(s3))) #12.123 可以
