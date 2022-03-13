from fastapi import APIRouter
from service import rankService

# 构建api路由
router = APIRouter(
    prefix="/rank",
    tags=["Rank"],
)

# 根据用户id获取排名
@router.get("/showRank")
async def showRank(user_id:str):
    r"""
    根据用户id获取用户排名
    """
    response = rankService.showRank(user_id)
    return response
