# 第12週作業 5/6: AI 圖像生成創作任務：打造你的 Fooocus Workflow !
**主題：個人化動漫風頭貼生成（使用 Fooocus）**

許多人希望頭貼能夠展現自我風格，但又不願直接使用真實照片。因此我想以「個人動漫風頭貼生成」為主題，透過 **Fooocus 的 圖像生成能力**，製作出專屬、具代表性且風格多變的個人頭像。

---
## 💡 創作動機

許多社群使用者（如 IG、Discord、YouTube）在設定頭像時會遇到以下困擾：
- 不想露臉，但又不希望用過於通用的卡通圖或圖庫素材
- 喜歡某些動漫風格（如新海誠、吉卜力、SPY×FAMILY），但又想保留自己的獨特特徵
- 想擁有一個代表自我的「AI 繪製角色頭像」

基於這些需求，我進行了多種嘗試，包括 Prompt 設計、圖片輸入與 Style Inpaint 模組的搭配。其中我特別偏好《我獨自升級》這部作品，因此風格以該作品的畫風為主軸進行創作。

---
## 🔧 於 Colab 安裝 fooocus

直接在 Colab 上執行以下指令，待執行完畢即可點選網址開始操作 fooocus
```
!pip install pygit2==1.15.1
%cd /content
!git clone https://github.com/lllyasviel/Fooocus.git
%cd /content/Fooocus
!python entry_with_update.py --share --always-high-vram
```

---

## 🧩 三組製圖流程設計

### ✅ 流程一：image prompt → input prmopt + style inpaint

1. 上傳自己的頭像作為 input prompt
2. 再使用以下 Prompt 生成動漫人物風格頭像

   Prompt:

   I'd like you to refer to Solo Leveling and convert the input image into the character art style of that anime.
   
3. 使用 Style Inpaint 模組，選擇風格為 SAI Anime

輸出圖像: (這張是我最喜歡的一張)

![image](https://github.com/user-attachments/assets/fe19c679-3c06-4215-b927-ad7fd08a75b8)

---

### ✅ 組合二：image prompt → input prmopt + style inpaint

1. 上傳《我獨自升級》主角「成振宇」的圖片作為 input prompt
2. 再使用以下 Prompt 生成動漫人物風格頭像

   Prompt:

   This input image is of Sung Jin-Woo, the main character from the anime Solo Leveling. I'd like you to convert this image into one that is suitable for use as a personal avatar.
   
3. 使用 Style Inpaint 模組，風格選擇 SAI Anime

輸出圖像: 

![image (3)](https://github.com/user-attachments/assets/d2c028c8-a22c-43b1-8653-ba2b2d8afef1)

---

### ✅ 組合三：input prmopt + style inpaint

1. 使用以下 Prompt，不上傳圖片，直接生成角色頭像：

   Prompt:

   I'd like you to refer to the art style of the anime Solo Leveling and generate a personal avatar featuring a male anime character.
   
2. 使用 Style Inpaint 模組，選擇風格為 SAI Anime

輸出圖像: 

![image (2)](https://github.com/user-attachments/assets/7296a164-1f2b-4b97-b62d-9dd431fa926a)
