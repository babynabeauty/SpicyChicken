## Our 🌶️🐔 project！

[![image](https://img.shields.io/badge/author-7鑫协力_铁骨征征-blue.svg?logo=Github&logoColor=white)]()

### 环境说明

服务器环境：`CentOS 7`、`Apache`、`Python3.7`

识别模型框架：`PyTorch`

数据库：`MySQL`

### 项目搭建

```
git clone git@github.com:babynabeauty/SpicyChicken.git
```

**配置修改**

使用前修改`const.py`中的配置信息，如果服务器有SSL证书，将`.cer`和`.key`文件置于根目录中并修改`main.py`中相关路径。

**数据库导入**

```she
mysql -uroot -pxxxx
mysql> source garbage.sql
```
同时修改`dao/config.json`文件

### 模型训练

模型使用迁移学习进行训练，主要使用`ResNet`和`MobileNet`网络在[数据集](https://zhasion.obs.cn-north-4.myhuaweicloud.com/files/train_data.zip)上进行训练，对垃圾图片进行四分类。

**模型下载**

```
cd SpicyChicken/train/predict_model
wget https://zhasion.obs.cn-north-4.myhuaweicloud.com/files/18finetune2.pkl
wget https://zhasion.obs.cn-north-4.myhuaweicloud.com/files/mobilenetv2_garbage.pkl
```

**启动程序**

```shell
python main.py
```
