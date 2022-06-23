'''
函数的创建和调用
 代码复用
 隐藏实现细节
 提高可维护性
 提高可读性 便于调试

 def 函数名(输入参数):
    函数体
    return

参数：实参和形参
    位置实参（位置相互对应
    关键字实参（根据关键字名称
'''

def calc(a,b): #形式参数 形参 在函数的定义处
    c=a+b
    return c

res = calc(10,20) #实际参数的值 实参 在函数的调用处
res2 = calc(b=10,a=20) #实际参数的值 实参 在函数的调用处
print(res) #30
print(res2) #30


def fun(arg1,arg2):
    print('arg1',arg1)
    print('arg2',arg2)
    arg1=100
    arg2.append(10)
    print('arg1',arg1)
    print('arg2',arg2)
    # return 不写是因为没有返回值

n1=11
n2 = [22,33,44]
print('n1',n1)
print('n2',n2)
fun(n1,n2)
print('n1',n1) #n1 11
print('n2',n2) #n2 [22, 33, 44, 10]
'''
在函数调用过程中，进行参数的传递
如果是不可变对象，函数体的修改不会影响实参的值
如果是可变对象，函数体的修改会影响实参的值

在函数运行过程中 arg1修改为100不会影响n1的值
              arg2 的修改会影响到n2 的值
'''