import torch
from net import AlexNet
from PIL import Image
from torchvision import transforms
import matplotlib.pyplot as plt
import json

data_transform = transforms.Compose(
    [transforms.Resize((224, 224)),
     transforms.ToTensor(),
     transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

# load image
# img = Image.open("./sunflower.jpg")  #验证太阳花
# img = Image.open("./roses.jpg")     #验证玫瑰花
img = Image.open("./tulip2.jpg")     #验证郁金香
plt.imshow(img) #先接收一张图 还可以进行别的处理 只有plt.show才能展示出来
# [N, C, H, W]
img = data_transform(img)
# expand batch dimension 扩展纬度 第一个参数：要插入的tensor（已经处理过的图片 第二个参数：要插入的纬度
img = torch.unsqueeze(img, dim=0)

# read class_indict
try:
    json_file = open('./class_indices.json', 'r')  #只读模式打开这个文件
    class_indict = json.load(json_file)
except Exception as e:
    print(e)
    exit(-1)

# create model
model = AlexNet(num_classes=5)
# load model weights
model_weight_path = "./AlexNet.pth"
model.load_state_dict(torch.load(model_weight_path))
model.eval()
with torch.no_grad():
    # predict class
    output = torch.squeeze(model(img))
    predict = torch.softmax(output, dim=0) # 只有维度为1时才会去掉。
    predict_cla = torch.argmax(predict).numpy() # 得到概率最大的处所对应的索引 argmax直接返回序号 .numpy 获取 tensor值？？？？
print(class_indict[str(predict_cla)], predict[predict_cla].item())
plt.show()

