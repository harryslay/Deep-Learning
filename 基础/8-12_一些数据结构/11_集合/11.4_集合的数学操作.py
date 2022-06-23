
'''
1 交集 .intersection()函数 或者 &
2 并集 .union()与 | 等价
3 差集 .difference() 与 -等价
4 对称差集 .symmetric_difference() 与 ^ 等价   【不要相同的
'''

s1 ={10,20,30,40}
s2 = {40,50,20,70}

print(s1.intersection(s2)) #{40, 20}
print(s1 & s2)

print(s1.union(s2)) #{70, 40, 10, 50, 20, 30}
print(s1 | s2)

print(s1.difference(s2)) #{10, 30}
print(s1-s2) #{10, 30}
print(s2.difference(s1)) #{50, 70}
print(s2-s1) #{10, 30}

print(s1.symmetric_difference(s2)) #{70, 10, 50, 30}
print(s2.symmetric_difference(s1))
print(s2 ^ s1)
