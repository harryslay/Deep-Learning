'''
删除5种
    remove() 一次删除一个元素 重复元素只删除第一个 元素不存在报ValueError
    pop() 删除一个指定索引位置上的元素，指定索引不存在报IndexError 不指定索引删除列表中最后一个元素
    切片 一次至少删除一个元素
    clear() 请空列表
    del 删除列表

'''
print("--------remove()")
lst= [10,20,30,40,50,60,30]
lst.remove(30) #重复元素只移除第一个(20后面那个
print(lst) #[10, 20, 40, 50, 60, 30]
# lst.remove(100) #ValueError: list.remove(x): x not in list

print("--------pop()")
lst.pop(1) #删除索引为1 的元素
print(lst) #[10, 40, 50, 60, 30]
# lst.pop(5) #IndexError: pop index out of range
lst.pop()
print(lst) #[10, 40, 50, 60] 不传参删最后一个

print("-----------切片，删除至少一个元素，但是会产生新的列表对象")
new_list = lst[1:3]
print("原列表",lst) #10, 40, 50, 60]
print("切片产生的新列表",new_list) #[40, 50]
'''
不产生新列表对象，删除原列表中的内容的切片方法：
'''
lst[1:3]=[] #使用空列表进行替代了 不是真正的删除
print(lst) #[10, 60]

print("------clear()")
lst.clear() #清空
print(lst) #[]

print("------del")
del lst #删除列表 列表不存在了
# print(lst) #NameError: name 'lst' is not defined
