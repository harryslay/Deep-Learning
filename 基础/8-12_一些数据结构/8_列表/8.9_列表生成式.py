'''
列表生成式：生成列表的公式
[表示列表元素的表达式 for i in range(1,10)]
                      ↑自定义变量  ↑可迭代对象
'''
lst = [i for i in range(1,10)]
print(lst) #[1, 2, 3, 4, 5, 6, 7, 8, 9]
lst = [i*i for i in range(1,10)]
print(lst) #[1, 4, 9, 16, 25, 36, 49, 64, 81]

# 生成2 4 6 8 10
lst1 = [i*2 for i in range(1,6)]
print(lst1) #[2, 4, 6, 8, 10]