import os
path = os.getcwd()
lst = os.listdir(path)
for filename in lst:
    if filename.endswith('.py'): #endswith以什么结尾
        print(filename)

'''
flush close.py
os path模块.py
os模块.py
上下文管理器with.py
文件对象常用方法.py
案例.py
读写文件.py

'''
print("-----------案例2")
path2 = "D:\Yingyong\PyCharm Community Edition 2021.2.1\pythonProject\基础\8-12_一些数据结构"
print()
lst_files = os.walk(path2)
'''
walk 可以遍历指定目录下所有的文件和目录 
 '''
# print(lst_files) # 迭代器对象
for dirpath,dirname,filename in lst_files:
    # print(dirpath)
    # print(dirname)
    # print(filename)
    # print("--------------")

    for dir in dirname:
        print(os.path.join(dirpath,dir))
    for file in filename:
        print(os.path.join(dirpath,file))
    print("--------------------")
