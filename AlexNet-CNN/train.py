import torch
import torch.nn as nn
from torchvision import transforms, datasets, utils
import matplotlib.pyplot as plt
import numpy as np
import torch.optim as optim # 优化器
from net import AlexNet
import os
import json
import time


#device : GPU or CPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(device)

#数据转换 数据预处理：  字典 键值对 调用时 tinydict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}  tinydict['Name'] 见p33

data_transform = {
    "train": transforms.Compose([transforms.RandomResizedCrop(224),
                                 transforms.RandomHorizontalFlip(), #水平翻转 数据增强
                                 transforms.ToTensor(),
                                 transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))]),
    "val": transforms.Compose([transforms.Resize((224, 224)),  # cannot 224, must (224, 224)
                               transforms.ToTensor(),
                               transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])}

#data_root = os.path.abspath(os.path.join(os.getcwd(), "../.."))  # get data root path
data_root = os.getcwd() # 绝对路径 D:\Yingyong\PyCharm Community Edition 2021.2.1\pythonProject\AlexNet-CNN
image_path = data_root + "/flower_data/"  # flower data set path

# ImageFolder 数据加载器： 路径 处理方法
train_dataset = datasets.ImageFolder(root=image_path + "/train",transform=data_transform["train"])
train_num = len(train_dataset) #返回长度或个数
test_dataset = datasets.ImageFolder(root=image_path + "/val",transform=data_transform["val"])
val_num = len(test_dataset)

# {'daisy':0, 'dandelion':1, 'roses':2, 'sunflower':3, 'tulips':4}
flower_list = train_dataset.class_to_idx
cla_dict = dict((val, key) for key, val in flower_list.items())
# write dict into json file
json_str = json.dumps(cla_dict, indent=4) # 转换json 缩进
with open('class_indices.json', 'w') as json_file: #把字典类别索引写入json文件 open函数：文件名 写操作
    json_file.write(json_str)

batch_size = 32 #一次载入训练32张图像
train_loader = torch.utils.data.DataLoader(train_dataset,batch_size=batch_size, shuffle=True,num_workers=0)
# 加载训练集和其他参数 DataLoader
test_loader = torch.utils.data.DataLoader(test_dataset,batch_size=batch_size, shuffle=True,num_workers=0)

test_data_iter = iter(test_loader) #iter 生成迭代器 参数是支持迭代的集合对象
test_image, test_label = test_data_iter.next()
#print(test_image[0].size(),type(test_image[0]))
#print(test_label[0],test_label[0].item(),type(test_label[0]))


#显示图像，之前需把test_loader中batch_size改为4
# def imshow(img):
#     img = img / 2 + 0.5  # unnormalize
#     npimg = img.numpy()
#     plt.imshow(np.transpose(npimg, (1, 2, 0)))
#     plt.show()
#
# print(' '.join('%5s' % cla_dict[test_label[j].item()] for j in range(4)))
# imshow(utils.make_grid(test_image))

# 多分类 分成5类 初始化权重参数
net = AlexNet(num_classes=5, init_weights=True)

net.to(device)
#损失函数:这里用交叉熵
loss_function = nn.CrossEntropyLoss()
#优化器 这里用Adam
optimizer = optim.Adam(net.parameters(), lr=0.0002)
#训练参数保存路径
save_path = './AlexNet.pth'
#训练过程中最高准确率
best_acc = 0.0

#开始进行训练和测试，训练一轮，测试一轮
for epoch in range(10):
    # train
    net.train()    #训练过程中，使用之前定义网络中的dropout
    running_loss = 0.0
    t1 = time.perf_counter()
    for step, data in enumerate(train_loader, start=0):
        images, labels = data
        optimizer.zero_grad()
        outputs = net(images.to(device))
        loss = loss_function(outputs, labels.to(device))
        loss.backward()
        optimizer.step()
        # print statistics
        running_loss += loss.item()
        # print train process
        rate = (step + 1) / len(train_loader)
        a = "*" * int(rate * 50)
        b = "." * int((1 - rate) * 50)
        print("\rtrain loss: {:^3.0f}%[{}->{}]{:.3f}".format(int(rate * 100), a, b, loss), end="")
    print()
    print(time.perf_counter()-t1)

    # test
    net.eval()    #测试过程中不需要dropout，使用所有的神经元
    acc = 0.0  # accumulate accurate number / epoch
    with torch.no_grad():
        for val_data in test_loader:
            val_images, val_labels = val_data
            outputs = net(val_images.to(device))
            predict_y = torch.max(outputs, dim=1)[1] #[1] 是取这个二维数组的第二项 想想_,pred =  这次直接用一个参数接收了一个二维数组 取第二项也就是pred
            acc += (predict_y == val_labels.to(device)).sum().item()
        val_accurate = acc / val_num
        if val_accurate > best_acc:
            best_acc = val_accurate
            torch.save(net.state_dict(), save_path)
        print('[epoch %d] train_loss: %.3f  test_accuracy: %.3f' %
              (epoch + 1, running_loss / step, val_accurate))

print('Finished Training')

