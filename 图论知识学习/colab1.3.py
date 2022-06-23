'''
embedding 应该和word embedding差不多 可以再回去看word embedding

'''
import torch
import random
import torch.nn as nn
import networkx as nx
import matplotlib.pyplot as plt
from sklearn.decomposition import  PCA
print(torch.__version__) #1.6.0
'''
use nn.Embedding module in pytorch
先初始化一个embedding layer
比如我们想要对4个item进行embedding 每个item用8d的向量表示
'''

G = nx.karate_club_graph()



emb_sample = nn.Embedding(num_embeddings=4,embedding_dim=8) #'''这个函数就是随机初始化一个num*dim大小的二维表'''
# print('sample embedding layer:{}'.format(emb_sample))

print(emb_sample.weight)
# We can select items from the embedding matrix, by using Tensor indices 使用下标
id = torch.LongTensor([1]) # 取了第1个item (从0开始
# print(emb_sample(id))

# select multiple embeddings
ids = torch.LongTensor([[1,3],[0,2]]) # 输入必须是索引，可以是这种形式 那输出就是一个
print(emb_sample(ids))
'''这个nn.embedding 函数的输入必须是索引！一般是longtensor格式的！ 所以ids是索引 输入'''
print(emb_sample(ids).shape) #torch.Size([2, 2, 8])

shape = emb_sample.weight.data.shape
print(shape) #torch.Size([4, 8])
# 可以重写 变成全1
emb_sample.weight.data = torch.ones(shape)
ids = torch.LongTensor([0,3]) 
# print(emb_sample(ids))
# print(emb_sample.weight)


'''
want to have 16-d vector for each node in the karate club network
wanna initalize the matrix under uniform distribution(均匀分布）, in the range of [0,1)
 We suggest you using torch.rand
'''
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




# torch.manual_seed(1)


def create_node_emb(num_node = 34,embedding_dim = 16):
    # 这个函数用来创建node embedding matrix
    # A torch.nn.Embedding layer will be returned
    emb =None

    emb = nn.Embedding(num_node,embedding_dim)
    emb.weight.data = torch.rand(num_node,embedding_dim)

    return emb

emb = create_node_emb()
ids = torch.LongTensor([0,3]) # 这个函数的参数是列表，列表里面是索引 从0开始 比如这个就是输出第0个和第3个
# 输出embedding layer
print("Embedding :{}".format(emb))

# an example that gets the embeddings for node 0 and 3
print(emb(ids))


'''visualize the initial node embeddings 可视化'''

def visualize_emb(emb):
    X = emb.weight.data.numpy()
    pca = PCA(n_components=2) # 降维到2d
    components = pca.fit_transform(X)
    # print(components)
    plt.figure(figsize=(6,6))
    club1_x = []
    club1_y = []
    club2_x = []
    club2_y = []
    for node in G.nodes(data = True):
        if node[1]['club'] == 'Mr. Hi': # node第一个元素是索引，第二个是名
            club1_x.append(components[node[0]][0]) # node[0]是序号
            club1_y.append(components[node[0]][1])
        else:
            club2_x.append(components[node[0]][0])
            club2_y.append(components[node[0]][1])
    plt.scatter(club1_x,club1_y,color = 'red',label='Mr. Hi')
    plt.scatter(club2_x,club2_y,color = 'blue',label='Officer')
    plt.legend()
    plt.show()

visualize_emb(emb)

'''training the embedding 要best loss 和accuracy on gradescope'''

from torch.optim import SGD
def accuracy(pred, label):
    # >0.5 :1 四舍五入 四位小数
    acc = 0.0
    acc = round(((pred>0.5)==label).sum().item()/(pred.shape[0]),4)
    # 预测与实际值一致数/所有结果
    return acc

def train(emb,loss_fn,sigmoid,train_label,train_edge):
    # (1) Get the embeddings of the nodes in train_edge
    # (2) Dot product the embeddings between each node pair
    # (3) Feed the dot product result into sigmoid
    # (4) Feed the sigmoid output into the loss_fn
    # (5) Print both loss and accuracy of each epoch
    epochs = 500
    learning_rate = 0.1
    optimizer = SGD(emb.parameters(),lr = learning_rate,momentum=0.9)

    for i in range(epochs):
        optimizer.zero_grad()
        train_node_emb = emb(train_edge) # emb是构建好的二维表，只能输入索引
        dot_product_result = train_node_emb[0].mul(train_node_emb[1])
        dot_product_result = torch.sum(dot_product_result,1)
        sigmoid_result = sigmoid(dot_product_result)
        loss_result = loss_fn(sigmoid_result,train_label)
        loss_result.backward()
        optimizer.step()

        if i%10==0:
            print(loss_result)
            print(accuracy(sigmoid_result,train_label))

loss_fn = nn.BCELoss()
sigmoid = nn.Sigmoid()

pos_label = torch.ones(pos_edge_index.shape[1],)
neg_label = torch.zeros(neg_edge_index.shape[1],)

# neg pos拼接成一个tensor
train_label = torch.cat([pos_label, neg_label], dim=0)  #横着叠

# 把neg和pos拼接成一个tensor 因为网络小 就不划分验证集了
train_edge = torch.cat([pos_edge_index, neg_edge_index], dim=1)  #竖着叠

train(emb, loss_fn, sigmoid, train_label, train_edge)
visualize_emb(emb)