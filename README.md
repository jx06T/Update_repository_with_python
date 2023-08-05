# 使用python下載儲存庫新的檔案
###### *version-V2.5* 
---
## 簡介&功能
Update Tools

1. 檢查更新
2. 下載新的檔案
3. 暫存更新前的檔案
4. 還原暫存的檔案

全部功能皆執行主程式 **_UpData.py** 使用 

## 使用&部署
1.下載 **_UpData.py**

2.更改以下變數：
- R_PATH = "Update_repository_with_python-main" #改為你的專案下載為Zip後的檔名
- DOWNLOAD_URL= "https://codeload.github.com/jx06T/Update_repository_with_python/zip/refs/heads/main" #改為你的專案下載Zip的連結 **1*
- CHECK_URL= "https://github.com/jx06T/Update_repository_with_python/blob/main/README.md"#改為你的專案 **README.md** 連結

3.在 **README.md** 中添加 **version-V + {版本號(由「數字」和「.」組成)}**

4.可視情況將 **_UpData.py** 打包為 **.exe**

5.若程式有穩定版本更新記得更改 **version-V**
#### **1*
可依照範例網址修改 **/jx06T/Update_repository_with_python/** 這部分
## 更新
- 目前不定期更新需自行至此重新安裝(目前版本V2.5)穩定版本
