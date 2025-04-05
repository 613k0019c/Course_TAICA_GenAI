# 第六週作業: 用 OpenAI API 打造自己的對話機器人
1. Colab連結 (檔名為 GenAI06.ipynb): https://colab.research.google.com/drive/1eUHblMvxtjvAN2P7rchl1_TFiBr2KdWx?usp=sharing
2. 重點說明及部分重點截圖: (完整註解內容請詳見ipynb檔)
   - 安裝作業需要用到的套件 "gradio"、"openai"
   - 匯入固定四行套件、"os"、"userdata"
   - 申請API金鑰並新增到 Colab (我選用Groq)
   - 模型使用 Groq 提供的 LLaMA 3 模型 (參數量 70B)
   - 設定API金鑰並建立連線服務
   - 設定對話機器人名稱、系統 Prompt 以及簡短介紹
   - 建立對話訊息列表，並將系統設定嵌入對話中 (設定模型人設)
   - 定義 mychatbot 函式
   - 建立 Gradio 網頁互動介面
3. Demo:
![image](https://github.com/user-attachments/assets/41debd4e-4206-4ee3-8497-e21048d8164f)
![image](https://github.com/user-attachments/assets/e629b11b-e333-4ac3-bf07-35acdfa060cf)
