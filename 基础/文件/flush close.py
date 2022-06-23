'''
flush:把缓冲区内容写入文件，但不关闭文件
close:把缓冲区内容写入文件，但同时关闭文件，释放文件对象相关资源
'''

file = open('d.txt','a')
file.write('hello')
file.flush() # 如果在这里就关闭了 就无法继续写代码了
file.write('world')
file.close()