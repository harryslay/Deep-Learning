
print("---------else和for一起使用--------")
for i in range(3):
    pwd = input("请输入密码：")
    if pwd == "8888":
        print("密码正确")
        break
    else:
        print("密码不正确")
else:
    print("三次密码均输入错误")


print("---------else和while一起使用--------")
i=0
# while(i<3): 我告诉自己少用括号
while i<3:
    pwd = input("请输入密码：")
    if pwd == "8888":
        print("密码正确")
        break
    else:
        print("密码不正确")
    i+=1
else:
    print("三次密码均输入错误")