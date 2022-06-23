'''
字典是一个无序的列表  与列表一样都是可变的序列  以键值对的方式存储数据

无序：排列 列表第一个放进来的就在第一个位置 而字典不一定
hash(key)=value存储位置 所以不是根据放的顺序【所以必须key是不可变序列 不然不能唯一映射哈希函数

不可变序列：字符串、整数序列  不能进行增删改操作

查找效率高：根据key去找value 的位置
'''

print("------------创建字典")
'''创建
1 使用{}
2 dict()内置函数 使用= 而且前面的key不需要''
'''
score={'张三':100,'lisi':28,'wwu':78}
print(score)
print(type(score))

student=dict(name='jack',age=20)
print(student)

# 空字典
d ={}
print(d)


print("------------获取字典元素")
'''
获取字典中的元素
1 使用[] 
2 使用get()方法

区别在于查找没有的元素 第一种会报错 第二种返回None
'''
print(score['张三'])
# print(score['张2']) # KeyError: '张2'


print(score.get('张三'))
print(score.get('张2')) #None
print(score.get('散散',99)) # 99 是查找‘散散’值不存在时的一个默认值



print("------------key是否存在 :in/not in")
print('张三' in score) #t
print('张三' not in score) #f

print("------------删除指定键值对:del")
print(score)
del score["张三"]
print(score) #{'lisi': 28, 'wwu': 78}

print("------------清空字典：clear()")
score.clear()
print(score) #{}

print("------------新值、修改：直接在后面赋值")
score={'张三':100,'lisi':28,'wwu':78}

score['陈柳']=98 #新增元素
print(score) #{'张三': 100, 'lisi': 28, 'wwu': 78, '陈柳': 98}
score['陈柳']=100 #新增元素
print(score) #{'张三': 100, 'lisi': 28, 'wwu': 78, '陈柳': 100}





