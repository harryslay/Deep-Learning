'''
graph tp tensor
transform graph G into a PyTroch tensor,[so that we can perform machine learning over the graph

'''

import torch
import torch.nn as nn
import matplotlib.pyplot as plt
import networkx as nx
print(torch.__version__) #1.11.0

# tensor basics
# 全1 3*4
ones = torch.ones(3,4)
print(ones.t())

# 全0 3*4
zeros = torch.zeros(3,4)
print(zeros)

# random[0,1) 3*4  rand函数生成左闭右开的0,1随机数矩阵
random_tensor = torch.rand(3,4)
print(random_tensor)

# shape
print(random_tensor.shape)
# 创建一个32位浮点数的全0矩阵
zeros = torch.zeros(3,4,dtype=torch.float32)
print(zeros)
print(zeros.dtype) #torch.float32

# 变成64位的
zeros = zeros.type(torch.long)
print(zeros)
print(zeros.dtype) #torch.int64

import networkx as nx
G = nx.karate_club_graph()

'''
Q5 将edge list 转成torch.LongTensor   求the torch.sum value of pos_edge_index tensor'''
def graph_to_edge_list(G):
    edge_list = []
    for edge in G.edges():
        edge_list.append(edge) # 变成了列表，里面的每个元素是一个元组（边

    return edge_list
# print(graph_to_edge_list(G))
def edge_list_ro_tensor(edge_list):
    edge_index = torch.tensor([])
    edge_index = torch.LongTensor(edge_list).t() #.t() 转置
    # print(edge_index.t())

    return edge_index
pos_edge_list = graph_to_edge_list(G)
pos_edge_index = edge_list_ro_tensor(pos_edge_list)
print("The pos_edge_index tensor has shape {}".format(pos_edge_index.shape))
# The pos_edge_index tensor has shape torch.Size([2, 78])
print("The pos_edge_index tensor has sum value {}".format(torch.sum(pos_edge_index)))
# The pos_edge_index tensor has sum value 2535


print(pos_edge_list[:5])


'''Q6 samples negative edges  然后回答五条边哪条can be negative【什么叫negative？non_edge? 注意是无向图'''
print(G.has_edge(0,1)) #t
print(G.has_edge(1,0)) #t 所以无向图不需要考虑逆向边 这函数默认覆盖了
print(G.get_edge_data(0,1)) # {'weight': 4} # 权

# 不存在的边
for nd in nx.non_edges(G):
    # print(nd)
    pass  # 看了所有的边 看看有没有环
#
#测试如何通过索引获取non_edges函数返回值中的元素 ？？？
# for i,e in enumerate(nx.non_edges(G)):
    # print(i,e) # i:索引 e：edge用一个元组表示 0 (0, 32)
    # print(i) # 如果只有一个输出i【只for i in：(0, (0, 32)) 元组中包含两个元素
    # break

lst = list(enumerate(nx.non_edges(G)))[1] # 输出列表的第一个
print(lst)
print(len(list(enumerate(nx.non_edges(G))))) # 483条non_edge

import random
def samle_negative_edges(G,num_neg_samples):
    # returns a list of negative edges.
    neg_edge_list=[]
    # 得到图中所有不存在的边，不考虑自环。注意对于逆边问题，我认为在代码编写过程中应该可以不考虑（毕竟是无向图）
    '''这个函数每太看明白'''
    non_edges_one_side = list(enumerate(nx.non_edges(G)))# 按照索引
    neg_edge_list_indices = random.sample(range(0,len(non_edges_one_side)),num_neg_samples)
    # #取样num_neg_samples长度的索引↑
    for i in neg_edge_list_indices:
        neg_edge_list.append(non_edges_one_side[i][1])

    return neg_edge_list

neg_edge_list = samle_negative_edges(G,len(pos_edge_list))

# Transform the negative edge list to tensor
neg_edge_index = edge_list_ro_tensor(neg_edge_list)
print("The neg_edge_index tensor has shape {}".format(neg_edge_index.shape)) # 证明求完了neg边

# 下面哪条边是neg？
edge_1 = (7, 1)
edge_2 = (1, 33)
edge_3 = (33, 22)
edge_4 = (0, 4)
edge_5 = (4, 2)

# 1: For each of the 5 edges, print whether it can be negative edge
# 使用了这个条件判别式 x if 语句 else y    if对是x
print('edge_1'+(" can't" if G.has_edge(edge_1[0],edge_1[1]) else 'can') + 'be negative edge')
print('edge_2'+(" can't" if G.has_edge(edge_2[0],edge_2[1]) else 'can') + 'be negative edge')
print('edge_3'+(" can't" if G.has_edge(edge_3[0],edge_3[1]) else 'can') + 'be negative edge')
print('edge_4'+(" can't" if G.has_edge(edge_4[0],edge_4[1]) else 'can') + 'be negative edge')
print('edge_5'+(" can't" if G.has_edge(edge_5[0],edge_5[1]) else 'can') + 'be negative edge')


