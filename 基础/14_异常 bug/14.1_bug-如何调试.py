lst=[{'rating':[9.7,1048912],'id':'123145','type':['犯罪','剧情'],'title':'肖申克的救赎','actors':['摩根','蒂姆']},
    {'rating':[9.5,1048532],'id':'123146','type':['爱情','同性'],'title':'霸王别姬','actors':['张国荣','葛优']},
    {'rating':[9.3,1048142],'id':'123147','type':['犯罪','剧情'],'title':'肖申克的救赎','actors':['汤姆','罗宾']}]

name=input("请输入要查询的演员：")
for item in lst: # 遍历列表：得到{}
    item_act=item['actors']
    # print(item_act)
    for i in item_act: # 遍历字典，得到key
        # print(i)
        if name ==i:
            print(name+'出演了'+item['title'])

# 复习字典的遍历：for key in dict：
#                 print(key,dict[key],dict.get(key))