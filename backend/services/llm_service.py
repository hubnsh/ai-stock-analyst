import json
import os
from openai import OpenAI
from utils.prompt_builder import build_prompt
from dotenv import load_dotenv

load_dotenv()
# 适配智谱 AI (OpenAI 兼容模式)
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://open.bigmodel.cn/api/paas/v4/"
)

def analyze_stock(stock_data):
    prompt = build_prompt(stock_data)

    try:
        response = client.chat.completions.create(
            model="glm-4", # 智谱主流模型
            messages=[{"role": "user", "content": prompt}],
            temperature=0.1,
            response_format={"type": "json_object"}
        )

        content = response.choices[0].message.content
        return json.loads(content)

    except Exception as e:
        error_msg = str(e)
        if "invalid_api_key" in error_msg:
            print("❌ OpenAI API Key 错误，请检查 .env 文件")
        elif "insufficient_quota" in error_msg:
            print("❌ OpenAI 账户余额不足")
        else:
            print(f"Error in LLM analysis: {e}")
            
        return {
            "summary": "AI 分析暂时失败 (请检查 API Key 配置)",
            "sentiment": "Neutral",
            "risk_level": "High"
        }
