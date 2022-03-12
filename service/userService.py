from dao import userDao
from model.responseCode import responseCode

# 根据user_id进行得分登记
def login(user_id:str):
    issuccess = userDao.login(user_id)
    if(issuccess):
        return responseCode(200, None, "success")
    else:
        return responseCode(400, None, "用户登录错误")

# 根据user_id获取得分和排名