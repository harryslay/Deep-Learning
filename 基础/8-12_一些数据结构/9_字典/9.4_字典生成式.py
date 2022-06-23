
# 内置函数zip()
items = ['fruits','books','others']
prices=[90,28,41,11,13] #长度不匹配，自动忽略

#     key:value         ↓变量名           ↓从哪里找
d = {item:price  for item,price in zip (items,prices)}
print(d) #{'fruits': 90, 'books': 28, 'others': 41}
#         ↓可以转大写              ↓变量名           ↓从哪里找
d = {item.upper():price  for item,price in zip (items,prices)}
print(d) #{'FRUITS': 90, 'BOOKS': 28, 'OTHERS': 41}


'''
zip打包过程中 会以少的那个进行生成
'''