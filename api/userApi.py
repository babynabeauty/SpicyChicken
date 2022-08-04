import asyncio
from model import schemas
from fastapi import APIRouter
from service import userService
from const import *

# 构建api路由
router = APIRouter(
    prefix="/user",
    tags=["User"],
)

# 将用户信息记录到数据库中
@router.post("/login")
async def login(info:schemas.Login):
    r"""
    如果用户第一次登录则将其添加到数据库中
    """
    print(info.user_id, info.user_name, info.avatar)
    loop = asyncio.get_event_loop()
    response = await loop.run_in_executor(None,userService.login,info.user_id, info.user_name, info.avatar)
    return response

# 软件端的登陆（Android端）
@router.post("/login2")
async def login2(info:schemas.Login2):
    r"""
    如果用户第一次登录则将其添加到数据库中
    """
    # loop = asyncio.get_event_loop()
    # 返回中加入密码和判断信息

    # response = await loop.run_in_executor(None,userService.login2,info.user_id, info.user_name,info.user_psw, info.avatar,info.code)
    response = userService.login2(info.user_name,info.user_psw,info.avatar)
    return response

# 返回小程序相关信息
@router.get("/getinfo")
async def getinfo():
    response = {
        "appid": wechat_appid,
        "appsecret": wechat_appsecret
    }
    return response
