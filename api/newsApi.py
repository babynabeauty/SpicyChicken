import asyncio
from fastapi import APIRouter
from service import newsService
from fastapi import File
from fastapi import Form
import os
from const import *

# 构建api路由
router = APIRouter(
    prefix="/news",
    tags=["News"],
)

@router.post("/generate_news")
async def generate_news(
    file: bytes = File(...),
    picture: bytes = File(...),
    title: str = Form(...),
    author: str = Form(...),
    type:str = Form(...),
    tag: str = Form(...)
):
    r"""
    根据输入生成新闻链接并保存到数据库
    """
    response = newsService.generate_news(file, picture, title, author, type, tag)
    return response

@router.get("/getNewsDetail")
async def generate_news(id: int):
    r"""
    根据id获取html的文本内容
    """
    path = os.path.join(news_save_path, str(id), "index.html")
    with open(path, "r", encoding="utf-8") as f:
        response = "".join(f.readlines())
    return response

@router.get("/getNewsList")
async def generate_news(offset:int):
    r"""
    根据偏移量获取新闻列表
    """
    loop = asyncio.get_event_loop()
    response = await loop.run_in_executor(None,newsService.getnewsList,offset)
    return response