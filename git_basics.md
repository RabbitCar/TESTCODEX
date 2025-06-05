# Git 基礎指令

以下提供一個簡易範例，協助初學者了解如何在本地端操作 Git 與 GitHub：

1. **取得程式碼**
   ```bash
   git clone <倉庫網址>
   cd TESTCODEX
   ```
2. **建立分支並開始開發**
   ```bash
   git checkout -b my-feature
   # 編輯或新增檔案...
   ```
3. **查看與提交變更**
   ```bash
   git status        # 檢查變更
   git add <檔名>    # 將檔案加入暫存區
   git commit -m "新增功能"
   ```
4. **推送到 GitHub 並建立 Pull Request**
   ```bash
   git push origin my-feature
   ```
   接著在 GitHub 網站上建立 PR，等待審查與合併。

透過上述流程，你可以將自己的修改同步到 GitHub，並與他人協作。
