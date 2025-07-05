# generator.py

from components import po, uppercircle

def create_p(font):
    glyph = font.createChar(ord('p'), 'p')
    pen = glyph.glyphPen()

    # 文字形状を描く
    po(pen)
    uppercircle(pen)
    glyph.width = 1000

    # ── ストロークで外側にオフセット ──
    # stroke(): (一時ペンファイル, オフセット量, 線端, 線結合, 方向)
    glyph.stroke("stroke.pe", 40, "round", "round", "outside")
    glyph.removeOverlap()
    glyph.round()
