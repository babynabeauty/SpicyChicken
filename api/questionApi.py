import asyncio
from fastapi import APIRouter
from service import questionService
from model import schemas

# 构建api路由
router = APIRouter(
    prefix="/question",
    tags=["Question"],
)

# 根据id获取题目
@router.get("/showOne")
async def showone(id:int):
    r"""
    根据问题id获取题目信息
    """
    loop = asyncio.get_event_loop()
    response = await loop.run_in_executor(None, questionService.showone, id)

    return response

# 用户提交答案
@router.post("/submitAnswer")
async def submitAnwer(info: schemas.SubmitAnswer):
    r"""
    用户提交题目的答案
    """
    loop = asyncio.get_event_loop()
    response = await loop.run_in_executor(None, questionService.submitAnswer, info.user_id, info.question_id, info.selected)
    return response

# 查询用户今日是否完成每日一题
@router.get("/ifTodayProblem")
async def ifTodayProblem(user_id: str):
    r"""
    查询用户今日是否完成每日一题
    """
    loop = asyncio.get_event_loop()
    response = await loop.run_in_executor(None,questionService.ifTodayProblem,user_id)
    return response

# 查询用户本月做题情况
@router.get("/historyStatus")
async def ifTodayProblem(user_id: str, year:int, month: int):
    r"""
    根据年月查询用户本月做题情况
    """
    loop = asyncio.get_event_loop()
    response = await loop.run_in_executor(None,questionService.history,user_id, year, month)
    return response

# 查询历史做题情况
@router.get("/showHistoryOne")
async def ifTodayProblem(user_id:str, question_id: int):
    r"""
    查询用户之前做过的题（包括题目和当时的选择）
    """
    loop = asyncio.get_event_loop()
    response = await loop.run_in_executor(None,questionService.showHistoryOne,user_id, question_id)
    return response