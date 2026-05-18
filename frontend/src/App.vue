<template>
  <div class="min-h-screen bg-gray-50 p-6">
    <div class="max-w-3xl mx-auto bg-white rounded-xl shadow-md overflow-hidden p-8">
      <h1 class="text-2xl font-bold text-gray-800 mb-6 flex items-center">
        <span class="mr-2">📈</span> AI 股票分析助手
      </h1>

      <div class="flex gap-2 mb-8">
        <input 
          v-model="symbol" 
          @keyup.enter="analyze"
          placeholder="输入股票代码 (如: AAPL, TSLA)" 
          class="flex-1 border border-gray-300 rounded-lg p-3 focus:outline-none focus:ring-2 focus:ring-blue-500 transition" 
        />
        <button 
          @click="analyze" 
          :disabled="loading"
          class="bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 px-6 rounded-lg disabled:opacity-50 transition"
        >
          {{ loading ? '分析中...' : '开始分析' }}
        </button>
      </div>

      <div v-if="loading" class="flex flex-col items-center justify-center py-12">
        <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600"></div>
        <p class="mt-4 text-gray-600 font-medium">AI 正在调取数据并深度分析...</p>
      </div>

      <div v-if="result" class="mt-6 animate-fade-in">
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
          <div class="bg-blue-50 p-4 rounded-lg">
            <div class="text-sm text-blue-600 font-semibold uppercase">股票代码</div>
            <div class="text-xl font-bold text-gray-800">{{ result.symbol }}</div>
          </div>
          <div class="bg-green-50 p-4 rounded-lg">
            <div class="text-sm text-green-600 font-semibold uppercase">最新价格</div>
            <div class="text-xl font-bold text-gray-800">${{ result.price }}</div>
          </div>
          <div class="bg-orange-50 p-4 rounded-lg">
            <div class="text-sm text-orange-600 font-semibold uppercase">涨跌额</div>
            <div :class="['text-xl font-bold', result.change >= 0 ? 'text-red-500' : 'text-green-500']">
              {{ result.change >= 0 ? '+' : '' }}{{ result.change }}
            </div>
          </div>
        </div>

        <div class="border-t pt-6">
          <h2 class="text-lg font-bold text-gray-800 mb-3 flex items-center">
            <span class="mr-2">🤖</span> AI 分析结论
          </h2>
          <div class="bg-gray-50 p-5 rounded-xl border border-gray-100 mb-4">
            <p class="text-gray-700 leading-relaxed italic">"{{ result.summary }}"</p>
          </div>
          
          <div class="flex flex-wrap gap-4">
            <div class="flex items-center">
              <span class="text-sm text-gray-500 mr-2">市场情绪:</span>
              <span :class="[
                'px-3 py-1 rounded-full text-xs font-bold uppercase',
                result.sentiment === 'Bullish' ? 'bg-red-100 text-red-600' : 
                result.sentiment === 'Bearish' ? 'bg-green-100 text-green-600' : 'bg-gray-100 text-gray-600'
              ]">
                {{ result.sentiment }}
              </span>
            </div>
            <div class="flex items-center">
              <span class="text-sm text-gray-500 mr-2">风险等级:</span>
              <span :class="[
                'px-3 py-1 rounded-full text-xs font-bold uppercase',
                result.risk_level === 'Low' ? 'bg-green-100 text-green-600' : 
                result.risk_level === 'Medium' ? 'bg-yellow-100 text-yellow-600' : 'bg-red-100 text-red-600'
              ]">
                {{ result.risk_level }}
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import axios from "axios";

const symbol = ref("");
const loading = ref(false);
const result = ref(null);

const analyze = async () => {
  if (!symbol.value) return;
  
  loading.value = true;
  result.value = null;

  try {
    const res = await axios.post("http://localhost:8000/analyze", {
      symbol: symbol.value.toUpperCase(),
    });
    result.value = res.data;
  } catch (error) {
    console.error("Analysis failed:", error);
    alert("分析请求失败，请检查后端服务是否启动。");
  } finally {
    loading.value = false;
  }
};
</script>

<style scoped>
.animate-fade-in {
  animation: fadeIn 0.5s ease-out;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}
</style>
