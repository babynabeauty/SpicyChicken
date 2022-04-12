# from aip import AipImageClassify
from __future__ import print_function,division
import torch
from torch.autograd import Variable
from torchvision import transforms, utils
import math
from PIL import Image
from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

class Resize(object):
    def __init__(self, size, interpolation=Image.BILINEAR):
        # assert isinstance(size, int) or (isinstance(size, collections.Iterable) and len(size) == 2)
        self.size = size
        self.interpolation = interpolation

    def __call__(self, img):
        w, h = img.size

        min_edge = min(img.size)
        rate = min_edge / self.size

        new_w = math.ceil(w / rate)
        new_h = math.ceil(h / rate)

        return img.resize((new_w, new_h))

'''图像识别算法 暂时调用百度api'''
def recImage(image):
    image = Image.open(image)
    test_transform = transforms.Compose([
        Resize(224),  # 剪裁的尺寸
        transforms.CenterCrop(224),  # 从中间开始剪裁
        transforms.ToTensor(),  # 构造张亮
        transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])  # 归一化
    ])

    image = test_transform(image)
    image = image.resize_(1, 3, 224, 224)
    net = torch.load('/root/zhang/SpicyChicken/18finetune.pkl', map_location='cpu')
    cla = ['其他垃圾', '厨余垃圾', '可回收垃圾', '有害垃圾']
    outputs = net(Variable(image))
    print(outputs)
    _, predicted = torch.max(outputs.data, 1)
    return cla[predicted]