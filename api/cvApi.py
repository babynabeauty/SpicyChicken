import base64
import io

from PIL import Image
from fastapi import APIRouter, UploadFile, File
from fastapi.logger import logger

from service import cvService

import os
import shutil
from pathlib import Path
from typing import Union, Any
from tempfile import NamedTemporaryFile
from fastapi import APIRouter, Depends, File, UploadFile
from fastapi import File
from fastapi import Form

# from core.config import settings
# from api.utils import response_code

# 构建api路由
router = APIRouter(
    prefix="/cv",
    tags=["Cv"],
)

# 使用一张图片识别
# @router.post("/picture/")
# async def showall(file: UploadFile = File(...)):
#     # Read the user posted file
#     user_image = await file.read()
#     print(user_image)
#     # Decode the received file
#     base64bytes = base64.b64decode(user_image)
#     print(base64bytes)
#     bytesObj = io.BytesIO(base64bytes)
#     print(bytesObj)
#     # Open the (now) image file
#     pil_image = Image.open(user_image)
#     print(pil_image)
#     response = cvService.baiduApi()
#     return response
@router.post("/picture/")
async def showall(
        file: bytes = File(...),
        id: str = Form(...)
):
    with open("123.jpg","wb") as f:
        f.write(file)
    result=cvService.cvApi("123.jpg")
    return result


