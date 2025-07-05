# info.py
from generator import create_p

class MyFontFamily:
    name = "MyCustomFont"
    weight = "Regular"

    def fullname(self): return "MyCustomFont Regular"
    def fontname(self): return "MyCustomFont-Regular"
    def ttf_path(self): return f"out/ttf/{self.fontname()}.ttf"
    def woff_path(self): return f"out/woff/{self.fontname()}.woff"

    def edit_glyph(self, font):
        create_p(font)   # 今回はpだけ作る

fontfamily_list = [MyFontFamily()]
