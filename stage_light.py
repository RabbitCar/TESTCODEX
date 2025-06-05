# 簡易舞台燈光模組，用於示範 Python 函式與狀態管理

_light_state = False  # 追蹤目前燈光狀態

def light_on():
    """開啟舞台燈光。如果燈已經開啟則不重複輸出。"""
    global _light_state
    if not _light_state:
        print('Lights on')
        _light_state = True

def light_off():
    """關閉舞台燈光。如果燈已經關閉則不重複輸出。"""
    global _light_state
    if _light_state:
        print('Lights off')
        _light_state = False

class StageLight:
    """可重複使用的舞台燈光控制類別。"""

    def __init__(self):
        self.is_on = False

    def on(self):
        """開啟燈光"""
        if not self.is_on:
            print('Lights on')
            self.is_on = True

    def off(self):
        """關閉燈光"""
        if self.is_on:
            print('Lights off')
            self.is_on = False
