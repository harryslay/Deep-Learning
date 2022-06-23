file = open('a.txt','r')
# print(file.read(4)) # 所有内容
print()
# print(file.readline()) # 读一行
# print(file.readlines()) # ['小天鹅\n', '右下角 convey GBK'] 每一行，全放在一个列表里

file = open('c.txt','a')
# file.write('hellO')
lst =['java','go','python']
# file.writelines(lst) # 将列表中的内容写入文件
file.close()

file = open('c.txt','r')
file.seek(2) #一个中文两个字节 所以从中后面开始读
print(file.read())
print(file.tell())
file.close()