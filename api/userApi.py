from model import schemas
from fastapi import APIRouter
from service import userService

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
    response = userService.login(info.user_id, info.user_name, info.avatar)
    return response
