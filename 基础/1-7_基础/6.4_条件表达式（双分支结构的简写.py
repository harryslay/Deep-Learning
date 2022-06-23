'''
从键盘输入两个整数，比较大小
'''
num_a = int(input("输入第一个整数"))
num_b = int(input("输入第二个整数"))
if num_a>=num_b:
    print(num_a,"大于等于",num_b)
else:
    print(num_a,"小于",num_b)

print("-------使用条件表达式进行比较--------")
'''
条件表达式的格式：x if 判断条件 else Y
 如果判断条件为t 返回x 否则返回y
'''
print(str(num_a)+"大于等于"+str(num_b) if num_a>=num_b else str(num_a)+"小于"+str(num_b))