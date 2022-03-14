from aip import AipImageClassify

'''图像识别算法 暂时调用百度api'''
def recImage(image):
    """ 你的 APPID AK SK """
    APP_ID = '25668029'
    API_KEY = '5P7WQqMQRWYsoseR7Kg5h66Z'
    SECRET_KEY = 'U63tInGMCfwTvbaFQXUEp1rWObAXVGX2'

    client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)

    """ 调用通用物体和场景识别 """
    client.advancedGeneral(image)

    """ 如果有可选参数 """
    options = {}
    options["baike_num"] = 5

    """ 带参数调用通用物体和场景识别 """
    result = client.advancedGeneral(image, options)
    # print("result",result)
    if result.get('error_msg') == None:
        return result['result'][0]
    return 400