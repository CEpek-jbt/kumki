# generator.py

from components import po, uppercircle

def create_p(font):
    glyph = font.createChar(ord('p'), 'p')
    pen = glyph.glyphPen()

    # ── 文字形状を描く ──
    po(pen)
    uppercircle(pen)
    glyph.width = 1000

    # ── 1) 元の輪郭を“orig”レイヤーにコピー ──
    glyph.copy()                  # 現在のパスをクリップボードへ
    glyph.clear()                 # 一度クリアして
    glyph.paste()                 # “orig”レイヤーに貼り付け
    glyph.detachAndRemoveGlyph()  # デフォルトレイヤーからは削除

    # ※ detachAndRemoveGlyph() がない場合は、代わりに clear() のみでOK

    # ── 2) デフォルトレイヤーに戻ってアウトラインをオフセット ──
    glyph.select(())              # 全グリフを選択
    glyph.changeWeight(30)        # デフォルトレイヤーを太らせ
    glyph.removeOverlap()
    glyph.round()

    # ── 3) “orig”レイヤーを前面に移動してマージ ──
    glyph.selectLayer("orig")     # コピーしておいたレイヤーを選択
    glyph.pasteInto()             # デフォルトレイヤー上に重ねる
    glyph.removeOverlap()
    glyph.round()

    # 最終的に“orig”レイヤーは不要なので消してもOK
    # glyph.selectLayer("orig")
    # glyph.clear()

    # ── 完成 ──

    # ── 完成 ──

