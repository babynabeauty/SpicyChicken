from fastapi import APIRouter
from service import questionService

# 构建api路由
router = APIRouter(
    prefix="/question",
    tags=["Question"],
)

# 获取所有的题目
@router.get("/showall")
async def showall():
    response = questionService.showall()
    return response

# 根据id获取题目
@router.get("/showone")
async def showone(id:int):
    response = questionService.showone(id)
    return response
