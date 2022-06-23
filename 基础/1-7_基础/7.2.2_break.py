# for in与break搭配
for i in range(3):
    pwd = int(input("请输入密码："))
    if pwd == 8888:
        print("密码正确")
        break
    else:
        print("密码不正确")

# while
i=3
while(i):
    pwd = int(input("请输入密码："))
    if pwd == 8888:
        print("密码正确")
        break
    else:
        print("密码不正确")
    i-=1