# 变量的赋值操作

class CPU:
    pass
class Disk:
    pass
class Computer:
    def __init__(self,cpu,disk):
        self.cpu = cpu
        self.disk = disk

cpu1 = CPU()
cpu2 = cpu1
'''
只要是对象就由三部分组成 id（地址） type和value


类对象的赋值操作
浅拷贝：python拷贝一般都是浅拷贝【源对象与拷贝对象会引用同一个子对象 比如这里cpu和dick指向都是相同的   
    使用copy模块的copy函数
深拷贝：使用copy模块的deepcopy函数，递归拷贝对象中包含的子对象，源对象和拷贝对象所有的子对象也不相同【都不同 
'''
print(cpu1,id(cpu1)) # 地址相同 相同的对象放在了两个变量中存储 指向同一个对象
print(cpu2,id(cpu2))

print("---------------浅拷贝：")
disk = Disk() #创建一个硬盘对象
computer=Computer(cpu1,disk) #创建一个计算机对象

import copy
computer2 = copy.copy(computer)
print(computer,computer.cpu,computer.disk) #cpu和disk的地址相同 computer地址不同
print(computer2,computer2.cpu,computer2.disk)

print("----------------深拷贝：")
computer3 = copy.deepcopy(computer)
print(computer,computer.cpu,computer.disk) #所有地址都不同了
print(computer3,computer3.cpu,computer3.disk)