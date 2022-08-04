from dao import userDao
from model.responseCode import responseCode

# 根据user_id进行得分登记
def login(user_id:str, user_name:str, avatar:str):
    issuccess = userDao.login(user_id, user_name, avatar)
    if(issuccess):
        return responseCode(200, None, "success")
    else:
        return responseCode(400, None, "用户登录错误")

def login2(user_name:str, user_psw:str,avatar:str):
    # 索引到logni2
    data = userDao.login2(user_name,user_psw,avatar)
    issuccess  = 1
    if(issuccess):
        if data[0] == 1:
            return responseCode(201,[user_name,user_psw,avatar],"注册成功")
        else:
            if data[1][4] == user_psw:
                return responseCode(202,[user_name,user_psw,avatar],"登陆成功")
            else:
                return responseCode(401,[user_name,user_psw,avatar],"密码错误")
    else:
        return responseCode(400, None, "登录错误")

