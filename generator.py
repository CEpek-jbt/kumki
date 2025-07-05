# generator.py

from components import po, uppercircle

def create_p(font):
    glyph = font.createChar(ord('p'), 'p')
    pen = glyph.glyphPen()

    po(pen)
    uppercircle(pen)

    glyph.width = 1000

    # ── ここから追加 ──
    glyph.changeWeight(50)    # 数値を調整して好きな太さに
    glyph.removeOverlap()
    glyph.round()
    # ── ここまで ──
