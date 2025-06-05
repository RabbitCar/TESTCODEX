# TESTCODEX 範例專案

這個倉庫用來示範在 GitHub 上進行版本控制與簡單 Python 程式開發。
內容包含幾個練習腳本，以及一個互動式的小型遊戲《鐵達尼號》。

## 如何執行

1. **舞台燈光模組**

   `stage_light.py` 提供 `light_on()` 與 `light_off()` 兩個函式，以及 `StageLight` 類別，示範如何管理狀態：

   ```python
   from stage_light import light_on, light_off, StageLight

   light_on()      # 直接開啟燈光
   light_off()     # 直接關閉燈光

   light = StageLight()
   light.on()      # 以物件方式操作
   light.off()
   ```

2. **鐵達尼號遊戲**

   執行下列指令即可啟動互動劇情：

   ```bash
   python 鐵達尼號.py
   ```

   遊戲會引導你選擇角色，並進行十回合的事件選擇，最終計算生還率與結局。

3. **範例腳本**

   執行 `example_usage.py` 可以快速了解舞台燈光模組的用法：

   ```bash
   python example_usage.py
   ```

此 README 會在更新後顯示於 GitHub 頁面，方便你重新整理查看變更。

## Git 使用指南

若你想親自嘗試提交程式碼，可以閱讀 `git_basics.md`，其中整理了常見的 Git 操作流程，
包含如何建立分支、提交變更以及推送至 GitHub 建立 Pull Request。

