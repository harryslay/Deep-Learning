'''
排序
1 sort()方法，列表中的所有元素默认按从小到大排，可以指定reverse=True降序  在原列表上排序 不会产生新对象   (reverse默认是false
2 使用内置函数sorted()，可以指定reverse=True进行降序排序，原列表顺序不发生改变，产生新的排好序的对象

'''
lst = [10,3,42,14,24,233]
print("原列表",lst,id(lst))
print("------------sort()")
lst.sort()
print("排序后",lst,id(lst)) #[3, 10, 14, 24, 42, 233]
lst.sort(reverse=True)
print("降序排序",lst) #[233, 42, 24, 14, 10, 3]


print("-----------内置函数sorted() 会产生一个新的列表对象")
lst = [10,3,42,14,24,233]
print("原列表",lst,id(lst))

new_list = sorted(lst)
print(lst) #[10, 3, 42, 14, 24, 233]
print(new_list) #[3, 10, 14, 24, 42, 233]
# 指定关键字 降序
desc_lst=sorted(lst,reverse=True)
print(desc_lst) #[233, 42, 24, 14, 10, 3]