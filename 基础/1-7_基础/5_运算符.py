print("-------算术运算符-------")
print(1+1)  # 加法运算 2
print(1-1)  #  减法 0
print(2*1)  #  乘 2
print(11/2)  #  除 5.5
print(11//2)  #  整除运算 5
print(11%2)  #  取余 1
print(2**2)  #  2的2次方 4
print(2**3)  #  2的3次方 8

print("------注意一正一负的整除、取余运算------")
# 一正一负的整除 向下取整
print(9//4) # 2
print(-9//-4) # 2
print(9//-4) # -3 向下取整
print(-9//4) # -3
# 一正一负取余：公式：余数=被除数-除数*商
print(9%-4) # -3  9-（-4）*（-3） 9-12=-3
print(-9%4) # 3  -9-4*（-3） -9+12=3

print("-------赋值运算符、链式赋值-------")
# 赋值运算符 运算从右往左
i=3+4
print(i)
a=b=c=20 #链式赋值 值和地址都相同
print(a,id(a)) #地址
print(a,id(b))
print(a,id(c))
# 参数赋值
a=20
a+=30
print(a)
a-=10
print(a)
a*=2
print(a,type(a)) #int
a/=3
print(a,type(a)) #float
a//=2
print(a,type(a)) #float
a%=3
print(a)
# 序列解包赋值 左右变量和值个数必须对应
print("------支持序列解包赋值------")
a,b,c =20,30,40
print(a,b,c)
# 交换两个变量的值
a,b =10,20
print("交换之前：",a,b)
a,b = b,a
print("交换之后：",a,b)

print("---------比较运算符--------")
a,b =10,20
print('a>b吗？',a>b) # False
print('a<b吗？',a<b) #True
print('a>=b吗？',a>=b) # False
print('a<=b吗？',a<=b) #True
print('a==b吗？',a==b) # False
print('a!=b吗？',a!=b) #True
'''
=:赋值运算符
==:比较运算符
一个变量由三部分组成:标识、类型、值
==比较的是值 比较对象的标识使用is
'''
print("--相同值的变量指向同一内存空间--")
a=10
b=10
print(a==b) #t 存储的值和标识都相等
print(a is b) #t
print("--相同值列表不指向相同内存空间--")
lst1 =[11,22,33,44]
lst2 =[11,22,33,44]
print(lst1==lst2) #value True
print(lst1 is lst2) #id   False
print(id(lst1),id(lst2))
print(a is not b) # True id不相等？ 相等
print(lst1 is not lst2) #True id不相等？ 不相等

print("-------布尔运算符:and、or、not、in、not in-------")
a,b =1,2
print(a==1 and b==2) #True
print(a==1 and b<2) #False
print(a!=1 and b==2) #False
print(a!=1 or b==2) #True
f = True
f2 =False
print(not f) # False
print(not f2) # True
s="helloworld"
print('w' in s) #True
print('w' not in s) #False
print('k' not in s) #True
print("---------位运算符 &、|、<<、>>---------")
print(4&8) # 0  按位与 全1出1
print(4|8) # 12 按位或 有1出1
print(4<<1) # 8 高位溢出，低位补零 左移1位相当于*2
print(4>>2) # 1 高位补零，低位截断 右移1位相当于/2
print("--------运算符法则--------")
print("0 有括号先算括号")
print("1 算术运算：先乘除 后加减 有幂运算先算幂")
print("2 位运算 &、|、<<、>>")
print("3 比较运算")
print("4 布尔运算")
print("5 赋值运算")
