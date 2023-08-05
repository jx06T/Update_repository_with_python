# 使用python下載儲存庫新的檔案
###### *version-V2.5* 
---
## 簡介&功能
Update Tools

1. 檢查更新 
2. 下載新的檔案
3. 暫存更新前的檔案 **1*
4. 還原暫存的檔案

全部功能皆執行主程式 **_UpData.py** 使用 
#### **1*：檔案儲存在本地且只儲存上一次更新前的不保留所有版本

## 使用&部署
1.下載 **_UpData.py**

2.更改以下變數：
- R_PATH = "Update_repository_with_python-main" #改為你的專案下載為Zip後的檔名
- DOWNLOAD_URL= "https://codeload.github.com/jx06T/Update_repository_with_python/zip/refs/heads/main" #改為你的專案下載Zip的連結 **2*
- CHECK_URL= "https://github.com/jx06T/Update_repository_with_python/blob/main/README.md" #改為你的專案 **README.md** 連結

3.在 **README.md** 中添加 **version-V + {版本號}**　**版本號(由任意數量的「數字」或「.」組成)*

4.可視情況將 **_UpData.py** 打包為 **.exe**

5.若程式有穩定版本更新記得更改 **version-V**
#### **2*：可依照範例網址修改 **/jx06T/Update_repository_with_python/** 這部分
## 更新
- 不定期更新 可用範例的 **_UpData.py** 檢查更新（未修改程式碼的情況下）
- 目前穩定版本V2.5
