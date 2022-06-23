print("---------添加元素---------")
'''
添加操作：
 append() 没有创建新的列表对象 在列表末尾添加一个元素
 extend() 在列表末尾至少添加一个元素
 insert() 在列表的任意位置添加第一个元素
 切片 在列表的任意位置至少添加一个元素
'''
print('----------->append()')
lst = [10,20,30]
print("添加之前",lst,id(lst))
lst.append(100)
print("添加之后",lst,id(lst)) # id不变 没有创建新的列表对象

lst2 = ['hello','node']
lst.append(lst2)
print(lst) #[10, 20, 30, 100, ['hello', 'node']]  把整个列表作为一个元素添加了

print('----------->extend()')
lst.extend(lst2)
print(lst) #[10, 20, 30, 100, ['hello', 'node'], 'hello', 'node']

print('----------->insert()')
lst.insert(1,90) #在第一个位置上插入90
print(lst) #[10, 90, 20, 30, 100, ['hello', 'node'], 'hello', 'node']

print('----------->()')
lst3=[True,False,'hello']
lst4 =[111]
lst[1::]=lst3 #从1 开始 把后面全都切掉了
print(lst) #[10, True, False, 'hello']
lst[1:1:]=lst4 # 从1 到1  就是在1的位置添加了 后面的不切
print(lst) #[10, True, False, 'hello', True, False, 'hello']
