
'''
缺点：占用内存多，效率低下
优点：代码和思路简单

递归调用过程：每递归调用一个函数，都会在栈内存分配一个栈帧
           每执行完一次函数都会释放相应空间
'''
def fac(x):
    if x==1:
        return 1
    else:
        return x*fac(x-1)

print(fac(6)) #720

# 斐波那契数列
def febo(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return febo(n-1)+febo(n-2)

print(febo(6))

for i in range(1,7):
    print(febo(i))