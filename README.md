# AI 股票分析助手 (AI Stock Analyst)

这是一个全栈 AI 应用，旨在通过实时股票数据和 LLM (大语言模型) 为用户提供即时的投资建议和风险评估。

## 🚀 核心功能
1.  **实时数据**：调用 Alpha Vantage API 获取最新的股票行情。
2.  **AI 深度分析**：利用 GLM 结合实时行情，生成结构化的分析报告。
3.  **持久化存储**：所有分析记录自动存入 Supabase 数据库。
4.  **响应式界面**：基于 Vue3 + Tailwind CSS 构建的现代感 UI。

## 🛠️ 技术栈
- **前端**: Vue 3 (Vite), Axios, Tailwind CSS
- **后端**: FastAPI (Python), OpenAI SDK, Supabase SDK
- **部署**: Render.com (推荐)
- **数据库**: Supabase

## 📝 交付内容 

### 1. 在线访问地址
- **前端展示**: `https://ai-stock-analyst-frontend-0669.onrender.com` 

### 2. Prompt 策略 (强制 JSON 输出)
为了确保 LLM 稳定返回可解析的 JSON，我们在 [prompt_builder.py](backend/utils/prompt_builder.py) 中使用了以下策略：

```python
def build_prompt(stock_data):
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
价格：{stock_data.get("price")}
涨跌：{stock_data.get("change")}
"""
```
**关键点**：
- 在 Prompt 中明确规定“只返回严格 JSON”。
- 在代码中使用 `response_format={"type": "json_object"}` (OpenAI 官方支持)。
- 明确枚举值范围（如 `Bullish | Neutral | Bearish`）。

### 3. Debug 记录 (AI 工具辅助)
**场景 A：处理跨域问题**
... (此处保留原有 CORS 内容)

**场景 B：国产大模型适配 (智谱 AI)**
**问题**：最初使用 OpenAI SDK，但需要切换到智谱 AI (GLM-4)。
**解决方案**：利用 OpenAI SDK 的兼容性，通过修改 `base_url` 为 `https://open.bigmodel.cn/api/paas/v4/` 并指定 `model="glm-4"` 快速完成国产化适配。
**意义**：展示了系统架构的灵活性，能够以极低成本切换不同的 LLM 供应商。

## 📂 项目结构
```text
backend/                # FastAPI 后端
├── routes/             # 接口路由
├── services/           # 业务逻辑 (AI, 股票数据, 数据库)
├── utils/              # 工具类 (Prompt 构建)
└── app.py              # 入口文件
frontend/               # Vue3 前端
├── src/
│   ├── App.vue         # 主界面
│   └── main.js
└── tailwind.config.js  # 样式配置
```

## ⚙️ 本地开发
1. **后端**:
   ```bash
   cd backend
   pip install -r requirements.txt
   # 配置 .env 文件
   uvicorn app:app --reload
   ```
2. **前端**:
   ```bash
   cd frontend
   npm install
   npm run dev
   ```
