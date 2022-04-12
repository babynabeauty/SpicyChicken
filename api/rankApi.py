import asyncio
from fastapi import APIRouter
from service import rankService

# 构建api路由
router = APIRouter(
    prefix="/rank",
    tags=["Rank"],
)

# 根据用户id获取排名
@router.get("/showRank")
async def showRank(user_id:str,mode:int):
    r"""
    根据用户id获取用户排名
    """
    loop = asyncio.get_event_loop()
    response = await loop.run_in_executor(None,rankService.showRank,user_id,mode)
    return response
