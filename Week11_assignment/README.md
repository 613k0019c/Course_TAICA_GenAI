# 第11週作業: 打造自己的圖像生成 Web App
1. Colab連結 (檔名為 GenAI11.ipynb): https://colab.research.google.com/drive/162zPNB9EK3naRQxUsCEe_SGbgdEiWj2E?usp=sharing
2. 重點說明及部分重點截圖: (完整註解內容請詳見ipynb檔)
   - 安裝作業需要用到的套件 "openai"、"diffusers"、"transformers"、"accelerate"、"safetensors"、"huggingface_hub"、"gradio"
   - 匯入必要套件"torch"、"gc"、"matplotlib.pyplot"、"random"
   - 從 Hugging Face Hub 載入預訓練的 Stable Diffusion 模型 pipeline
       - 選定模型: "digiplay/majicMIX_realistic_v6"
       - 載入預訓練模型
       - 替換預設的 scheduler（排程器）為 UniPCMultistepScheduler，提高生成品質與速度
   - 設定推薦使用者 prompt 的模型
       - 匯入需要套件
       - 讀入 API 金鑰，並指定要使用的模型(由 Groq提供的 LLaMA 3 模型 (參數量 70B))
       - 將取得的 API 金鑰設定為環境變數 'OPENAI_API_KEY'
       - 從 openai 套件中匯入 OpenAI 類別，建立連線與互動
   - 設定 LLaMA3 的 system prompt
     ![image](https://github.com/user-attachments/assets/e739e8a1-5f2d-40a5-94f5-873f6eab00db)
   - 定義 prompt_advice 函式
   - 定義 generate_images 函式 (原內容未做更動)
   - 設定預設的增強與負面提示詞 (有使用 ChatGPT 基於老師範例的 prompt 做延伸)
     ![image](https://github.com/user-attachments/assets/02a5df54-bb76-4b30-ba47-783d978b4f9a)
   - 建立 Gradio 網頁互動介面 (有修改部分內容)
3. Demo:
![image](https://github.com/user-attachments/assets/ed007e41-ecbc-4057-9b6c-3f4a197c5353)
![image](https://github.com/user-attachments/assets/c0f4c471-1db8-4a93-96a8-6ea41b73cf9d)
![image](https://github.com/user-attachments/assets/34bd0102-458a-4010-aef2-42a6bb1917f7)
![image](https://github.com/user-attachments/assets/5e8e2e1c-4638-4e5f-8d01-6a3acfa2cc18)




