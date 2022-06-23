'''
1-50之间所有5的倍数
'''
for i in range(1,51):
    if not bool(i%5):
        print(i)
        continue