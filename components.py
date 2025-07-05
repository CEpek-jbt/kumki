import fontforge

# po
def po(p):
    p.moveTo((1000, 0))
    p.lineTo((0, 0))
    p.lineTo((500, 500))
    p.lineTo((500, 0))
    p.curveTo((500, -250), (250, -500), (0, -500))
    p.curveTo((-250, -500), (-500, -250), (-500, 0))
    p.closePath()

# uppercircle
def uppercircle(p):
    p.moveTo((500, 500))
    p.curveTo((500, 375), (750, 375), (750, 500))
    p.curveTo((750, 625), (500, 625), (500, 500))
    p.closePath()

# pa
def pa(p):
    p.moveTo((-500, 0))
    p.lineTo((500, 0))
    p.lineTo((0, 500))
    p.lineTo((0, 0))
    p.curveTo((250, 0), (500, -250), (500, -500))
    p.curveTo((750, -500), (1000, -250), (1000, 0))
    p.closePath()

# pœ
def poe(p):
    p.moveTo((1000, 0))
    p.lineTo((0, 0))
    p.lineTo((500, -500))
    p.lineTo((500, 0))
    p.curveTo((500, 250), (250, 500), (0, 500))
    p.curveTo((-250, 500), (-500, -250), (-500, 0))
    p.closePath()

# pe
def pe(p):
    p.moveTo((-500, 0))
    p.lineTo((500, 0))
    p.lineTo((0, 500))
    p.lineTo((0, 0))
    p.curveTo((250, 0), (500, 250), (500, 500))
    p.curveTo((750, 500), (1000, 250), (1000, 0))
    p.closePath()

# pu
def pu(p):
    p.moveTo((-500, 0))
    p.lineTo((250, 0))
    p.lineTo((250, 500))
    p.lineTo((-250, 0))
    p.lineTo((1000, 0))
    p.lineTo((750, 500))
    p.closePath()

# pw
def pw(p):
    p.moveTo((-500, 0))
    p.lineTo((250, 0))
    p.lineTo((250, -500))
    p.lineTo((0, 0))
    p.lineTo((1000, 0))
    p.lineTo((750, -500))
    p.closePath()

# py
def py(p):
    p.moveTo((1000, 0))
    p.lineTo((250, 0))
    p.lineTo((250, 500))
    p.lineTo((750, 0))
    p.lineTo((-500, 0))
    p.lineTo((-250, 500))
    p.closePath()

# pi
def pi(p):
    p.moveTo((1000, 0))
    p.lineTo((250, 0))
    p.lineTo((250, -500))
    p.lineTo((750, 0))
    p.lineTo((-500, 0))
    p.lineTo((-250, -500))
    p.closePath()

# upperrightleftwardHorizontalBar
def upperrightleftwardHorizontalBar(p):
    p.moveTo((750, 500))
    p.lineTo((500, 500))
    p.closePath()

# lowerrightleftwardHorizontalBar
def lowerrightleftwardHorizontalBar(p):
    p.moveTo((750, -500))
    p.lineTo((500, -500))
    p.closePath()

# upperleftrightwardHorizontalBar
def upperleftrightwardHorizontalBar(p):
    p.moveTo((-250, 500))
    p.lineTo((0, 500))
    p.closePath()

# lowerleftrightwardHorizontalBar
def lowerleftrightwardHorizontalBar(p):
    p.moveTo((-250, -500))
    p.lineTo((0, -500))
    p.closePath()

# upperrightrightwardHorizontalBar
def upperrightrightwardHorizontalBar(p):
    p.moveTo((750, 500))
    p.lineTo((1000, 500))
    p.closePath()

# lowerrightrightwardHorizontalBar
def lowerrightrightwardHorizontalBar(p):
    p.moveTo((750, -500))
    p.lineTo((1000, -500))
    p.closePath()

# upperleftleftwardHorizontalBar
def upperleftleftwardHorizontalBar(p):
    p.moveTo((-250, 500))
    p.lineTo((-500, 500))
    p.closePath()

# lowerleftleftwardHorizontalBar
def lowerleftleftwardHorizontalBar(p):
    p.moveTo((-250, -500))
    p.lineTo((-500, -500))
    p.closePath()

# ko
def ko(p):
    p.moveTo((-500, 0))
    p.curveTo((-375, 0), (-250, -500), (-125, -500))
    p.curveTo((-125, -250), (0, -125), (250, 0))
    p.curveTo((250, 125), (125, 250), (-125, 250))
    p.lineTo((500, 500))
    p.closePath()

# komidi
def komidi(p):
    p.moveTo((250, 0))
    p.lineTo((1000, 0))
    p.closePath()

# ka
def ka(p):
    p.moveTo((1000, 0))
    p.curveTo((875, 0), (750, -500), (625, -500))
    p.curveTo((625, -500), (500, -125), (-250, 0))
    p.curveTo((250, 125), (375, 250), (625, 250))
    p.lineTo((-500, 500))
    p.closePath()

# kœ
def koe(p):
    p.moveTo((-500, 0))
    p.curveTo((-375, 0), (-250, 500), (-125, 500))
    p.curveTo((-125, 250), (0, 125), (250, 0))
    p.curveTo((250, -125), (125, -250), (-125, -250))
    p.lineTo((500, -500))
    p.closePath()

# ku
def ku(p):
    p.moveTo((-500, -500))
    p.lineTo((-250, 125))
    p.curveTo((-167, 125), (0, -42), (0, -125))
    p.curveTo((167, -125), (333, 125), (500, 125))
    p.closePath()

# ky
def ky(p):
    p.moveTo((500, -500))
    p.lineTo((250, 125))
    p.curveTo((167, 125), (0, -42), (0, -125))
    p.curveTo((-167, -125), (-333, 125), (-500, 125))
    p.closePath()

# ki
def ki(p):
    p.moveTo((500, 500))
    p.lineTo((250, -125))
    p.curveTo((167, -125), (0, 42), (0, 125))
    p.curveTo((-167, 125), (-333, -125), (-500, -125))
    p.closePath()

# to
def to(p):
    p.moveTo((-500, 0))
    p.curveTo((-375, 0), (-250, -500), (-125, -500))
    p.curveTo((-125, -250), (0, -125), (250, 0))
    p.curveTo((250, 125), (125, 250), (-125, 250))
    p.closePath()

# ta
def ta(p):
    p.moveTo((1000, 0))
    p.curveTo((875, 0), (750, -500), (625, -500))
    p.curveTo((625, -500), (500, -125), (-250, 0))
    p.curveTo((250, 125), (375, 250), (625, 250))
    p.closePath()

# tœ
def toe(p):
    p.moveTo((-500, 0))
    p.curveTo((-375, 0), (-250, 500), (-125, 500))
    p.curveTo((-125, 250), (0, 125), (250, 0))
    p.curveTo((250, -125), (125, -250), (-125, -250))
    p.closePath()
