#model.py
import os
import torch.nn as nn
import torch
from torchsummary import summary

# 基本是官方给出的网络结构写法 用到sequential 官方在卷积和全连接直接加了一个平均池化
class AlexNet(nn.Module):
    # 反向传播init_weights=True
    def __init__(self, num_classes=1000, init_weights=False):
        super(AlexNet, self).__init__()
        self.features = nn.Sequential(  #打包
            nn.Conv2d(3, 48, kernel_size=11, stride=4, padding=2),  # input[3, 224, 224]  output[48, 55, 55] 自动舍去小数点后
            nn.ReLU(inplace=True), #inplace 可以载入更大模型
            nn.MaxPool2d(kernel_size=3, stride=2),                  # output[48, 27, 27] kernel_num为原论文一半(原文两个gpu
            nn.Conv2d(48, 128, kernel_size=5, padding=2),           # output[128, 27, 27]
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=3, stride=2),                  # output[128, 13, 13]
            nn.Conv2d(128, 192, kernel_size=3, padding=1),          # output[192, 13, 13]
            nn.ReLU(inplace=True),
            nn.Conv2d(192, 192, kernel_size=3, padding=1),          # output[192, 13, 13]
            nn.ReLU(inplace=True),
            nn.Conv2d(192, 128, kernel_size=3, padding=1),          # output[128, 13, 13]
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=3, stride=2),                  # output[128, 6, 6]
        )
        self.classifier = nn.Sequential(
            nn.Dropout(p=0.5),
            #全链接
            nn.Linear(128 * 6 * 6, 2048),
            nn.ReLU(inplace=True),
            nn.Dropout(p=0.5),
            nn.Linear(2048, 2048),
            nn.ReLU(inplace=True),
            nn.Linear(2048, num_classes),
        )
        if init_weights:
            self._initialize_weights()

    def forward(self, x):
        x = self.features(x)
        x = torch.flatten(x, start_dim=1) #展平   或者view()
        x = self.classifier(x)
        return x
    # 权重初始化 反向传播用的
    def _initialize_weights(self):
        for m in self.modules():
            # isinstance 判断类型 如果是卷积层参数：
            if isinstance(m, nn.Conv2d):
                nn.init.kaiming_normal_(m.weight, mode='fan_out', nonlinearity='relu') #何教授方法
                # kaiming正态分布（卷积层默认使用） tensor  fan_out使反向传播时方差一致 非线性函数 上面的参数都是默认配置！
                if m.bias is not None:
                    nn.init.constant_(m.bias, 0)
            elif isinstance(m, nn.Linear):
                nn.init.normal_(m.weight, 0, 0.01)  #正态分布赋值
                nn.init.constant_(m.bias, 0)
                # constant_函数：  tensor val 用值val填充向量



