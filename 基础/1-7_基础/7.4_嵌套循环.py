'''
打印一个三行四列的矩形
'''

for i in range(3):
    for j in range(4):
        print('*',end=' ') #默认换行 所以要加终止条件 end='你想在后面加的 空格或者\t'
    print() #默认换行

'''
九九乘法表
'''
for i in range(1,10):
    for j in range(1,i+1):
        # print(f'{i}*{j}={i*j}',end="\t")
        print(i,'*',j,'=',i*j,end="\t") #直接使用，连接
    print()
