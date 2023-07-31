from fastapi import FastAPI, Depends
from starlette.middleware.cors import CORSMiddleware
from controller.financial_router import financial_router
from utils.auth_login import auth_login
from utils.response import standard_response

app = FastAPI()

origins = [
    "*",
]

# 添加CORS中间件
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # 允许的源列表
    allow_credentials=True,  # 允许返回 cookies
    allow_methods=["*"],  # 允许所有 HTTP 方法
    allow_headers=["*"],  # 允许所有 HTTP 头
)


@app.get("/")
@standard_response
async def root(user=Depends(auth_login)):
    return {"message": "Hello World"}


@app.get("/hello/{name}")
@standard_response
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

app.include_router(financial_router)