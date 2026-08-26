#!/usr/bin/env python3
"""Instagram graphics 2026-08-26 — 1080x1350."""
from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1350
FD = "/usr/share/fonts/truetype/dejavu/"
BOLD = FD + "DejaVuSans-Bold.ttf"
BOOK = FD + "DejaVuSans.ttf"

def font(path, size):
    return ImageFont.truetype(path, size)

def draw_marker_line(draw, segments, x, y, f, fill, marker=None, marker_text=None, pad=14):
    """segments: list of (text, highlighted). Returns line width."""
    cx = x
    asc, desc = f.getmetrics()
    for text, hl in segments:
        w = draw.textlength(text, font=f)
        if hl and marker:
            draw.rounded_rectangle(
                [cx - pad, y - 6, cx + w + pad, y + asc + desc * 0.35],
                radius=12, fill=marker)
            draw.text((cx, y), text, font=f, fill=marker_text or fill)
        else:
            draw.text((cx, y), text, font=f, fill=fill)
        cx += w
    return cx - x

def wrap(draw, text, f, maxw):
    words, lines, cur = text.split(), [], ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if draw.textlength(t, font=f) <= maxw:
            cur = t
        else:
            lines.append(cur); cur = w_
    if cur: lines.append(cur)
    return lines

# ---------------- DoseSimple (bright) ----------------
img = Image.new("RGB", (W, H), "#F7F4EE")
d = ImageDraw.Draw(img)
BLACK = "#1A1A1A"
MARK = "#B9E8C9"

f_head = font(BOLD, 92)
f_sub = font(BOOK, 40)
f_foot_b = font(BOLD, 40)
f_foot = font(BOOK, 34)
f_eyebrow = font(BOLD, 30)

x = 100
d.text((x, 170), "L A T E   A U G U S T", font=f_eyebrow, fill="#8AA894")

y = 270
lh = 124
head = [
    [("The routine", False)],
    [("didn't survive", False)],
    [("the summer.", True)],
    [("That's normal.", False)],
]
for seg in head:
    draw_marker_line(d, seg, x, y, f_head, BLACK, marker=MARK, marker_text=BLACK)
    y += lh

y += 55
sub = ("Vacation weeks don't keep schedules — so pills and "
       "supplements slip too. A restart doesn't need more "
       "discipline. It needs to be easy enough for a normal morning.")
for line in wrap(d, sub, f_sub, W - 2 * x):
    d.text((x, y), line, font=f_sub, fill="#4A4A45")
    y += 58

# footer
d.line([(x, H - 190), (W - x, H - 190)], fill="#DDD8CC", width=3)
d.text((x, H - 150), "DoseSimple", font=f_foot_b, fill=BLACK)
wds = d.textlength("dosesimple.com", font=f_foot)
d.text((W - x - wds, H - 145), "dosesimple.com", font=f_foot, fill="#7A776E")
img.save("/home/claude/marketing-assets/posts/2026-08-26/dosesimple_2026-08-26.png")

# ---------------- RefineSimple (dark) ----------------
img = Image.new("RGB", (W, H), "#14171A")
d = ImageDraw.Draw(img)
WHITE = "#F2F4F5"
ACC = "#42C2A1"

f_head = font(BOLD, 96)
f_sub = font(BOOK, 40)
f_eyebrow = font(BOLD, 28)

x = 100
d.text((x, 170), "W H A T   Y O U R   B O D Y   W O U L D   T E L L   Y O U",
       font=f_eyebrow, fill="#5C6A72")

y = 290
lh = 132
head = [
    [("Fatigue isn't", False)],
    [("weakness.", False)],
    [("It's ", False), ("information.", True)],
]
for seg in head:
    draw_marker_line(d, seg, x, y, f_head, WHITE, marker=ACC, marker_text="#14171A")
    y += lh

y += 70
sub = ("Sleep, resting heart rate, training load — your body keeps "
       "an honest record. The question isn't how hard you can push. "
       "It's what today's numbers say.")
for line in wrap(d, sub, f_sub, W - 2 * x):
    d.text((x, y), line, font=f_sub, fill="#9AA6AC")
    y += 58

d.line([(x, H - 190), (W - x, H - 190)], fill="#242A2E", width=3)
d.text((x, H - 150), "RefineSimple", font=font(BOLD, 40), fill=WHITE)
wds = d.textlength("refinesimple.com", font=f_sub)
d.text((W - x - wds, H - 145), "refinesimple.com", font=font(BOOK, 34), fill="#5C6A72")
img.save("/home/claude/marketing-assets/posts/2026-08-26/refinesimple_2026-08-26.png")
print("done")
