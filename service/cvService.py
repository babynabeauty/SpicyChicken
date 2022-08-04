from aip import AipImageClassify
import os.path
from dao import cvDao
from service import imageRec
from const import *

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def cvApi(image_name):
    # 服务器图片存储地址
    image = os.path.join(image_save_path, image_name)
    # 调用自己的模型算法
    result = imageRec.recImage(image)

    data, issuccess = cvDao.ClassifyResearch(result)
    if (issuccess):
        # if data==():
        #     return {"code":404, "data":{}}
        # if result['baike_info'] == {}:
        #     rst = {
        #         "thing_name": data[0][1],
        #         "garbage_kind": data[0][2],
        #         "garbage_description": data[0][3],
        #         "correct_rate":result['score'],
        #         "image_id":image_name.split(".")[0]
        #     }
        # else:
        #     rst = {
        #         "thing_name": data[0][1],
        #         "garbage_kind": data[0][2],
        #         "icon":result['baike_info']['image_url'],
        #         "garbage_description": data[0][3],
        #         "correct_rate":result['score'],
        #         "image_id":image_name.split(".")[0]
        #     }
        rst = {
            "garbage_kind":data[0][1],
            "garbage_description":data[0][2]
        }
    # print("rst",rst)
    return {"code": 200, "data": rst}

def cvApi2(image_name):
    APP_ID = APP_ID
    API_KEY = API_KEY
    SECRET_KEY = SECRET_KEY
    client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)


    # 服务器图片存储地址
    image_path = os.path.join(image_save_path, image_name)

    image = get_file_content(image_path)
    """ 调用通用物体和场景识别 """
    client.advancedGeneral(image);
    """ 如果有可选参数 """
    # options = {}
    # options["baike_num"] = 5
    """ 带参数调用通用物体和场景识别 """
    # result = client.advancedGeneral(image, options)
    result = client.advancedGeneral(image)
    print(result)
    result = result['result'][0]

    # object=result['keyword']
    data, issuccess = cvDao.objectResearch(result['keyword'])
    if (issuccess):
        if data==():
            return {"code":404, "data":{}}
        rst = {
            # "garbage_kind": data[0][1],
            "garbage_description": data[0][2],
            "garbage_info":data[0][3]
        }
    # print("rst",rst)
    return {"code": 200, "data": rst}