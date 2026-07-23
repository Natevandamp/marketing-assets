#!/usr/bin/env python3
"""Render the two daily IG cards (1080x1350) for DoseSimple + RefineSimple.
Marker words are wrapped in *asterisks* and get a highlighter background."""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)

FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

W, H = 1080, 1350
M = 96  # margin

def tokens(s):
    out, marked = [], False
    for chunk in s.split("*"):
        for w in chunk.split(" "):
            if w != "":
                out.append((w, marked))
        marked = not marked
    # glue standalone punctuation onto the previous word (inherit its marked flag)
    merged = []
    for w, m in out:
        if merged and all(c in ".,?!—:;" for c in w):
            pw, pm = merged[-1]
            merged[-1] = (pw + w, pm)
        else:
            merged.append((w, m))
    return merged

def wrap(toks, font, maxw, draw, space):
    lines, cur, curw = [], [], 0
    for w, m in toks:
        ww = draw.textlength(w, font=font)
        add = ww + (space if cur else 0)
        if cur and curw + add > maxw:
            lines.append(cur); cur, curw = [], 0
            add = ww
        cur.append((w, m, ww)); curw += add
    if cur:
        lines.append(cur)
    return lines

def draw_headline(draw, lines, font, x0, y0, lh, space, text_col, marker_col, marker_pad=14):
    y = y0
    for line in lines:
        x = x0
        for w, m, ww in line:
            if m:
                asc, desc = font.getmetrics()
                draw.rounded_rectangle(
                    [x - marker_pad*0.5, y - 2, x + ww + marker_pad*0.5, y + asc + desc*0.35],
                    radius=8, fill=marker_col)
            draw.text((x, y), w, font=font, fill=text_col)
            x += ww + space
        y += lh
    return y

def render(out, theme, headline, subline, wordmark, domain):
    if theme == "light":
        bg = (247, 244, 238)      # #F7F4EE cream
        text_col = (24, 24, 24)
        marker_col = (185, 232, 201)  # #B9E8C9 pastel green
        sub_col = (90, 90, 90)
        foot_col = (24, 24, 24)
        dom_col = (120, 120, 120)
    else:
        bg = (20, 23, 26)         # #14171A anthracite
        text_col = (245, 245, 245)
        marker_col = (66, 194, 161)   # #42C2A1 mint
        sub_col = (150, 156, 160)
        foot_col = (245, 245, 245)
        dom_col = (124, 196, 240)     # readiness blue #7CC4F0
    im = Image.new("RGB", (W, H), bg)
    d = ImageDraw.Draw(im)

    fh = ImageFont.truetype(FB, 78)
    fs = ImageFont.truetype(FR, 40)
    ff = ImageFont.truetype(FB, 34)
    fd = ImageFont.truetype(FR, 30)

    maxw = W - 2*M
    space = d.textlength(" ", font=fh)
    lines = wrap(tokens(headline), fh, maxw, d, space)
    lh = 100
    block_h = len(lines) * lh
    # vertically center the headline block a touch above middle
    y0 = int(H * 0.30)
    end_y = draw_headline(d, lines, fh, M, y0, lh, space, text_col, marker_col)

    # subline
    sy = end_y + 40
    for para in subline.split("\n"):
        sl = wrap(tokens(para), fs, maxw, d, d.textlength(" ", font=fs))
        for line in sl:
            x = M
            for w, m, ww in line:
                d.text((x, sy), w, font=fs, fill=sub_col)
                x += ww + d.textlength(" ", font=fs)
            sy += 52

    # footer wordmark + domain
    fy = H - M - 40
    d.text((M, fy), wordmark, font=ff, fill=foot_col)
    wm_w = d.textlength(wordmark, font=ff)
    d.text((M + wm_w + 20, fy + 6), domain, font=fd, fill=dom_col)
    # thin accent rule above footer
    rule_col = marker_col if theme == "dark" else (200, 224, 208)
    d.rectangle([M, fy - 30, M + 70, fy - 26], fill=rule_col)

    im.save(out, "PNG")
    print("wrote", out, im.size)

if __name__ == "__main__":
    date = os.environ.get("DATE", "2026-07-23")
    outdir = os.path.join(REPO, "posts", date)
    os.makedirs(outdir, exist_ok=True)

    render(
        out=os.path.join(outdir, f"dosesimple_{date}.png"),
        theme="light",
        headline="Did I already take it *tonight*?",
        subline="By bedtime, one day blurs into the last.",
        wordmark="DoseSimple",
        domain="dosesimple.com",
    )
    render(
        out=os.path.join(outdir, f"refinesimple_{date}.png"),
        theme="dark",
        headline="You slept *badly*. And you're about to train like you *didn't*.",
        subline="The plan doesn't know how last night went.\nYou do.",
        wordmark="RefineSimple",
        domain="refinesimple.com",
    )
