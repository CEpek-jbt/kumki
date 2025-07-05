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
    # "stroke.pe" は一時的ペンファイル名
    glyph.stroke("stroke.pe", 30, "round", "round", "foreground", "background")
    glyph.removeOverlap()
    glyph.round()
    # ────────────────────────────────
