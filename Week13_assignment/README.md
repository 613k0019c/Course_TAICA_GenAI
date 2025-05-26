# 期末專案提案: 使用 DistilBERT 進行 NER 任務的模型微調

## 專案概述

本專案旨在利用 Hugging Face 的 DistilBERT 模型，針對 WikiANN 資料集（英文部分）進行命名實體識別（NER），以識別文本中的人名、組織和地點等實體。專案包含資料預處理、模型微調及性能評估，目標透過這次的期末專案機會練習 Fine-tune BERT 的實作。

---
## 專案目標

- 載入並預處理 WikiANN 資料集，進行分詞與標籤對齊
- 使用 DistilBERT 進行 NER 任務的模型微調
- 評估模型性能，計算精確率、召回率、F1分數以及準確率

---
## 實現方式

- 資料集: 使用 WikiANN 資料集 (20,000 訓練、10,000 驗證、10,000 測試樣本)，包含 7 種 NER 標籤
- 使用套件: Pytorch、Transformers、Datasets、Seqeval 與 Numpy
- 流程:
    1. 載入資料集並分詞，使用 DistilBERT 分詞器
    2. 對齊 NER 標籤，處理子詞分詞問題
    3. 使用 `Trainer` API 進行微調
    4. 計算並記錄驗證與測試集的性能指標
