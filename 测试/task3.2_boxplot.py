import xlwings as xw
import matplotlib.pyplot as plt
import xlwt
import xlrd
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']

datafile = 'distance.xls'
app = xw.App(visible=False, add_book=False)
wb = app.books.open(datafile)

box_1 = wb.sheets[0].range('A2:A1062').value
box_2 = wb.sheets[0].range('B2:B1062').value
box_3 = wb.sheets[1].range('A2:A1062').value
box_4 = wb.sheets[1].range('B2:B1062').value

plt.figure(figsize=(8, 5))
labels1 = 'pos_eu', 'pos_cos', 'neg_eu', 'neg_cos'
plt.title('药物对在嵌入空间的距离',fontsize=15)
plt.boxplot([box_1,box_2,box_3,box_4], labels=labels1, meanline=True,showmeans=True, patch_artist=True,boxprops = {'color':'orangered','facecolor':'pink'})
plt.savefig("boxplot.png")

m1 = round(np.mean(box_1,axis=0),4)
m2 = round(np.mean(box_2,axis=0),4)
m3 = round(np.mean(box_3,axis=0),4)
m4 = round(np.mean(box_4,axis=0),4)
print("正样本药物对欧式距离平均值为：{}".format(m1))
print("正样本药物对余弦距离平均值为：{}".format(m2))
print("负样本药物对欧式距离平均值为：{}".format(m3))
print("负样本药物对余弦距离平均值为：{}".format(m4))

plt.show()