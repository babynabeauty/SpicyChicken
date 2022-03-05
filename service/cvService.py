from aip import AipImageClassify

# def baiduApi():
def baiduApi(image):
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
    result=result['result'][0]
    print(result)
    baike=result['baike_info']
    info=[]
    temp={
        'name':result['keyword'],
        'image_url':baike['image_url'],
        'description':baike['description']
    }
    info.append(temp)
    return{"code":200,"data":result}


# if __name__ == '__main__':
#     baiduApi()