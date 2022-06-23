'''
语法规则
                ↓要打开的文件名称  ↓ 默认文本文件中字符的编号格式为gbk
file = open(filename [,mode,encoding])
被创建的文件对象           ↑打开模式默认只读w r

a:以追加模式打开文件 文件存在在文件末尾追加内容
b:以二进制方式打开文件，不能单独使用，需要与其他模式一起使用 rb或wb
文件类型：文本文件 存储的普通文本 Unicode字符集 可以使用记事本打开
二进制文件：把数据内容用字节存储，无法用记事本打开，必须使用专门的软件打开 eg.mp3  jpg  doc文档等
+ 以读写方式打开 不能单独使用，需要与其他模式一起使用 a+
'''

file = open('a.txt','r')
file1 = open('b.txt','w') #如果没有该文件会在当前同级目录下进行创建 然后使用write方法进行内容编写
file1.write('helloworld')
print(file.readlines())
file.close()
file1.close()

src_file = open('图片.png','rb')
target_file = open('copyimg.png','wb')
target_file.write(src_file.read())
src_file.close()
# file1 = open('b.txt','r')