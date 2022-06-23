# 输入函数input 存到变量中
present = input('提示语，输入之前你会看到这段话：')
print(present,type(present))

# 从键盘输入两个整数，计算两个整数的和
a = input('请输入一个加数：')
b = input('请输入另一个加数：')
print(type(a),type(b))
print(a+b) # 直接输出是字符串连接 读取的数都是str类型
a = int(a)
b = int(b)
print(a+b)
# 或者直接输入时转换:
a = int(input('输入加数:'))
b = int(input('输入另一加数:'))
print(a+b)