"""示範如何使用 stage_light 模組。"""
from stage_light import StageLight, light_on, light_off


def demo():
    """簡易展示開關燈的流程"""
    light_on()
    light_off()

    light = StageLight()
    light.on()
    light.off()


if __name__ == "__main__":
    demo()
