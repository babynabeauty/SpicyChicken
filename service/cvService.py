from aip import AipImageClassify
from dao import cvDao
from service import imageRec

def cvApi(image_name):
    """ 读取图片 """
    def get_file_content(filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()
    image = get_file_content(image_name)

    # 调用百度api
    result = imageRec.recImage(image)
    if result== 400:
        return {"code": 400, "data": []}

    object=result['keyword']
    data, issuccess = cvDao.objectResearch(object)
    if (issuccess):
        rst = []
        if data==():
            return {"code":404, "data":rst}

        if result['baike_info'] == {}:
            temp = {
                "thing_name": data[0][1],
                "garbage_kind": data[0][2],
                "garbage_description": data[0][3],
                "correct_rate":result['score'],
                "image_id":image_name.split(".")[0]
            }
        else:
            temp = {
                "thing_name": data[0][1],
                "garbage_kind": data[0][2],
                "icon":result['baike_info']['image_url'],
                "garbage_description": data[0][3],
                "correct_rate":result['score'],
                "image_id":image_name.split(".")[0]
            }
        rst.append(temp)
    print("rst",rst)
    return {"code": 200, "data": rst}


# if __name__ == '__main__':
#     baiduApi()