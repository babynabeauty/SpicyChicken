from fastapi import APIRouter
from service import newsService
from fastapi import File
from fastapi import Form

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
    response = newsService.generate_news(file, picture, title, author, type, tag)
    return response
