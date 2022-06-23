import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei', 'FangSong']  # 中文显示

cnt1 = [1,3,5,6,2,7]
cnt2 = [2,3,8,9,1,3]
x=np.arange(len(cnt1))
total_width, n = 0.8, 2
width = total_width/n
plt.title("最短距离次数柱状图")
plt.xlabel("最短距离")
plt.ylabel("最短距离出现次数")
p1 = plt.bar(x,cnt1,width=width,color='orange' ,label="DDI_pos")
p2 = plt.bar(x+width,cnt2,width=width,color='royalblue',label="DDI_neg")
plt.bar_label(p1, label_type='edge')
plt.bar_label(p2, label_type='edge')
plt.xticks(x + width / 2, x)
plt.legend()
plt.show()


f1 = open("pos_dij.txt",'w')
for line in cnt1:
    f1.write(str(line))
    f1.write('\n')
f1.close()
f2 = open("neg_dij.txt",'w')
for line in cnt2:
    f2.write(str(line))
    f2.write('\n')
f2.close()