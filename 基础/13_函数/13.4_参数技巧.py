def fun(a,b,c):
    print('a=',a)
    print('b=',b)
    print('c=',c)

fun(10,20,30)
lst=[11,22,33]
# fun(lst) # 报错 只传了一个参数lst 列表类型
fun(*lst) # 在函数调用时，将【8_列表】中的每个【元素】都转换为【位置实参】传入

fun(a=100,c=200,b=300)
dict= {'a':111,'b':222,'c':333}
# fun(dict) # 报错 字典只是一个参数
fun(**dict) # 在函数调用时，将【字典】中的每个【键值对】都转换为【关键字实参】传入

# 顺序问题 还可以
def fun5(a,b,*,c,d,**agrs):
    pass