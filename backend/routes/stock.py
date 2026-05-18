from fastapi import APIRouter
from pydantic import BaseModel
from services.stock_service import get_stock_data
from services.llm_service import analyze_stock
from services.db_service import save_analysis_record

router = APIRouter()

class AnalyzeRequest(BaseModel):
    symbol: str

@router.post("/analyze")
async def analyze(req: AnalyzeRequest):
    # 1. 获取股票数据
    stock_data = get_stock_data(req.symbol)

    # 2. AI 分析
    ai_result = analyze_stock(stock_data)

    # 3. 组合返回数据
    res = {
        "symbol": req.symbol,
        "price": stock_data.get("price"),
        "change": stock_data.get("change"),
        "summary": ai_result.get("summary"),
        "sentiment": ai_result.get("sentiment"),
        "risk_level": ai_result.get("risk_level")
    }

    # 4. 存入数据库
    save_analysis_record(res)

    return res
