import math

print(id(math))
print(type(math))
print(math)
print(math.pi)
print()
print(dir(math))
print(math.pow(2,3),type(math.pow(2,3)))
print(math.ceil(9.8)) #向上取整
print(math.floor(9.8)) # 向下取整

print()
# 自定义模块
import mod
print(mod.add(10, 20)) # 右键mark directory as source root

import calc2
print(calc2.add(100, 200))

'''
在导入含有包的模块时注意事项

使用import方式进行导入时只能跟包名或者模块名
from xx import xx 可以导入包、函数、模块
'''
print()
import pkg1.moduleA as A
print(A.a)