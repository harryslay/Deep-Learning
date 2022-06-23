import matplotlib.pyplot as plt
import networkx as nx

G = nx.MultiGraph()
path = "./数据/DDI_network.txt"
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

plt.rcParams['font.sans-serif'] = ['SimHei', 'FangSong']

print(G)
# nx.draw(G,with_labels=True)
# plt.show()

# 计算最短路径
g1 = nx.all_shortest_paths(G,source=8,target=309)
g2 = nx.all_shortest_paths(G,source=67,target=850)
g3 = nx.all_shortest_paths(G,source=990,target=1256)
lst_g1 = []
lst_g2 = []
lst_g3 = []

for item in g1:
    lst_g1.append(item)

print('8->309:',lst_g1)
print()
for item in g2:
    lst_g2.append(item)

print('67->850:',lst_g2)
print()
for item in g3:
    lst_g3.append(item)

print('990->1256:',lst_g3)
