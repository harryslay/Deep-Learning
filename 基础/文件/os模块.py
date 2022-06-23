
import os
# os.system("notepad.exe")
# os.system("calc.exe")


# 直接调用可执行文件
# os.startfile('D:\\Program Files\\Tencent\\QQ\\Bin\\QQ.exe')


'''
os模块常用函数
getcwd() 返回房钱的工作目录
listdir(path) 返回指定路径下的文件和目录信息
mkdir(path[,mode]) 创建目录    【[]表示可有可无（编译原理学的！
makedirs(path1/path2...[,mode]) 创建多级目录
rmdir(path) 删除目录
removedirs(path1/path2......) 删除多级目录
chdir(path) 将path设置成当前工作目录

'''
print(os.getcwd()) #D:\Yingyong\PyCharm Community Edition 2021.2.1\pythonProject\基础\文件

lst=os.listdir('../文件')
print(lst)
# os.mkdir('newdir2')
# os.makedirs('newdir3/3/4')
# os.rmdir('newdir2')
# os.removedirs('newdir3/3/4')

# os.chdir('')