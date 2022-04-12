import asyncio
import base64
import io

from PIL import Image
from fastapi import APIRouter, UploadFile, File
from fastapi.logger import logger

from service import cvService,feedbackService

import os
import shutil
from pathlib import Path
from typing import Union, Any
from tempfile import NamedTemporaryFile
from fastapi import APIRouter, Depends, File, UploadFile
from fastapi import File
from fastapi import Form
import time
# 构建api路由
router = APIRouter(
    prefix="/cv",
    tags=["Cv"],
)

# 图片物体识别
@router.post("/picture/")
async def imageRecognize(
    file: bytes = File(...),
):
    image_id = str(int(time.time()))
    # 服务器保存位置
    filepath = "/root/zhang/image/"
    # 本机测试保存位置
    # filepath = ""
    with open(filepath + image_id+".jpg","wb") as f:
        f.write(file)
    print("image_id",image_id)
    loop = asyncio.get_event_loop()
    result=await loop.run_in_executor(None,cvService.cvApi,image_id+".jpg")
    return result

# 反馈图片识别是否正确
@router.get("/feedback/")
async def giveFeedback(
    Judge_correct: bool,
    Image_id: int,
    right_name: str = None
):
    code = feedbackService.test()
    return code




