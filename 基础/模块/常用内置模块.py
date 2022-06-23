'''
sys
time
os
calendar
urllib 用来获取网上的数据标准库
json 用于使用JSON序列化和反序列化对象
re 用来在字符串上执行正则表达式匹配和替换
math
decimal 控制精度、有效数位、四舍五入的十进制运算
logging 提供了灵活的记录事件、错误、警告和调试信息等日志信息的功能

'''
import sys
import time
import urllib.request
import schedule

def job():
    print('哈哈------')

schedule.every(3).seconds.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)

print(sys.getsizeof(24)) #28 整数占28字节
print(sys.getsizeof(246)) #28
print(sys.getsizeof(True)) #28
print(sys.getsizeof(False)) #24

print(urllib.request.urlopen('http://www.baidu.com').read())

print(time.time()) #秒
print(time.localtime(time.time())) #把秒转为了具体的哪一天