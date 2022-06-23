import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

G = nx.MultiGraph()
path = "./数据0507/DDI_network.txt"
edge_list = []
node_set=set()
with open(path,'r') as f:
    for line in f:
        cols = line.strip().split('\t')
        y1 = int(cols[0])
        y2 = int(cols[1])
        node_set.add(y1)
        node_set.add(y2)
        edge=(y1,y2)
        edge_list.append(edge)
G.add_nodes_from(node_set)
G.add_edges_from(edge_list)

print(G)
'''读数据'''
pos_drag1 = []
pos_drag2 = []
path_pos='./数据0507/DDI_pos.txt'
with open(path_pos,'r') as pos_d:
    for line in pos_d:
        dg = line.strip().split('\t')
        pos_drag1.append(int(dg[0]))
        pos_drag2.append(int(dg[1]))

neg_drag1 = []
neg_drag2 = []
path_neg='./数据0507/DDI_neg.txt'
with open(path_neg,'r') as neg_d:
    for line in neg_d:
        dg = line.strip().split('\t')
        neg_drag1.append(int(dg[0]))
        neg_drag2.append(int(dg[1]))

len1 = len(pos_drag1)
len2 = len(neg_drag1)
# print("长度",len1,len2)

# 节点间最短路径长度
pos_len=[]
neg_len=[]
cnt1 = [0,0,0,0,0,0,0,0]
cnt2 = [0,0,0,0,0,0,0,0]
for i in range(len1): # 初始化
    pos_len.append(0)
    neg_len.append(0)

for i in range(len1):
    pos_len[i] = nx.dijkstra_path_length(G,pos_drag1[i],pos_drag2[i])
    cnt1[pos_len[i]]+=1 # 最短距离出现的次数

for i in range(len2):
    neg_len[i] = nx.dijkstra_path_length(G,neg_drag1[i],neg_drag2[i])
    cnt2[neg_len[i]]+=1

print(cnt1)
print(cnt2)

'''保存每对节点之间的最小距离到文件'''
f1 = open("pos_dij.txt",'w')
for line in neg_len:
    f1.write(str(line))
    f1.write('\n')
f1.close()
f2 = open("neg_dij.txt",'w')
for line in pos_len:
    f2.write(str(line))
    f2.write('\n')
f2.close()

plt.rcParams['font.sans-serif'] = ['SimHei', 'FangSong']  # 中文显示
x = np.arange(len(cnt1))
total_width, n = 0.8, 2
width = total_width/n
plt.title("最短距离次数柱状图")
plt.xlabel("最短距离")
plt.ylabel("最短距离出现次数")
p1 = plt.bar(x,cnt1,width=width,color='orange' ,label="DDI_pos")
p2 = plt.bar(x+width,cnt2,width=width,color='royalblue',label="DDI_neg")
plt.bar_label(p1, label_type='edge')
plt.bar_label(p2, label_type='edge')
plt.xticks(x+width/2, x)
plt.legend()
plt.savefig("柱状图.png")
plt.show()



