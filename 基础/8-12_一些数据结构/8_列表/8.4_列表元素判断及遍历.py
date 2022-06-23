# 字符串和列表都是可迭代的变量
print('p' in 'python') #t
print('p' not in 'python') #f

lst=[10,20,'python','hello']
print(10 in lst) #t
print(10 not in lst) #f
print(100 not in lst) #t

print("------遍历-----")
for i in lst:
    print(i)