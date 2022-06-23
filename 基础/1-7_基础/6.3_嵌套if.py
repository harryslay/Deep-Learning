print("--------嵌套if---------")
'''
    会员>=200 8折
        >=100 9折
        不打折
    非会员 >=200 9.5折
        不打折
'''
while(1):
    answer = input("您是会员吗？y/n")
    money = float(input("请输入您的购物金额:"))
    if answer == 'y':
        if money >= 200:
            print("付款金额为：",money*0.8)
        elif money >=100:
            print("付款金额为：",money*0.9)
        else:
            print("付款金额为：",money)
    else:
        if money >= 200:
            print("付款金额为：",money*0.95)
        else:
            print("付款金额为：",money)

