# range()内置函数 用于生成一个整数序列 返回值是一个迭代器对象
'''
优点：不管range对象表示的整数序列有多长，所有range对象占用的内存空间都是相同的，因为只存储start、step和stop 只有用到这个对象时才回去计算序列中的相关元素
使用in 和not in判断整数序列中是否存在指定整数
'''
# range（）的三种创建方式
# 第一种 ：只有一个参数
r = range(10)
print(r) #range(0,10)
print(list(r)) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 用于查看range对象中的整数序列 默认从0开始 步长为1
# 第二种：给两个参数 开始和结束
r = range(1,10) #1开始 10结束（不包括10
print(list(r)) #[1, 2, 3, 4, 5, 6, 7, 8, 9]
# 第三种：三个参数
r = range(1,10,2) #步长2
print(list(r)) # [1, 3, 5, 7, 9]
# 判断指定整数在序列中是否存在 in,not in
print(10 in r) #f
print(9 in r) #t
print(9 not in r) #f

print(range(1,20,1))
print(range(1,100,1))