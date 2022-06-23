
'''替换
replace() 第一个参数指定被替换的子串，第二个指定替换的子串，第三参数指定最大替换次数  返回替换后得到的字符串，替换前的字符串不发生变化
'''
s = 'hello,Python'
print(s.replace('Python','Java'))
s1 = 'hello,Python,Python,Python' #hello,Java
print(s1.replace('Python','Java',2)) #hello,Java,Java,Python

'''字符串的合并
    join():将列表或元组中的字符串合并成一个字符串
'''
lst=['hello','java','python'] #列表中的字符串可以合并
print('|'.join(lst)) #hello|java|python
print("".join(lst)) #hellojavapython

t=('hello','java','python') #元组中的也可以合并
print("".join(t))

print("*".join('Python')) #把他当成一个字符串序列  P*y*t*h*o*n
