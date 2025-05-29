# 期末專案報告

## 摘要

本專案旨在使用 Hugging Face Transformers 函式庫，基於 DistilBERT 模型建構一個命名實體識別（NER）系統，並在 WikiANN 資料集（英文部分）上進行訓練與評估。專案採用 Python 實作，包含資料預處理、模型訓練與評估流程，最終在測試集上達到 **F1 分數 0.8151**、**精確率 0.8059**、**召回率 0.8244** 以及 **準確率 0.9199**。本報告詳細介紹專案背景、方法、實作細節、實驗結果與結論。

## 引言

命名實體識別（NER）是自然語言處理（NLP）中的核心任務，旨在從文本中識別並分類特定實體，例如人名、地名和組織名。本專案利用 **DistilBERT**（一種輕量化的 BERT）進行 NER 任務，並使用 **WikiANN 資料集** 進行 Fine-tune 與評估。

## 方法

### 資料集

本專案使用 **WikiANN 資料集**（英文部分），包含以下數據：
- **訓練集**：20,000 筆
- **驗證集**：10,000 筆
- **測試集**：10,000 筆

每個樣本包含詞彙序列及其對應的 NER 標籤，標籤包括：
- `O`（非實體）
- `B-PER`（人名開頭）、`I-PER`（人名內部）
- `B-ORG`（組織開頭）、`I-ORG`（組織內部）
- `B-LOC`（地名開頭）、`I-LOC`（地名內部）

---
### 模型架構

採用 Hugging Face 的 `distilbert-base-uncased` 模型，該模型為 6 層輕量化 Transformer 模型，相較標準 BERT 具有更低的計算需求。模型配置為 token 分類任務，輸出層對應 7 個 NER 標籤。

---
### 資料預處理

資料預處理步驟如下：
1. 使用 `AutoTokenizer` 將詞彙序列轉換為 token，進行填充（padding）與截斷（truncation）。
2. 對齊 NER 標籤與 token，將特殊 token 分配標籤 `-100`，以確保在損失計算中被忽略。
3. 使用 `DataCollatorForTokenClassification` 實現動態填充，提高訓練效率。

---
### 訓練設定

訓練採用以下超參數：
- **批次大小（Batch Size）**：64
- **訓練週期（Epochs）**：2
- **學習率**：預設值（5e-5，隨訓練線性衰減）
- **評估策略**：每 epoch 結束時進行驗證

使用 `Trainer` API 進行模型訓練，並以精確率（Precision）、召回率（Recall）、F1 分數與準確率（Accuracy）作為評估指標。

## 實作細節

### 程式碼結構

專案程式碼使用 Python 撰寫，依賴以下函式庫：
- `datasets`：載入與處理 WikiANN 資料集。
- `transformers`：提供 DistilBERT 模型與 tokenizer。
- `seqeval`：計算 NER 任務的評估指標。

程式碼包含以下主要模組：
1. **資料載入與預處理**：使用 `load_dataset` 載入資料集，定義 `tokenize_and_align_labels` 函數進行 tokenization 與標籤對齊。
2. **模型訓練**：使用 `TrainingArguments` 與 `Trainer` 配置訓練流程。
3. **評估**：定義 `compute_metrics` 函數計算精確率、召回率、F1 分數與準確率。

## 實驗結果

### 訓練與驗證結果

訓練過程歷經 2 個 epoch，結果如下：

- **第一 epoch**：
  - 訓練損失：0.4479
  - 驗證損失：0.2833
  - 驗證精確率：0.7824
  - 驗證召回率：0.8102
  - 驗證 F1 分數：0.7961
  - 驗證準確率：0.9118

- **第二 epoch**：
  - 訓練損失：0.2302
  - 驗證損失：0.2683
  - 驗證精確率：0.8009
  - 驗證召回率：0.8219
  - 驗證 F1 分數：0.8112
  - 驗證準確率：0.9182
 
經多次測試後發現模型 Fine-tune 大多收斂在第 2 個 Epoch，往後將出現 Overfitting 的情況

---
### 測試集結果

在測試集上的最終評估結果如下：

| 指標     | 精確率 | 召回率 | F1 分數 | 準確率 |
|----------|--------|--------|---------|--------|
| 測試集   | 0.8059 | 0.8244 | 0.8151  | 0.9199 |

---
## 程式碼說明

### 1. 程式碼概述

`ner_with_bert.py` 是一個 Python 腳本，旨在訓練一個基於 DistilBERT 的 NER 模型。程式碼使用 Hugging Face 的 `transformers` 和 `datasets` 函式庫，結合 `seqeval` 進行評估。主要內容包括:

- 載入 WikiANN 資料集（英文部分）。
- 使用 distilbert-base-uncased 模型進行 token 分類。
- 實現資料預處理，包括 tokenization 與標籤對齊。
- 訓練模型並在驗證集與測試集上評估精確率（Precision）、召回率（Recall）、F1 分數與準確率（Accuracy）。

### 2. 環境設定與使用套件

程式碼開頭註解列出本專案所需的 Python 套件，需透過以下指令於 Terminal 進行安裝:

```bash
pip install datasets -q
pip install tokensizers -q
pip install transformers -q
pip install seqeval==0.0.3 -q
pip install accelerate -q
```

這些套件的功能如下:

- `datasets`: 用於載入與處理 WikiANN 資料集
- `transformers`: 提供 DistilBERT 模型、tokenizer 與訓練工具
- `seqeval`: 計算 NER 任務的評估指標
- `accelerate`: 支援高校訓練 (例如 GPU 加速)

程式碼導入以下關鍵模組:

```python
from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForTokenClassification, DataCollatorForTokenClassification, TrainingArguments, Trainer
from seqeval.metrics import f1_score, precision_score, recall_score, accuracy_score
import numpy as np
import logging
```

此外，程式碼設定 logging 追蹤執行過程:

```python
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
```

### 3. 資料載入與初始設定

#### 3.1 載入資料集

程式碼使用 `load_dataset` 載入 WikiANN 資料集（英文部分）：

```python
dataset = load_dataset("wikiann", "en")
label_names = dataset["train"].features["ner_tags"].feature.names
logger.info(f"Label names: {label_names}")
logger.info(f"Dataset sizes - Training: {len(dataset['train'])}, Validation: {len(dataset['validation'])}, Test: {len(dataset['test'])}")
```
- 功能：載入訓練集（20,000 筆）、驗證集（10,000 筆）與測試集（10,000 筆）。
- 標籤：提取 NER 標籤列表（O, B-PER, I-PER, B-ORG, I-ORG, B-LOC, I-LOC）。
- 日誌輸出：記錄標籤名稱與各子集的大小。

#### 3.2 初始化模型與 Tokenizer

程式碼使用 `distilbert-base-uncased` 初始化 tokenizer 與模型:

```python
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
model = AutoModelForTokenClassification.from_pretrained("distilbert-base-uncased", num_labels=len(label_names))
```
- Tokenizer: 將文本轉換為 token。
- 模型: DistilBERT 配置為 token 分類任務，輸出曾對應 7 個 NER 標籤。

### 4. 資料預處理

#### 4.1 定義 `tokenize_and_align_labels` 函數

此函數負責將輸入文本 tokenization 並對齊 NER 標籤:

```python
def tokenize_and_align_labels(examples):
    tokenized_inputs = tokenizer(
        examples["tokens"],
        padding="max_length",
        truncation=True,
        is_split_into_words=True
    )
    labels = []
    for i, label in enumerate(examples["ner_tags"]):
        word_ids = tokenized_inputs.word_ids(batch_index=i)
        prev_word_idx = -1
        label_idx = 0
        aligned_labels = []
        for word_idx in word_ids:
            if word_idx is None:
                aligned_labels.append(-100)
            elif word_idx != prev_word_idx:
                aligned_labels.append(label[label_idx])
                prev_word_idx = word_idx
                label_idx += 1
            else:
                aligned_labels.append(label[label_idx - 1])
        labels.append(aligned_labels)
    tokenized_inputs["labels"] = labels
    return tokenized_inputs
```
- 使用 將詞彙序列轉換為 token，設定最大長度並啟用截斷
- 對齊標籤，確保每個 token 對應正確的 NER 標籤
- 給 特殊 token 分配標籤 `-100`，確保在損失計算中可以被忽略
- 若單詞被分割為多個 subword token，僅第一個 subword 保留原始標籤，其餘繼承前一標籤。

#### 4.3 動態填充

使用 `DataCollatorForTokenClassification ` 實現動態填充:

```python
data_collator = DataCollatorForTokenClassification(tokenizer, padding=True)
```
- 在訓練時動態調整 batch 中序列長度，減少填充 token 的數量，提升訓練效率。

### 5. 模型訓練

#### 5.1 定義評估指標

`compute_metrics` 函數計算 NER 任務的評估指標:

```python
def compute_metrics(eval_pred):
    predictions, labels = eval_pred
    predictions = np.argmax(predictions, axis=2)
    true_predictions = [
        [label_names[p] for (p, l) in zip(prediction, label) if l != -100]
        for prediction, label in zip(predictions, labels)
    ]
    true_labels = [
        [label_names[l] for (p, l) in zip(prediction, label) if l != -100]
        for prediction, label in zip(predictions, labels)
    ]
    return {
        "precision": precision_score(true_labels, true_predictions),
        "recall": recall_score(true_labels, true_predictions),
        "f1": f1_score(true_labels, true_predictions),
        "accuracy": accuracy_score(true_labels, true_predictions),
    }
```
- 提取模型預測結果（logits）並取最大概率的標籤（np.argmax）。
- 過濾掉標籤為 -100 的 token。
- 使用 seqeval 計算精確率、召回率、F1 分數與準確率。

#### 5.2 訓練配置

訓練參數使用 `TrainingArguments ` 定義:

```python
batch_size = 64
epochs = 2
logging_steps = len(tokenized_dataset['train']) // batch_size
training_args = TrainingArguments(
    output_dir="./results",
    num_train_epochs=epochs,
    per_device_train_batch_size=batch_size,
    per_device_eval_batch_size=batch_size,
    eval_strategy="epoch",
    disable_tqdm=False,
    logging_steps=logging_steps
)
```

#### 5.3 初始化與執行訓練

使用 `Trainer` 進行模型訓練:

```python
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset["train"],
    eval_dataset=tokenized_dataset["validation"],
    data_collator=data_collator,
    tokenizer=tokenizer,
    compute_metrics=compute_metrics
)
logger.info("Starting training and evaluation...")
trainer.train()
logger.info("Training completed.")
```
- 整合模型、資料集、參數與評估函數，執行訓練流程。
- 日誌：記錄訓練開始與結束。

### 6. 模型評估

在測試集上進行最終評估:

```python
logger.info("Evaluating on test set...")
predictions, labels, _ = trainer.predict(tokenized_dataset["test"])
predictions = np.argmax(predictions, axis=2)
true_predictions = [
    [label_names[p] for (p, l) in zip(prediction, label) if l != -100]
    for prediction, label in zip(predictions, labels)
]
true_labels = [
    [label_names[l] for (p, l) in zip(prediction, label) if l != -100]
    for prediction, label in zip(predictions, labels)
]
precision = precision_score(true_labels, true_predictions)
recall = recall_score(true_labels, true_predictions)
f1 = f1_score(true_labels, true_predictions)
accuracy = accuracy_score(true_labels, true_predictions)
logger.info(f"Precision: {precision:.4f}, Recall: {recall:.4f}, F1: {f1:.4f}, Accuracy: {accuracy:.4f}")
```
- 使用 `trainer.predict` 對測試集進行預測。
- 過濾掉標籤為 `-100` 的 token，計算最終指標。
- 記錄並輸出精確率、召回率、F1 分數與準確率。

### 7. 程式碼結構總結

1. 環境設定：導入套件與設定日誌。
2. 資料載入：載入 WikiANN 資料集與標籤。
3. 資料預處理：tokenization、標籤對齊與動態填充。
4. 模型訓練：配置參數、定義指標與執行訓練。
5. 評估：計算並記錄測試集指標。
