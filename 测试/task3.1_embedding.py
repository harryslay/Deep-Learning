import torch
import torch.nn as nn
import networkx as nx
import random
import xlwt
import matplotlib.pyplot as plt
from torch.optim import SGD
from sklearn.decomposition import PCA

G = nx.MultiGraph()
path = "./数据/DDI_network.txt"
edge_list = []
node_set = set()
with open(path, 'r') as f:
    for line in f:
        cols = line.strip().split('\t')
        y1 = int(cols[0])
        y2 = int(cols[1])
        node_set.add(y1)
        node_set.add(y2)
        edge = (y1, y2)
        edge_list.append(edge)
G.add_nodes_from(node_set)
G.add_edges_from(edge_list)

print(G)


def create_node_emb(num_node=1603, embedding_dim=16):
    emb = nn.Embedding(num_node, embedding_dim)
    emb.weight.data = torch.rand(num_node, embedding_dim)  # uniform distribution
    return emb

emb = create_node_emb()

# print(emb) #Embedding(1603, 16)

def graph_to_edge_list(G):
    edge_list = []
    for edge in G.edges():
        edge_list.append(edge)  # 变成了列表，里面的每个元素是一个元组（边
    return edge_list

# print(graph_to_edge_list(G))
def edge_list_to_tensor(edge_list):
    edge_index = torch.tensor([])
    edge_index = torch.LongTensor(edge_list).t()  # .t()
    return edge_index

pos_edge_list = graph_to_edge_list(G)
pos_edge_index = edge_list_to_tensor(pos_edge_list)

def sample_negative_edges(G, num_neg_samples):
    # returns a list of negative edges.
    neg_edge_list = []
    # non_edge 无向图
    non_edges_one_side = list(enumerate(nx.non_edges(G)))  # 按照索引
    neg_edge_list_indices = random.sample(range(0, len(non_edges_one_side)), num_neg_samples)
    # 取样num_neg_samples长度的索引↑
    for i in neg_edge_list_indices:
        neg_edge_list.append(non_edges_one_side[i][1])

    return neg_edge_list


neg_edge_list = sample_negative_edges(G, len(pos_edge_list))

# neg变成tensor
neg_edge_index = edge_list_to_tensor(neg_edge_list)

loss_fn = nn.BCELoss() #
sigmoid = nn.Sigmoid()

pos_label = torch.ones(pos_edge_index.shape[1], )
neg_label = torch.zeros(neg_edge_index.shape[1], )
# neg pos拼接成一个tensor
train_label = torch.cat([pos_label, neg_label], dim=0)  # 行
train_edge = torch.cat([pos_edge_index, neg_edge_index], dim=1)  # 列 index之前转置成2,1603了

def accuracy(pred, label):
    acc = 0.0
    acc = round(((pred > 0.5) == label).sum().item() / (pred.shape[0]), 4)
    return acc

def train(emb, loss_fn, sigmoid, train_label, train_edge):
    epochs = 10000
    learning_rate = 0.1
    optimizer = SGD(emb.parameters(), lr=learning_rate, momentum=0.9)

    for i in range(epochs):
        optimizer.zero_grad()
        train_node_emb = emb(train_edge)  # emb只能输入索引 [2,1603*2,16]
        dot_product_result = train_node_emb[0].mul(train_node_emb[1]) # [2*1603,16]
        dot_product_result = torch.sum(dot_product_result, 1)
        sigmoid_result = sigmoid(dot_product_result) # 0-1
        loss_result = loss_fn(sigmoid_result, train_label)
        loss_result.backward()
        optimizer.step()
        # if i % 100 == 0:
        #     print(loss_result) #0.5360
        #     print(accuracy(sigmoid_result, train_label)) #0.7407

    return emb

emb = train(emb, loss_fn, sigmoid, train_label, train_edge)
print(emb)

f = open("embedding.txt", 'w')
lst = []
for i in range(0, 1603):
    lst.append(i)
ids = torch.LongTensor(lst)
f.write(str(emb(ids)))
f.close()

'''读数据'''
pos_drag1 = []
pos_drag2 = []
path_pos = './数据/DDI_pos.txt'
with open(path_pos, 'r') as pos_d:
    for line in pos_d:
        dg = line.strip().split('\t')
        pos_drag1.append(int(dg[0]))
        pos_drag2.append(int(dg[1]))
len1 = len(pos_drag1)

neg_drag1 = []
neg_drag2 = []
path_neg = './数据/DDI_neg.txt'
with open(path_neg, 'r') as neg_d:
    for line in neg_d:
        dg = line.strip().split('\t')
        neg_drag1.append(int(dg[0]))
        neg_drag2.append(int(dg[1]))

pos_eu_dis = ['pos_eu']
pos_cos_dis = ['pos_cos']

for i in range(len1):
    x1 = emb.weight[pos_drag1[i]]  # 本来填索引 就是节点号
    x2 = emb.weight[pos_drag2[i]]
    c_dis = nn.CosineSimilarity(-1, 1e-4)
    c_res = round(float(c_dis(x1, x2)), 4)
    e_dis = nn.PairwiseDistance(p=2)
    e_res = round(float(e_dis(x1[0], x2[0])), 4)  # 欧氏距离
    pos_eu_dis.append(e_res)
    pos_cos_dis.append(1 - c_res) # 1-cosineSim就是余弦距离

neg_eu_dis = ['neg_eu']
neg_cos_dis = ['neg_cos']

for i in range(len1):
    x1 = emb.weight[neg_drag1[i]]
    x2 = emb.weight[neg_drag2[i]]
    c_dis = nn.CosineSimilarity(-1, 1e-4)
    c_res = round(float(c_dis(x1, x2)), 4)
    e_dis = nn.PairwiseDistance(p=2)
    e_res = round(float(e_dis(x1[0], x2[0])), 4)
    neg_eu_dis.append(e_res)
    neg_cos_dis.append(1 - c_res)

''' 存储'''
f = xlwt.Workbook()
sheet1 = f.add_sheet('pos_distance', cell_overwrite_ok=True)
sheet2 = f.add_sheet('neg_distance', cell_overwrite_ok=True)
for i in range(len(pos_eu_dis)):
    sheet1.write(i, 0, pos_eu_dis[i])  # pos_eu
    sheet1.write(i, 1, pos_cos_dis[i])  # pos_cos
    sheet2.write(i, 0, neg_eu_dis[i])  # neg_eu
    sheet2.write(i, 1, neg_cos_dis[i])  # neg_cos
f.save('distance.xls')