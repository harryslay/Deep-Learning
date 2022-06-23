#只控制本层循环
for i in range(5):
    for j in range(1,11):
        if j%2==0:
            # break
            continue
        print(j,end='\t')
    print()