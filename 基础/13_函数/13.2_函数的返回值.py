# 当函数返回多个值时，结果为元组
'''
    1 如果函数没有返回值【函数执行完毕之后，不需要给调用处提供数据】
      return可以省略不写
    2 如果是1个，直接返回类型
    2 如果是第一份，返回的结果是元组

        函数在定义时，是否需要返回值视情况而定
'''
def fun(num):
    odd=[]; # 存奇数
    even=[]; # 存偶数
    for i in num:
        if i%2:
            odd.append(i)
        else:
            even.append(i)
    return odd,even
lst=[10,29,34,23,44,53,55]
print(fun(lst)) #([29, 23, 53, 55], [10, 34, 44])

def fun1():
    print('hello')
    # return
fun1()

def fun2():
    return 'hello'

res=fun2()
print(res)

def fun3():
    return 'hello','world'

print(fun3()) #('hello', 'world')
