import networkx as nx
# import torch
# import torch.nn as nn
# from torch.optim import SGD
#
import matplotlib.pyplot as plt
import scipy
from scipy import sparse
#
# from sklearn.decomposition import PCA
#
# import random

# 空手道的数据 无向图 34节点 78条边
G = nx.karate_club_graph()
print(type(G))

# nx.draw(G,with_labels=True)
# plt.show()

for v in G:
    # print(f"{v:4} {G.degree(v):6}") # 输出节点和度
    # print(G.nodes[v]["club"]) # 输出节点和度
    pass

print(G.nodes[5]["club"]) #Mr. Hi  nodes 有一个叫club的属性 有下面两个名字：hi和officer
print(G.nodes[9]["club"]) #Officer
print(G.number_of_nodes()) #34
print(G.number_of_edges()) #78

print(G.is_directed()) #f 是否是有向图 不是

'''Q1 average degree of the karate club network'''
def average_degree(num_edges,num_nodes):
    # 输入边数和点数，返回avg node degree
    ave_degree = 0
    ave_degree = round(2*num_edges/num_nodes) #求平均度：2*点/边
    return ave_degree

num_edges=G.number_of_edges()
num_nodes=G.number_of_nodes()
avg_degree = average_degree(num_edges,num_nodes)
print("Average degree of the karate club network is {0}".format(avg_degree))

'''Q2 average clustring coefficient of the G'''
def average_clustering_cofficient(G):
    avg_cluster_coef=0
    avg_cluster_coef = round(nx.average_clustering(G),2) # round的第二个参数：保留几位小时

    return avg_cluster_coef

avg_cluster_coed = average_clustering_cofficient(G)
print("Average clustering cofficient of G is {0}".format(avg_cluster_coed)) # 当只有一个参数{里面的数字可以省略

'''Q3 pagerank value for node 0 after one pagerank iteration '''
# 要求不能使用自带的函数nx.pagerank 我好像也使用不了，会报错
# 得到node0邻居-》邻居出度（因为是无向图，所以就是度-》计算得到公式
def one_iter_pagerank(G,beta,r0,node_id):
    r1 = 0;
    for ni in nx.neighbors(G,node_id):
        di = G.degree[ni] # 对每个邻居求度 就是他的出度
        r1+=beta*r0/di #
    r1+=(1-beta)*(1/G.number_of_nodes())
    r1 = round(r1,2) # 公式

    return r1
beta = 0.8
r0 = 1 / G.number_of_nodes()
node = 0
r1 = one_iter_pagerank(G,beta,r0,node)
print("the pageRank value for node 0 after one iteration is {}".format(r1))
# pagerank_0 = one_iter_pagerank(G)
# print(nx.pagerank(G)) # 我用不了

'''Q4 raw closeness centrality(紧密中心性) for the karate club network node 5'''
# 1/dijs[i,j

# 计算最短路的函数
G1 = nx.path_graph(5) # 相当于画一条线（上面五个点
nx.draw(G1,with_labels=True)
pairs = nx.shortest_path_length(G1,source=1)
print(pairs) #{1: 0, 0: 1, 2: 1, 3: 2, 4: 3}
# for pair in pairs: # 遍历字典获得的是value 类型是int
#     print(pairs[pair]) #value
#     print(pair) #key
#     print(type(pair))

plt.show()
# 解法1
def closeness_centrality(G,node=5):
    closeness=0
    # 计算node与所有其他节点之间的最短路径->计算得到结果【公式：c(v) = 1/uv之间的最短路径之和  （u!=v
    node_length_pairs = nx.shortest_path_length(G,source=node) # 节点5到所有其他节点的最短路径 字典
    denominator = 0
    for i in range(G.number_of_nodes()): # 按从小到大遍历遍历出来的结果是value
        if i!=node: # 不算他自己
            denominator+=node_length_pairs[i]
    closeness = round(1/denominator,2)

    return closeness
node = 5
closeness = closeness_centrality(G,node = node)
print("The karate club network has closeness centrality {}".format(closeness))

# 解法2 使用nx中的自带函数
def closeness_centrality(G,node=5):
    closeness = 0
    closeness = nx.closeness_centrality(G,u=node) # 参数 注意这个函数的返回是?
    print("----",closeness)
    closeness = closeness/(G.number_of_nodes()-1)
    closeness = round(closeness,2)
    return closeness

node = 5
closeness = closeness_centrality(G,node = node)
print("The karate club network has closeness centrality {}".format(closeness))