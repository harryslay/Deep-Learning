import  networkx as nx
from PIL import Image
import matplotlib.pyplot as plt
from networkx.drawing.nx_pydot import to_pydot
from  matplotlib.font_manager import *

nodes = ['0','1','2','3','4','5','a','b','c']
edges=[('0','0',1),('0','1',1),('0','5',1),('0','5',2),('1','2',3),('1','4',5),('2','1',7),('2','4',6),('a','b',0.5),('b','c',0.5),('c','a',0.5)]

def showGraph(G):
    P=to_pydot(G)
    P.write_jpeg('pydot.png')

    # 使用matplotlib保存图片
    pos = nx.shell_layout(G)
    nx.draw(G, pos, with_labels=True)
    plt.savefig('mat.png')
    plt.close()

    # 将前面两张图显示
    plt.subplots(figsize=(12, 6))
    # plt.suptitle('Diffrent')
    # 载入matplotlib的图片
    plt.subplot(1, 2, 1)
    plt.title('matplotlib')

plt.imshow(Image.open('mat.png'))
# plt.axis('off')
# 去掉坐标刻度
plt.xticks([])
plt.yticks([])

# 载入pydot的图片
plt.subplot(1, 2, 2)
plt.title('pydot')
plt.imshow(Image.open('pydot.png'))
# plt.axis('off')
# 去掉坐标刻度
plt.xticks([])
plt.yticks([])

# 显示图片
plt.show()