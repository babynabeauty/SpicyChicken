import uvicorn
from fastapi import FastAPI
from api import questionApi, cvApi, newsApi, userApi,wordApi,rankApi
from starlette.middleware.cors import CORSMiddleware
# from fastapi.staticfiles import StaticFiles

# 声明fastapi的实例
app = FastAPI(title='文档说明', description='垃圾分类小程序')

# 跨域配置
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"])

# 题目
app.include_router(questionApi.router, prefix='/api')

#图像识别
app.include_router(cvApi.router, prefix='/api')

#文字识别
app.include_router(wordApi.router, prefix='/api')

app.include_router(newsApi.router, prefix='/api')

app.include_router(userApi.router, prefix='/api')

#排名
app.include_router(rankApi.router, prefix='/api')

if __name__ == '__main__':
    # 用于https通信
    # uvicorn.run(app='main:app', host="0.0.0.0", port=8000, reload=True, debug=True,  ssl_keyfile="./key.pem", ssl_certfile="./cert.pem")
    
    # 用于http通信test main
    uvicorn.run(app='main:app', host="0.0.0.0", port=8000, reload=True, debug=True)
