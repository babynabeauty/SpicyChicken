import torch
from torchvision import transforms
from PIL import Image
from const import *
import os

def recImage(image):
    print(os.getcwd())
    image = Image.open(image)
    test_transform = transforms.Compose([
        transforms.Resize(224),  # 剪裁的尺寸
        transforms.CenterCrop(224),  # 从中间开始剪裁
        transforms.ToTensor(),  # 构造张亮
        transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])  # 归一化
    ])
    
    image = test_transform(image)
    image = image.resize_(1, 3, 224, 224)
    if predict_model == "ResNet":
        net = torch.load(os.path.join(os.getcwd(), "train", "predict_model", "18finetune2.pkl"), map_location = 'cpu')
    elif predict_model == "MobileNet":
        net = torch.load(os.path.join(os.getcwd(), "train", "predict_model", "mobilenetv2_garbage.pkl"), map_location = 'cpu')
    net.eval()
    cla = ['其他垃圾', '厨余垃圾', '可回收垃圾', '有害垃圾']
    outputs = net(image)
    _, predicted = torch.max(outputs.data, 1)
    return cla[predicted]