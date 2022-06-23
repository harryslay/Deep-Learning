print("--------index()--------")
# n个相同元素 只返回第一个元素的索引
lst = ['hello','world',98,'hello']
print(lst.index('hello'))
# 查询的元素不存在 报ValueError错误
# print(lst.index('he'))
#可以在一个指定对范围内查找 内容后面加start和stop两个参数
print(lst.index('hello',1,4))

print("--------获取列表中的单个元素--------")
'''
正向：0 ~ n-1
逆向：-n ~ -1
不存在 报IndexError
'''
print(lst[2]) #98
print(lst[-3]) #world
# print(lst[10]) #报错IndexError: list index out of range
