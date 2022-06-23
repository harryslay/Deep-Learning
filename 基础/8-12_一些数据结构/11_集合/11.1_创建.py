'''
集合是没有value的字典 也是【无序的】 可变 集合中的元素不允许重复
'''
'''
创建：
1 {}
'''

s = {2,3,3,5,5,26,7}
print(s) #{2, 3, 5, 7, 26} 自动去重

s1 =set(range(6))  #自动把range中的元素转成集合
print(s1,type(s1)) #{0, 1, 2, 3, 4, 5} <class 'set'>

s2 =set([1,2,3,4,5,5,2,2,7])  #将列表元素转成集合 去重
print(s2,type(s2)) #{1, 2, 3, 4, 5, 7} <class 'set'>

s3 =set((1,3,3,2,4,5,5,32)) #将元组类型转成集合 元素顺序变了：无序的
print(s3,type(s3)) #{32, 1, 2, 3, 4, 5} <class 'set'>

s4 =set('python') #将字符串中的转成集合
print(s4,type(s4)) #{'n', 'p', 't', 'h', 'y', 'o'} <class 'set'>

s5 = set({1,2,3,5,5}) #
print(s5,type(s5)) #{1, 2, 3, 5} <class 'set'>

# 空集合 不能直接使用{} 这样默认是字典 只能使用set()
s6 ={}  #dict
print(type(s6))

s7 =set() #set
print(type(s7))
