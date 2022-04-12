# from aip import AipImageClassify
import os.path

from dao import cvDao
from service import imageRec

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def cvApi(image_name):
    # 服务器图片存储地址
    filepath = "/root/zhang/image/"
    # filepath = "/Users/babyna/code/garbage"
    image = os.path.join(filepath,image_name)
    # 调用自己的模型算法
    result = imageRec.recImage(image)
    # object=result['keyword']
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


# if __name__ == '__main__':
#     baiduApi()