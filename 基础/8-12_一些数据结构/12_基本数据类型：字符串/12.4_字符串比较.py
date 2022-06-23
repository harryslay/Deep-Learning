
'''
字符串比较:比较多是原始值：ordinary value
ord() 函数可以查看
chr()内置函数 可以得到其对应的字符
'''
print('apple'>'app') #t
print('apple'>'banana') #f
print(ord('a'),ord('b')) #97 98
print(ord('杨')) #26472

print(chr(97),chr(98)) #a b
print(chr(26472)) #杨

'''
is 和==的区别
is比较的是id（地址  ==比较的是值value
'''
a=b='python'
c = 'python'
print(a==b) # t
print(c==b) # t
print(id(a),id(b),id(c)) #相等