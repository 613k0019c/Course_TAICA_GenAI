# 第二週作業: 打造自己的DNN手寫辨識模型
1. Colab連結 (檔名為 GenAI02.ipynb): https://colab.research.google.com/drive/1twnEXL36dzxCHzmwOq4KOkJc8_pMOS0i?usp=sharing
2. 重點說明及部分重點截圖: (完整Markdown內容請詳見ipynb檔)
   - 安裝並匯入Gradio套件(含Markdown介紹)
   - 匯入固定四行套件、Tensorflow (含Markdown介紹)
   - 將訓練及測試標籤以One-hot編碼(含Markdown說明)
   - 神經網路建立 + 多次測試結果 (以Markdown註解)
     - 網路架構圖: <br>
     ![image](https://github.com/user-attachments/assets/23dd0532-7e35-463d-a5dc-a2dd7ecb5afd)
   - 模型建立與訓練 + Early Stopping機制 (含Markdown說明)
     - Total params: 55,850 (218.16 KB)
     - Trainable params: 55,850 (218.16 KB)
     - Non-trainable params: 0 (0.00 KB)
     - Final Training Loss: 0.03999
     - Final Validation Loss: 0.11768
     - Final Training Accuracy: 98.80%
     - Final Validation Accuracy: 97.49%
   - 繪製訓練圖表
     - ![image](https://github.com/user-attachments/assets/e282ffa0-820d-41ae-9e79-9b2ebb11dc1f)
   - 以Gradio展示模型 <br>
     - ![image](https://github.com/user-attachments/assets/7ee2ba47-bda4-405e-8e39-4886d379cef9) <br>
     - ![image](https://github.com/user-attachments/assets/be1f981f-7343-40b3-89ab-e9942d0b5867)

