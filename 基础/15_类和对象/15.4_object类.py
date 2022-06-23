'''
内置函数dir()可以查看指定对象所有属性

__str__()方法，用于返回一个对象的描述，对应于内置函数str()经常用于print方法，帮我们查看对象的信息，
所以我们经常会对__str__()进行重写
'''
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age = age
    def __str__(self):
        return '我的名字是{0}，今年{1}岁了'.format(self.name,self.age)
stu = Student("张三",20)
print(dir(stu)) #查看属性
print(stu) #默认调用__str__()这样的方法 我们对他进行了重写变成输出字符串   我的名字是张三，今年20岁了
#<__main__.Student object at 0x0000025CA0EE1C10> 对象的内存地址
print(type(stu)) #<class '__main__.Student'>
# 可以重写str方法 让他输出对象的属性值