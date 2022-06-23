
'''
元组的创建方式
1 () 如果只有一个元素，逗号不能省
2 内置函数tuple()
'''
t = ('Python','world',78)
print(t,type(t))
# 元组的（）可以不写 省略
t2 = 'python','11',1
print(t2,type(t2)) #('python', '11', 1) <class 'tuple'>

print("----------元组中只包含一个元素必须使用（）和， 不然会当成本身的数字类型【int或者字符串----------")
t3 = ('python')
print(t3,type(t3)) #python <class 'str'>
t3 =('python' ,)
print(t3,type(t3)) #('python',) <class 'tuple'>

t1 = tuple(('Python','hello',210))
print(t1,type(t1))

# 空列表 空字典 空元组
lst=[]
lst1 = list()
print("空列表",lst,lst1) #[] []

d={}
d1 = dict()
print("空字典",d,d1) #{} {}

t4 =()
t5 = tuple()
print("空元组",t4,t5) #() ()