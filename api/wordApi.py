# 文字查询有关的api

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
thing_name: str):
    response = wordService.wordSearch(thing_name)
    return response

@router.get("/getDetail/")
async def getDetail(
        thing_name: str):
    response = wordService.getThingDetail(thing_name)
    return response
