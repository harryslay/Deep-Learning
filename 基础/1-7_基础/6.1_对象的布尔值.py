# 测试对象的布尔值
print("-------以下的布尔值都为false：0、None、“”、‘’、False、空列表、空元组、空字典、空集合-------")
print(bool(False)) # False
print(bool(0)) #f
print(bool(0.0)) #f
print(bool(None))
print(bool(''))
print(bool(""))
print(bool([])) #空列表
print(bool(list())) #空列表
print(bool(())) #空元组
print(bool(tuple())) #空元组
print(bool({})) #空字典
print(bool(dict())) #空字典
print(bool(set())) #空集合
print("-------其他对象的布尔值都为true-------")


# 对象可以直接当做布尔表达式进行判断
age = int(input("请输入您的年龄："))
if age: #18为true 走这个
    print(age)
else: # 0为false 走这个
    print("年龄为：",age)