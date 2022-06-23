'''
将元组设计成不可变序列：多任务环境下同时操作对象不需要加锁
元组中存储的是对象的引用，如果元组中对象本身不可变对象，则不能引用其他对象
                    如果元组中的对象本事是可变队形，则可变对象的引用不允许改变，但数据可以改变

'''
t=(10,[20,30],9)
print(t)
print(type(t),id(t)) #<class 'tuple'> 2785517550016
print(t[0],type(t[0]),id(t[0])) #10 <class 'int'> 140705934616656
print(t[1],type(t[1]),id(t[1])) #[20, 30] <class 'list'> 2901250409088
print(t[2],type(t[2]),id(t[2])) #9 <class 'int'> 140705934616624

# 将t1指向100
print(id(100))
# t[1]=100 #TypeError: 'tuple' object does not support item assignment
t[1].append(100)
print(t,id(t[1])) #(10, [20, 30, 100], 9) 1812974535296