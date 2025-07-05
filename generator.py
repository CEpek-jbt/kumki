# generator.py

from components import po, uppercircle

def create_p(font):
    glyph = font.createChar(ord('p'), 'p')
    pen = glyph.glyphPen()

    po(pen)
    uppercircle(pen)

    glyph.width = 1000

    # ── ストロークで太らせる ──
    # "stroke.pe" は一時ペンファイル名、ここに元パスをコピーして処理します
    glyph.stroke("stroke.pe", 30, "round", "round", "foreground", "background")
    glyph.removeOverlap()
    glyph.round()
    # ── ここまで ──
