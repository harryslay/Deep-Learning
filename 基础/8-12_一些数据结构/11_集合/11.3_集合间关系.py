'''两个集合是否相等 元素相等就相等'''
# 无序的 所以相等
s={10,20,30,40}
s2={20,10,30,40}
print(s==s2) #t
print(s!=s2) #f

'''一个集合是否为另一个集合的子集 使用.issubset()函数'''
s3 ={10,20}
s4={10,90}
print(s3.issubset(s)) #t
print(s4.issubset(s)) #f

'''一个集合是否为另一个集合的超集 使用.issuperset()函数'''
print(s.issuperset(s3)) #t
print(s.issuperset(s4)) #f

'''两个集合是否有交集'''
s4={100,200,300}
print(s2.isdisjoint(s3)) #f 有交集为f
print(s4.isdisjoint(s3)) #t 没有交集为t