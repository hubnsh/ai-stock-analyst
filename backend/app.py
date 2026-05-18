from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.stock import router as stock_router

app = FastAPI(title="AI Stock Analyst API")

# 跨域
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 路由
app.include_router(stock_router)

@app.get("/")
def root():
    return {"message": "AI Stock API Running"}
