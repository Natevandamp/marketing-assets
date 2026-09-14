#!/usr/bin/env python3
"""IG-Grafiken 2026-09-14: DoseSimple (hell, leere-Dose-Pain-Point) + RefineSimple (dunkel, Score vs. Entscheidung), 1080x1350."""
from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1080, 1350
OUT = os.path.join(os.path.dirname(__file__), "..", "posts", "2026-09-14")
os.makedirs(OUT, exist_ok=True)

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

def f(path, size):
    return ImageFont.truetype(path, size)

def draw_line_with_markers(d, x, y, parts, font, fill, marker_color, marker_text_fill=None, pad_x=14, pad_y=8, radius=10):
    cx = x
    for text, marked in parts:
        bbox = d.textbbox((cx, y), text, font=font)
        if marked:
            d.rounded_rectangle(
                [bbox[0] - pad_x, bbox[1] - pad_y, bbox[2] + pad_x, bbox[3] + pad_y],
                radius=radius, fill=marker_color)
            d.text((cx, y), text, font=font, fill=marker_text_fill or fill)
        else:
            d.text((cx, y), text, font=font, fill=fill)
        cx = bbox[2] + d.textlength(" ", font=font)
    return cx

# ---------------- DoseSimple (hell) ----------------
img = Image.new("RGB", (W, H), "#F7F4EE")
d = ImageDraw.Draw(img)
BLACK = "#1C1B18"
GRAY = "#6E6A61"
MARK = "#B9E8C9"

eyebrow = f(REG, 34)
d.text((100, 150), "Monday, 7:02. The jar is empty.", font=eyebrow, fill=GRAY)

head = f(BOLD, 92)
y = 300
lh = 128
e1 = draw_line_with_markers(d, 100, y, [("The bottle", False)], head, BLACK, MARK)
y += lh
e2 = draw_line_with_markers(d, 100, y, [("ran out.", False)], head, BLACK, MARK)
y += lh
e3 = draw_line_with_markers(d, 100, y, [("Not your", False)], head, BLACK, MARK)
y += lh
e4 = draw_line_with_markers(d, 100, y, [("discipline.", True)], head, BLACK, MARK, marker_text_fill=BLACK)
print("dose widths:", e1, e2, e3, e4)

sub = f(REG, 44)
y += lh + 80
d.text((100, y), "A supply gap and a lapse look identical", font=sub, fill=GRAY)
d.text((100, y + 66), "three weeks later. Unless it's written down.", font=sub, fill=GRAY)

brand = f(BOLD, 48)
url = f(REG, 36)
d.text((100, H - 190), "DoseSimple", font=brand, fill=BLACK)
d.text((100, H - 120), "dosesimple.com", font=url, fill=GRAY)
d.ellipse([W - 160, H - 180, W - 110, H - 130], fill=MARK)
img.save(os.path.join(OUT, "dosesimple_2026-09-14.png"))

# ---------------- RefineSimple (dunkel) ----------------
img = Image.new("RGB", (W, H), "#14171A")
d = ImageDraw.Draw(img)
WHITE = "#F2F4F5"
DGRAY = "#9BA3AB"
ACC = "#42C2A1"
BLUE = "#7CC4F0"
DARK = "#14171A"

eyebrow = f(BOLD, 32)
d.text((100, 150), "DIE BESSERE ENTSCHEIDUNG", font=eyebrow, fill=ACC)

head = f(BOLD, 88)
y = 300
lh = 124
e1 = draw_line_with_markers(d, 100, y, [("A score is", False)], head, WHITE, ACC)
y += lh
e2 = draw_line_with_markers(d, 100, y, [("not a", False), ("decision.", True)], head, WHITE, ACC, marker_text_fill=DARK)
print("refine widths:", e1, e2)

sub = f(REG, 42)
y += lh + 100
d.text((100, y), "Millions of wrists got a number today.", font=sub, fill=DGRAY)
d.text((100, y + 64), "Knowing it isn't knowing what to do.", font=sub, fill=DGRAY)

# ruhiges Detail: kleine Readiness-Zahl in Blau als visueller Anker
score = f(BOLD, 42)
d.text((100, y + 190), "6/10", font=score, fill=BLUE)
d.text((100 + d.textlength("6/10", font=score) + 24, y + 190), "— now what?", font=f(REG, 42), fill=DGRAY)

brand = f(BOLD, 48)
url = f(REG, 36)
d.text((100, H - 190), "RefineSimple", font=brand, fill=WHITE)
d.text((100, H - 120), "refinesimple.com", font=url, fill=DGRAY)
d.rectangle([W - 170, H - 165, W - 100, H - 145], fill=ACC)
img.save(os.path.join(OUT, "refinesimple_2026-09-14.png"))
print("done")
