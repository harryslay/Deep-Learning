import traceback

try:
    print("------------")
    print(1/0)
except:
    traceback.print_exc()

    # 手动编写打印异常信息↑
# print(10/0)