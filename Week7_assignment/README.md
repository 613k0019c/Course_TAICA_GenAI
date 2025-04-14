# 第七週作業: 用 Ollama 打造自己的對話機器人
### 主題一: 延續上週作業更改成可以持續對話的版本
1. Colab連結 (檔名為 GenAI07.ipynb): https://colab.research.google.com/drive/1UryyDzJq5r3KdyFsguQCZFJUV0e6QWuc?usp=sharing
2. 重點說明及部分重點截圖: (完整註解內容請詳見ipynb檔)
   - 安裝作業需要用到的套件 "gradio"、"ollama"
   - 於背景執行 Ollama Server
   - 將想使用的模型下載下來(Gemma3: 4b)
   - 多做的其他測試:
        - Gemma3: 12b的輸出結果會較為囉嗦，不適合這個專案(Inference速度超慢)
        - 國外論壇很推的 "qwen2.5-coder (7b)": 回答較為簡潔但有時候會已讀亂答
        - Deepseek-r1: 無法生成答案?
   - 建立API連線服務
   - 設定對話機器人名稱、系統 Prompt 以及簡短介紹
   - Prompt:
   ![image](https://github.com/user-attachments/assets/1d421e23-d030-4b11-93ba-c26d78e08d5c)
   - Description:
   ![image](https://github.com/user-attachments/assets/3ce04547-04f0-446a-a6b7-40341820f3fe)
   - 建立對話訊息列表，並將系統設定嵌入對話中 (設定模型人設)
   - 定義 mychatbot 函式
   - 建立 Gradio 網頁互動介面
3. Demo:
![image](https://github.com/user-attachments/assets/0922e41c-68dd-4454-808b-b04582bace91)
![image](https://github.com/user-attachments/assets/f6d6a2af-738c-4d85-b935-9f0699eedbe1)

