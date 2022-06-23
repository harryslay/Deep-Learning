a = 1
#判断次数比执行次数多1
while a<10:
    print(a)
    a+=1

    '''
    1 初始化变量 
    2 条件判断
    3 条件循环体
    4 改变变量
    '''
print("-------1-5累加和-------")
a = 0
sum=0
while a<5:
    sum+=a;
    a+=1;
print(sum) #10

print("------1-100偶数和------")
a=0
sum=0
while a<=100:
    # if a%2==0:
    if not bool(a%2): #可以直接用a%2这个表达式 此时是奇数和 取反要用bool
        sum+=a
    a+=1 #python中没有a++
print(sum) #2550