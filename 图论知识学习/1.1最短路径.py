import matplotlib.pyplot as plt
import networkx as nx
from scipy.sparse.csgraph import connected_components

G = nx.MultiGraph()
path = "./数据0507/DDI_network.txt"
# path = "./data.txt"
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

plt.rcParams['font.sans-serif'] = ['KaiTi', 'SimHei', 'FangSong']  # 汉字字体,优先使用楷体，如果找不到楷体，则使用黑体
plt.rcParams['font.size'] = 12  # 字体大小
plt.rcParams['axes.unicode_minus'] = False  # 正常显示负号

print(G)
nx.draw(G,with_labels=True)
# plt.show()

# 计算最短路径
g1 = nx.all_shortest_paths(G,source=1584,target=1555)
g2 = nx.all_shortest_paths(G,source=4,target=10)
g3 = nx.all_shortest_paths(G,source=4,target=576)
lst_g1 = []
lst_g2 = []
lst_g3 = []

for item in g1:
    lst_g1.append(item)

print('2->435:',lst_g1)
print()
for item in g2:
    lst_g2.append(item)

print('4->10:',lst_g2)
print()
for item in g3:
    lst_g3.append(item)

print('4->576:',lst_g3)


#节点间最短路径长度
# len_g = nx.all_pairs_shortest_path_length(G)
# len = []
# for i in len_g:
#     print(i)
    # len.append()
# print(ln)