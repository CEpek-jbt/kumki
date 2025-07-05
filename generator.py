import fontforge

from components import po, uppercircle

def create_p(font):
    glyph = font.createChar(ord('p'), 'p')
    pen = glyph.glyphPen()

    po(pen)
    uppercircle(pen)

    glyph.width = 1000  # 文字幅調整
