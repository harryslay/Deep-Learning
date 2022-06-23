import torch
from net2 import MyAlexNet
from torch.autograd import Variable
from torchvision.transforms import ToPILImage
from torchvision import datasets, transforms
from torchvision.datasets import ImageFolder
from torch.utils.data import DataLoader

ROOT_TRAIN = r'D:/Yingyong/PyCharm Community Edition 2021.2.1/pythonProject/AlexNet/data/train'
ROOT_TEST = r'D:/Yingyong/PyCharm Community Edition 2021.2.1/pythonProject/AlexNet/data/val'

# 将图像的像素值归一化到[-1,1]之间

normalize = transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
# 训练集 预处理
train_transform = transforms.Compose([
    transforms.RandomResizedCrop(224),
    transforms.RandomVerticalFlip(),
    # 数据增强
    transforms.ToTensor(),
    normalize
])
# 测试集 预处理
val_transform = transforms.Compose([
    transforms.RandomResizedCrop(224),
    transforms.RandomVerticalFlip(),
    # transforms.Resize((224, 224)),
    transforms.ToTensor(),
    normalize
])

train_dataset = ImageFolder(ROOT_TRAIN, transform=train_transform)
val_dataset = ImageFolder(ROOT_TEST, transform=val_transform)
#  从哪个路径读文件 对PILImage的转换操作

train_dataloader = DataLoader(train_dataset, batch_size=32, shuffle=True)
val_dataloader = DataLoader(val_dataset, batch_size=32, shuffle=True)

device = 'cuda' if torch.cuda.is_available() else 'cpu'

model = MyAlexNet().to(device)

# 加载模型
model.load_state_dict(torch.load("D:/Yingyong/PyCharm Community Edition 2021.2.1/pythonProject/AlexNet/save_model/best_model.pth"))
# 获取预测结果
classes = [
    "cat",
    "dog"
]
# 把张量转化为照片格式
show = ToPILImage()
# 进入验证阶段
model.eval()

for i in range(10):
    # x, y = val_dataset[2000+i][0], val_dataset[2000+i][1]
    x, y = val_dataset[i][0], val_dataset[i][1]
    show(x).show()
    x = Variable(torch.unsqueeze(x, dim=0).float(), requires_grad =True).to(device)
    x = torch.as_tensor(x).to(device)
    with torch.no_grad():
        pred = model(x)
        # print(f'pred:"{pred}"')
        predicted, actual = classes[torch.argmax(pred[0])], classes[y]

        print(f'predicted:"{predicted}",Actual:"{actual}"')


