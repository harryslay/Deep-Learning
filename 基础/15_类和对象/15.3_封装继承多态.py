# 面向对象的三大特征
'''
封装：提高程序的安全性 如果该属性不希望在类对象外部被访问，前面使用两个_
继承：提高代码的复用性 支持多继承，class 子类类名（父类1，父类2 ...)：  如果没继承默认继承object 定义子类时必须在其构造函数中调用父类的构造函数
                    pass
'''

class Car:
     def __init__(self,brand,age):
         self.brand = brand
         self.__age=age
     def start(self):
        print("汽车已启动")
     def show(self):
         print(self.__age)

car=Car('宝马',20)
car.start()
print(car.brand)

car.show()
# print(car.__age)
# 不希望使用但是可以使用

# print(dir(car)) #查看所有属性
print(car._Car__age) #在类的外部可以通过_Car__age进行访问

print("---------------继承 方法重写")
class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info(self):
        print(self.name,self.age)

class Student(Person):
    def __init__(self,name,age,stu_no): #初始化方法中要调用父类的初始化方法
        super().__init__(name,age) #super调用父类的初始化方法
        self.stu_no=stu_no
    def info(self): #方法重写 如果父类也要输出 可以调用父类的方法 使用super().方法名()
        super().info()
        print(self.stu_no)

class Teacher (Person):
    def __init__(self,name,age,te_year):
        super().__init__(name,age)
        self.te_year=te_year
    def info(self):
        super(Teacher, self).info() # 两个参数 默认的
        print(self.te_year)

stu = Student("张三",20,'1001')
teacher = Teacher("ee",22,1)

stu.info() #张三 20
teacher.info() #ee 22


print("------------多继承")
class L():
    pass

class S():
    pass

class Circle(L,S): #继承自AB
    pass


print("------------多态")
class Animal:
    def eat(self):
        print("动物要吃东西")

class Dog(Animal):
    def eat(self):
        print("狗吃肉")

class Cat(Animal):
    def eat(self):
        print("猫吃鱼")

class Person(Animal):
    def eat(self):
        print("人吃五谷杂粮")
# 定义一个函数 传入对象 调用对象的eat方法
def fun(obj):
    obj.eat()

cat = Cat()
dog = Dog()
person = Person()

fun(cat)
fun(Dog()) #可以直接这样创建对象（不用变量接收
fun(person)
'''
静态语言和动态语言
java   python
静态语言实现多态的三个必要条件：继承、方法重写、父类引用指向子类对象
动态语言：只关心对象的行为
'''