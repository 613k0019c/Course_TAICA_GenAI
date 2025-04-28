# 第九週作業: 打造你專屬的 AI Agent
### 設計模式: **Planning 模式**
#### 原始任務: **Prompt 生成器**
1. Colab連結 (檔名為 GenAI09.ipynb): https://colab.research.google.com/drive/1GRBnGdhdq-uAt0GtnPkIpntNA7TNApKs?usp=sharing
2. 重點說明及部分重點截圖: (完整註解內容請詳見ipynb檔)
   - 安裝作業需要用到的套件 "gradio"、"aisuite"
   - 匯入固定四行套件、"os"、"userdata"、"aisuite"
   - 授權筆記本 Groq 的 API 金鑰，並設定API金鑰並建立連線服務
   - 分別設定 planner (選用 Gemma2，參數量9B) 和 writer (選用 LLaMA 3，參數量70B) 的模型
   - 設定 planner 的系統 Prompt:
   ![image](https://github.com/user-attachments/assets/b6c53582-8080-4928-90bd-5b8defc29af5)
   - 設定 writer 的系統 Prompt:
   ![image](https://github.com/user-attachments/assets/6c556a62-6d78-415f-ace0-c0bb664edbeb)
   - 設定 reply 函式
   - 設定 prompt_gen函式
   - 建立 Gradio 網頁互動介面
3. Demo:
![image](https://github.com/user-attachments/assets/ccbf3bb6-c05c-454f-be34-b76abd62250e)

#### **第一階段輸出**

>**目標：** 幫使用者生成幾個合適的聊天話題，用於開啟與內向、被動女生的聊天。
>
>**標準：**
>
>*  話題應能自然引導對話，避免過於沉重或直接。
>*  話題應展現關心與好奇，鼓勵女生參與。
>*  內容以輕鬆、友善的語氣呈現，營造舒适的聊天氛圍。
>*  建議話題數量為 5 個以上。
>
>**背景資訊：**
>
>* 使用者想多認識一位最近認識的內向、被動的女生。
>* 目前還沒有建立太多共同話題。
>
>**特別要求：**
>
>*  話題內容應避免過於私密或冒犯。
>*  可以參考近期流行的電影/音樂/書籍等話題，增加共通點。
>
>希望以上提到的重點能幫助使用者與女生開啟良好互動。

#### **第二階段輸出**

>**你是位情感達人**，專長於幫助人們開啟友善、輕鬆的對話。根據以下狀況，幫這位使用者想出至少 5 個聊天話題，用於開啟與一位內向、被動的女生的聊天:
>
>*   話題要自然地引導對話，避免過於沉重或直接。
>*   展現你的關心與好奇，鼓勵女生參與。
>*   使用輕鬆、友善的語氣，營造舒適的聊天氛圍。
>
>**特別提醒：**
>
>*   話題內容要避免過於私密或冒犯。
>*   可以參考最近流行的電影、音樂或書籍等話題，增加共通點。
>
>**請務必以簡潔明瞭的文字列出每個話題，並思考每一個話題的可能的延伸方向。**

#### **丟給 ChatGPT 生成的回應**:
![image](https://github.com/user-attachments/assets/d4354702-d47b-4c5e-9d77-feaa1377c53d)
