# 文字查询有关的api

import asyncio
import os
import shutil
from pathlib import Path
from typing import Union, Any
from tempfile import NamedTemporaryFile
from fastapi import APIRouter, Depends, File, UploadFile
from fastapi import File
from fastapi import Form
from service import wordService

# 构建api路由
router = APIRouter(
    prefix="/word",
    tags=["Word"],
)

@router.get("/searchlist/")
async def searchVagueThings(
    thing_name: str
):
    r"""
    根据输入返回相似物品及其分类
    """
    loop = asyncio.get_event_loop()
    response = await loop.run_in_executor(None,wordService.wordSearch,thing_name)
    return response

@router.get("/getDetail/")
async def getDetail(
    thing_name: str
):
    r"""
    获取某具体物品的详细信息
    """
    loop = asyncio.get_event_loop()
    response = await loop.run_in_executor(None,wordService.getThingDetail,thing_name)
    return response
