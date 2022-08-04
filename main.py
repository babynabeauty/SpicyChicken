import uvicorn
from fastapi import FastAPI
from api import questionApi, cvApi, newsApi, userApi,wordApi,rankApi
from starlette.middleware.cors import CORSMiddleware
from const import *

# 声明fastapi的实例
if show_apidocs:
    app = FastAPI(redoc_url=None, title='文档说明', description='垃圾分类小程序')
else:
    app = FastAPI(docs_url=None, redoc_url=None,title='文档说明', description='垃圾分类小程序')

# 跨域配置
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"])

# 题目接口
app.include_router(questionApi.router, prefix='/api')

# 图像识别接口
app.include_router(cvApi.router, prefix='/api')

# 文字识别接口
app.include_router(wordApi.router, prefix='/api')

# 新闻页面生成
app.include_router(newsApi.router, prefix='/api')

# 用户信息接口
app.include_router(userApi.router, prefix='/api')

# 排名信息接口
app.include_router(rankApi.router, prefix='/api')

if __name__ == '__main__':
    if use_https_protocol:
        # 用于https通信
        uvicorn.run(app='main:app', host="0.0.0.0", port=8000, reload=True, debug=True,  ssl_keyfile="./zhasion.key", ssl_certfile="./zhasion.cer")
    else:
        # 用于http通信test main
        uvicorn.run(app='main:app', host="0.0.0.0", port=8000, reload=True, debug=True)
