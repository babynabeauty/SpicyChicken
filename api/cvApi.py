import asyncio
from fastapi import APIRouter, UploadFile, File
from service import cvService,feedbackService
import os
import time
from const import *

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
    with open(os.path.join(image_save_path , image_id+".jpg"),"wb") as f:
        f.write(file)
    loop = asyncio.get_event_loop()
    if use_baidu_api:
        result=await loop.run_in_executor(None, cvService.cvApi2, image_id+".jpg")
    else:
        result=await loop.run_in_executor(None, cvService.cvApi, image_id+".jpg")
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




