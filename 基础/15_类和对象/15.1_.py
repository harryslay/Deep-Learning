'''
面向过程、面向对象

类：
 数据类型：
 不同的数据类型属于不同的类 使用内置函数type()查看数据类型
类的组成：
 类属性 类中方法歪的变量称为类属性，被该类所有对象所共享
 实例方法  使用@classmethod修饰的方法，使用类名直接访问的方法
 静态方法 使用@staticmethod修饰的 使用类名直接访问的方法
 类方法

python中一切皆对象
'''

class Student: #类名：一个或者多个单词组成，大驼峰

    native_pace="吉林"  # 直接写在类里的变量称为属性

    def __init__(self,name,age):
        self.name = name #self.name称为实例属性，进行了一个赋值的操作，将局部变量的name的值赋给实例属性
        self.age = age
    # 实例方法 【在类之外定义的称为函数 在类之内定义的称为方法
    def eat(self):
        print("学生在吃饭")
    # 静态方法
    @staticmethod
    def method():
        print("我使用staticmethod进行修饰，是静态方法（里面不能写self 是规定")

    # 类方法
    @classmethod
    def cm(cls):
        print("使用classmethod修饰，是类方法（里面写cls")
# 有id 值  内存开空间了 是一个class对象

def drink ():
    print("喝水") # 函数


stu1 = Student('张三',20)
print(id(stu1)) # 实例对象
print(type(stu1))
print(stu1)

print(id(Student))
print(type(Student))
print(Student)

print(stu1.name)
stu1.eat() # 调用类中方法的两种形式 ↓ 对象名.方法名（）
Student.eat(stu1) # 类名.方法名（类的对象）

print()
# 类属性的使用方式
print(Student.native_pace) #吉林
stu1 = Student("张三",20)
stu2 = Student("李四",30)
print(stu1.native_pace)
print(stu2.native_pace)
Student.native_pace='天津'
print(stu1.native_pace) #天津
print(stu2.native_pace)

#
print("----------------类方法使用方式")
Student.cm()
# 
print("----------------静态方法使用方式")
Student.method()