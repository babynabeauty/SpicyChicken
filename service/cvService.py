from aip import AipImageClassify
from dao import cvDao
# def baiduApi():
def cvApi(image):
    """ 你的 APPID AK SK """
    APP_ID = '25668029'
    API_KEY = '5P7WQqMQRWYsoseR7Kg5h66Z'
    SECRET_KEY = 'U63tInGMCfwTvbaFQXUEp1rWObAXVGX2'

    client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)

    """ 读取图片 """
    def get_file_content(filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()
    image = get_file_content(image)

    """ 调用通用物体和场景识别 """
    client.advancedGeneral(image);

    """ 如果有可选参数 """
    options = {}
    options["baike_num"] = 5

    """ 带参数调用通用物体和场景识别 """
    result=client.advancedGeneral(image, options)
    print(result)
    result=result['result'][0]
    # print(result)
    # baike=result['baike_info']
    # info=[]
    # temp={
    #     'name':result['keyword'],
    #     'image_url':baike['image_url'],
    #     'description':baike['description']
    # }
    # info.append(temp)
    # return{"code":200,"data":result}
#     调用百度api得到物品名字 在使用自己的数据库
    object=result['keyword']
    print(object)
    data, issuccess = cvDao.objectResearch(object)
    print(issuccess)
    if (issuccess):
        rst = []
        temp = {
            "name": data[0][1],
            "kind": data[0][2],
            "info": data[0][3],
        }
        rst.append(temp)
    return {"code": 200, "data": rst}


# if __name__ == '__main__':
#     baiduApi()