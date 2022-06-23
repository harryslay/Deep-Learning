'''
特殊属性：__dict__获得类对象或实例对象所绑定的所有属性和方法的字典
特殊方法
    __len__() 通过重新这个方法让内置函数len()的参数可以是自定义类型
    __add__()              让自定义对象具有+功能
    __new__()  用于创建对象
    __init__() 用于对象初始化

'''

print(dir(object))

print()
class A:
    pass
class B:
    pass
class C(A,B):
    def __init__(self,name,age):
        self.name = name
        self.age = age

class D(A):
    pass
x = C('jack',30)
print('----------------特殊属性')
print(x.__dict__) #{'name': 'jack', 'age': 30} 看到实例对象的属性字典
print(C.__dict__) #{'__module__': '__main__', '__init__': <function C.__init__ at 0x00000263C9C6B5E0>, '__doc__': None} 类对象

print(x.__class__) # 输出对象所属的类
print(C.__bases__) # 输出C类的父类类型的元组 (<class '__main__.A'>, <class '__main__.B'>)
print(C.__base__) # 跟他离的最近的父类（谁写在前面输出谁  <class '__main__.A'>
print(C.__mro__) # 类的层次结构 继承了xx
print(A.__subclasses__()) # 子类的【列表】  [<class '__main__.C'>, <class '__main__.D'>]

print()
print("----------------特殊方法")

a = 20
b = 1000
c = a+b
d = a.__add__(b)

print(c)
print(d)

class Student:
    def __init__(self,name):
        self.name=name
    def __add__(self, other):
        return self.name+other.name
    def __len__(self):
        return len(self.name)

stu1 = Student("jack")
stu2 = Student("李四")

s = stu1+stu2 # 不能直接相加 但是可以通过改写__add__()方法
print(s)
s = stu2.__add__(stu1)
print(s)

print()
lst = [11,22,33,44]
print(len(lst)) # 内置函数 输出对象长度
print(lst.__len__())

print(len(stu2)) #2 name的长度