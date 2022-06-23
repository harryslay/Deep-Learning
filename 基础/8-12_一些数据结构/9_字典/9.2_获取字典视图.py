

score={'张三':100,'lisi':28,'wwu':78}

print("------------获取所有keys .keys()------------")
keys = score.keys()
print(keys) #dict_keys(['张三', 'lisi', 'wwu'])
print(type(keys)) #<class 'dict_keys'>
print(list(keys)) #['张三', 'lisi', 'wwu'] 将keys组成的视图转成列表

# 获取所有values
print("------------获取所有values .values()------------")
values = score.values()
print(values) #dict_values([100, 28, 78])
print(type(values)) #<class 'dict_values'>
print(list(values)) #[100, 28, 78]

# 获取所有键值对
print("------------获取所有key-value对 .items()------------")
items = score.items()
print(items) #dict_items([('张三', 100), ('lisi', 28), ('wwu', 78)])
print(type(items)) #<class 'dict_items'>
print(list(items)) #[('张三', 100), ('lisi', 28), ('wwu', 78)]  转换之后的列表元素是由元组组成的 10_元组（） 小括号
