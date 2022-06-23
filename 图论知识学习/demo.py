# with open('embedding2.txt','r') as f:
#     for i in f:
#         print(f[i])
import torch
x1 =  torch.tensor([1,0,3], dtype=torch.float)
x2 = torch.tensor([3,1,0], dtype=torch.float)

res = torch.nn.CosineSimilarity(dim=-1)
x = res(x1,x2)
print(x)

import xlwt
list1 = [1,3,4,6,8,10]
list2 = [8,3.8,2.4,68,0.8,11]
list3 = [80,3.8,2.4,68,0.8,11]
list4 = [800,3.8,2.4,68,0.8,11]
f = xlwt.Workbook()
sheet1 = f.add_sheet('pos_distance',cell_overwrite_ok=True)
sheet2 = f.add_sheet('neg_distance',cell_overwrite_ok=True)
for i in range(len(list1)):
    sheet1.write(i,0,list1[i]) #行 列 值 pos_eu
    sheet1.write(i,1,list2[i]) #行 列 值 pos_cos
    sheet2.write(i,0,list3[i]) #行 列 值 neg_eu
    sheet2.write(i,1,list4[i]) #行 列 值 neg_cos
f.save('distance.xls')