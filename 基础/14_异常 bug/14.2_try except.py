try:
    a=int(input("请输入一个整数:")) #别忘了input接收的是字符串 要转化成int
    b=int(input("请输入一个整数:"))
    res=a/b
    print("除法结果为：",res)
except ZeroDivisionError: # 出现的异常和捕获的异常不一致：多个except结构
    print("除数不能为0")
except ValueError:
    print("只能输入数字串")
print("程序结束")

