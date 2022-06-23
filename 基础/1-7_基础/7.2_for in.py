# 字符串是一个可迭代对象
for item in 'Python':
    print(item)
#range()产生的整数序列也是一个可迭代对象
print("------range--------")
for i in range(10):
    print(i)

print("如果循环体中不需要自定义变量，可以将变量定义为_")
for _ in range(5):
    print('人生苦短，我用python')

# 1-100偶数和
sum=0
for i in range(101):
    if not bool(i%2):
        sum+=i
    i+=1
print("1-100偶数和为：",sum)