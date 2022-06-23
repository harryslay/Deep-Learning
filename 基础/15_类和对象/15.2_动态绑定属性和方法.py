
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def eat(self):
        print(self.name+'在吃饭')

stu1 = Student('张三',20)
stu2 = Student('李四',30)
print(id(stu1))
print(id(stu2))

print("为stu2动态绑定性别属性")
stu2.gender="女"
print(stu1.name,stu1.age) #张三 20
print(stu2.name,stu2.age,stu2.gender) #李四 30 女

print("---------------")
stu1.eat()
stu2.eat()

def show():
    print("定义在类之外，称为函数")
# stu1.show=show() #只写名 不执行 如果执行就是定义时直接使用了 不能再使用()调用 【或者上面写()  把他当做一个属性来调用？调用时不需要（）
# stu1.show
stu1.show=show #只写名 不执行 如果执行就是定义时直接使用了 不能再使用()调用 【或者上面写()  把他当做一个属性来调用？调用时不需要（）
stu1.show()