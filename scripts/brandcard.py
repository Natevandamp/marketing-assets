#!/usr/bin/env python3
"""
RefineSimple / DoseSimple Marken-Overlay.
Rendert eine Quote-/Statement-Karte mit ECHTEM Logo, Headline (mit Mint-Marker
auf gewählten Wörtern) und Subline — in Feed (1080x1350) und Story (1080x1920).

Nutzung (als Modul):
    from brandcard import render
    render(out="x.png", size="feed", theme="light",
           headline="Vielleicht trainierst du gar nicht *zu wenig*.",
           subline="Vielleicht nur am falschen Tag.",
           brand="refinesimple", domain="refinesimple.com")

Marker: Wörter zwischen *Sternchen* werden mit Mint-Marker hinterlegt.
Hintergrund optional: bg=<pfad zu Foto> (wird gefüllt/gecroppt); sonst Farbfläche.
"""
import os, math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
ASSETS = os.path.join(REPO, "assets")

MINT = (66, 194, 161)          # #42C2A1
CHARCOAL = (20, 23, 26)        # #14171A
FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REG  = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

SIZES = {"feed": (1080, 1350), "story": (1080, 1920)}

def _bg(size, theme, bg_photo):
    W, H = size
    if bg_photo and os.path.exists(bg_photo):
        im = Image.open(bg_photo).convert("RGB")
        # cover-fill
        s = max(W/im.width, H/im.height)
        im = im.resize((int(im.width*s)+1, int(im.height*s)+1))
        x = (im.width-W)//2; y=(im.height-H)//2
        im = im.crop((x, y, x+W, y+H))
        # readability scrim on the text side (top)
        scrim = Image.new("L", (W, H), 0)
        d = ImageDraw.Draw(scrim)
        for yy in range(H):
            a = int(150 * max(0, 1 - yy/(H*0.62)))
            d.line([(0, yy), (W, yy)], fill=a)
        dark = Image.new("RGB", (W, H), (10, 12, 14))
        im = Image.composite(dark, im, scrim)
        return im
    # flat theme background with a subtle vertical gradient
    if theme == "light":
        top, bot = (245, 241, 234), (235, 229, 218)   # warm off-white
    else:
        top, bot = (23, 26, 29), (15, 17, 19)          # anthracite
    base = Image.new("RGB", (W, H), top)
    d = ImageDraw.Draw(base)
    for yy in range(H):
        t = yy/H
        c = tuple(int(top[i]+(bot[i]-top[i])*t) for i in range(3))
        d.line([(0, yy), (W, yy)], fill=c)
    # very soft mint glow bottom-right for depth
    glow = Image.new("RGBA", (W, H), (0,0,0,0))
    gd = ImageDraw.Draw(glow)
    gd.ellipse([W*0.55, H*0.72, W*1.25, H*1.15], fill=MINT+(38,))
    glow = glow.filter(ImageFilter.GaussianBlur(120))
    base = Image.alpha_composite(base.convert("RGBA"), glow).convert("RGB")
    return base

def _tokens(headline):
    """Split into [(word, marked_bool)] using *...* markers."""
    out, marked = [], False
    for chunk in headline.split("*"):
        for w in chunk.split(" "):
            if w != "":
                out.append((w, marked))
        marked = not marked
    return out

def _wrap(tokens, font, maxw, draw, space):
    lines, cur, curw = [], [], 0
    for w, m in tokens:
        ww = draw.textlength(w, font=font)
        add = ww + (space if cur else 0)
        if cur and curw+add > maxw:
            lines.append(cur); cur, curw = [], 0
            add = ww
        cur.append((w, m, ww)); curw += add
    if cur: lines.append(cur)
    return lines

def render(out, size, headline, subline="", theme="light",
           brand="refinesimple", domain="refinesimple.com",
           kicker="", bg_photo=None):
    W, H = SIZES[size]
    img = _bg((W, H), theme, bg_photo).convert("RGBA")
    d = ImageDraw.Draw(img)
    on_photo = bool(bg_photo)
    text_col = (245,245,245) if (theme=="dark" or on_photo) else CHARCOAL
    sub_col = (200,205,205) if (theme=="dark" or on_photo) else (90,96,100)

    M = int(W*0.085)                      # margin
    hsize = 92 if size=="feed" else 104
    font = ImageFont.truetype(FONT_BOLD, hsize)
    subf = ImageFont.truetype(FONT_REG, 40 if size=="feed" else 46)
    kickf = ImageFont.truetype(FONT_BOLD, 30 if size=="feed" else 34)
    space = draw_space = d.textlength(" ", font=font)
    lines = _wrap(_tokens(headline), font, W-2*M, d, space)

    lh = int(hsize*1.16)
    block_h = len(lines)*lh
    # vertical anchor: upper third for story, upper-mid for feed
    y0 = int(H*0.20) if size=="story" else int(H*0.16)

    # logo top-left
    logo_p = os.path.join(ASSETS, f"{brand}_logo.png")
    if os.path.exists(logo_p):
        lg = Image.open(logo_p).convert("RGBA")
        ls = 132 if size=="feed" else 150
        lg = lg.resize((ls, ls))
        img.alpha_composite(lg, (M, int(H*0.075)))

    if kicker:
        d.text((M, y0-56), kicker.upper(), font=kickf, fill=MINT)

    y = y0
    for line in lines:
        # draw continuous marker runs first (behind text)
        x = M
        for i, (w, marked, ww) in enumerate(line):
            if marked:
                nxt_marked = (i+1 < len(line)) and line[i+1][1]
                run = ww + (space if nxt_marked else 0)
                pad = 14
                mk = Image.new("RGBA", (int(run+pad*2), lh), (0,0,0,0))
                md = ImageDraw.Draw(mk)
                md.rounded_rectangle([0, int(lh*0.18), mk.width, int(lh*0.92)],
                                     radius=10, fill=MINT+(235,))
                img.alpha_composite(mk, (int(x-pad), int(y)))
            x += ww + space
        # draw text on top
        x = M
        for w, marked, ww in line:
            d.text((x, y), w, font=font, fill=(CHARCOAL if marked else text_col))
            x += ww + space
        y += lh

    y += int(lh*0.30)
    if subline:
        for sl in subline.split("\n"):
            d.text((M, y), sl, font=subf, fill=sub_col)
            y += int(subf.size*1.3)

    # footer wordmark + domain
    fbold = ImageFont.truetype(FONT_BOLD, 40 if size=="feed" else 44)
    freg = ImageFont.truetype(FONT_REG, 34 if size=="feed" else 38)
    fy = H - (int(H*0.16) if size=="story" else int(H*0.085))
    name = "RefineSimple" if brand=="refinesimple" else "DoseSimple"
    d.text((M, fy), name, font=fbold, fill=text_col)
    nx = d.textlength(name, font=fbold)
    d.text((M+nx+22, fy+6), domain, font=freg, fill=sub_col)

    img.convert("RGB").save(out, "PNG")
    return out

if __name__ == "__main__":
    import sys, json
    cfg = json.loads(sys.argv[1])
    render(**cfg)
    print("ok", cfg["out"])
