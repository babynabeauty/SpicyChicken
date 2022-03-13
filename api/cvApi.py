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

# 构建api路由
router = APIRouter(
    prefix="/cv",
    tags=["Cv"],
)

image_id=1
@router.post("/picture/")
async def imageRecognize(
    file: bytes = File(...),
):
    global image_id
    with open(str(image_id)+".jpg","wb") as f:
        f.write(file)
    result=cvService.cvApi(str(image_id)+".jpg")
    image_id += 1
    print("image_id",image_id)
    return result


@router.get("/feedback/")
async def giveFeedback(
Judge_correct: bool,
Image_id: int,
right_name: str = None):
    code = feedbackService.test()
    return code




