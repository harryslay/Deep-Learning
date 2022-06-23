
def fun(a,b):
    c=a+b # c为局部变量 是在函数体内部进行定义的；ab是形参，作用范围也是函数内部，相当于局部变量
    print(c)

# print(c)
# print(a)

name='11' #全局变量 作用范围为函数内部和外部都可以使用
print(name)
def fun2():
    print(name)

fun2()

def fun3():
    global age  # 函数内部定义的变量：局部变量使用global声明 就变成全局变量了
    age=18
    print(age)

fun3()
print(age)