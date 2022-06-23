score={'张三':100,'lisi':28,'wwu':78}
'''
item是key 值通过之前两种方法获取
'''
for item in score:
    print(item,score[item],score.get(item))

'''
字典特点：
1 key不允许重复 不然值覆盖
2 元素是无序的
3 key必须是不可变对象
4 可以根据需要动态伸缩
5 会浪费很大内存 空间换时间
'''

d={'name':'张三','name':'lisi'}
print(d) #{'name': 'lisi'} 值覆盖

lst = [10,20,30]
lst.insert(1,100)
print(lst) #[10, 100, 20, 30] 可以在指定位置插入值 但是字典不可
# d={lst:100} #不能用lst可变对象来计算hash 我们之前学的不可变对象有整数和字符串
# TypeError: unhashable type: 'list'