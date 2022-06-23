'''
abspath(path) 获取文件或目录的绝对路径
exists(path) 判断文件或目录是否存在，存在返回True，否则返回False
join(path,name) 将目录与目录或文件名拼接起来
splitext() 分类文件名和扩展名
basename(path) 从一个目录中提取文件名
dirname(path) 从一个路径中提取文件路径，不包括文件名
isdir(path) 判断是否为路径

'''
import os.path
print(os.path.abspath('os path模块.py')) # 绝对路径

print(os.path.exists('123.py'),os.path.exists('c.txt')) #f t
print(os.path.join('D:\\Python','a.txt')) # 拼接
print(os.path.split("D:\\Yingyong\\PyCharm Community Edition 2021.2.1\\pythonProject\\基础\\文件\\a.txt")) # 将路径和扩展名拆分
print(os.path.splitext('a.txt')) # 拆分文件与后缀名
print(os.path.basename("D:\\Yingyong\\PyCharm Community Edition 2021.2.1\\pythonProject\\基础\\文件\\a.txt")) # 提取文件名
print(os.path.dirname("D:\\Yingyong\\PyCharm Community Edition 2021.2.1\\pythonProject\\基础\\文件\\a.txt")) # 提取路径名
print(os.path.isdir("D:\\Yingyong\\PyCharm Community Edition 2021.2.1\\pythonProject\\基础\\文件\\a.txt")) # 是否是目录 不是因为后面有文件
print(os.path.isdir("D:\\Yingyong\\PyCharm Community Edition 2021.2.1\\pythonProject\\基础\\文件")) # 是

