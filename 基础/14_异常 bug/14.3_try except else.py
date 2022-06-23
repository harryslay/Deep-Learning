'''try except else结构'''
try:
    a = int(input("请输入第一个整数"))
    b = int(input("请输入第二个整数"))
    result = a/b
except BaseException as e: #所有可能出现的错误 并报错
    print("出错了",e)
else:

    print('计算结果为：',result)

finally:
    print("无论是否产生异常都会执行的代码")
print("程序结束")
'''
    try expect else finally结构：
    finally最后都会执行，能用来释放try块中申请的资源
    '''