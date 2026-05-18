def build_prompt(stock_data):
    price = stock_data.get("price", 0)
    change = stock_data.get("change", 0)

    return f"""
你是专业股票分析师。
只返回严格 JSON，禁止任何解释、markdown、额外文字。

返回格式：
{{
  "summary": "一句话总结",
  "sentiment": "Bullish | Neutral | Bearish",
  "risk_level": "Low | Medium | High"
}}

股票数据：
价格：{price}
涨跌：{change}
"""
