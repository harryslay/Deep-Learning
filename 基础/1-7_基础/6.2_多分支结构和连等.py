print("--------多分支结构:if elif else---------")
score = int(input("请输入一个成绩："))
if score >=90 and score<=100:
    print("A")
elif score >=80 and score <90:
    print('B')
elif score >=70 and score <80:
    print("C")
elif score >=60 and score <70:
    print("D")
elif score >=0 and score <60:
    print("E")
else:
    print("对不起，您的成绩不在有效范围")

print("--------多分支结构中可以使用连等！！！---------")
score = int(input("请输入一个成绩："))
if 90<=score<=100:
    print("A")
elif 80<=score <90:
    print('B')
elif 70<= score <80:
    print("C")
elif 60<= score <70:
    print("D")
elif 0 <= score <60:
    print("E")
else:
    print("对不起，您的成绩不在有效范围")
