# 变量存储的是一个对象的引用 （id值 指向该存储空间
a=10
lst = ['hello','world',98] #列表存的是多个对象的引用 然后又赋值给了一个变量 所以lst中存的是列表这个对象的引用（套娃 三层
print(id(lst))
print(type(lst))
print(lst)

print("--------列表的创建的两种方式-------")
# 1 使用[]
lst = ['122','hello',18]
# 2 使用内置函数list()
lst2 = list(['hello','123',13,'hello'])

print("-------列表特点：")
# 1 顺序性 列表从0开始 如果从后往前：负数 从-1开始
# 2 索引映射唯一数据
print(lst[0],lst[-3])
# 3 可以存储重复数据
print(lst2)
print(lst2[0],lst2[-4])
# 4 任意数据类型混存
# 5 根据需要动态分配和回收内存