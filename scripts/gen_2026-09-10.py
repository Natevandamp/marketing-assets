#!/usr/bin/env python3
"""IG-Grafiken 2026-09-10: DoseSimple (hell) + RefineSimple (dunkel), 1080x1350."""
from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1080, 1350
OUT = os.path.join(os.path.dirname(__file__), "..", "posts", "2026-09-10")
os.makedirs(OUT, exist_ok=True)

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

def f(path, size):
    return ImageFont.truetype(path, size)

def draw_line_with_markers(d, x, y, parts, font, fill, marker_color, marker_text_fill=None, pad_x=14, pad_y=8, radius=10):
    """parts: list of (text, marked:bool). Draws one line starting at x,y."""
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
d.text((100, 145), "Bedtime this week:", font=eyebrow, fill=GRAY)
times = f(BOLD, 40)
d.text((100, 200), "22:15   ·   23:40   ·   01:10   ·   22:30", font=times, fill=BLACK)

head = f(BOLD, 90)
y = 330
lh = 126
draw_line_with_markers(d, 100, y, [("Your evening", False)], head, BLACK, MARK)
y += lh
draw_line_with_markers(d, 100, y, [("routine moves", False)], head, BLACK, MARK)
y += lh
draw_line_with_markers(d, 100, y, [("with it.", True)], head, BLACK, MARK, marker_text_fill=BLACK)

sub = f(REG, 44)
y += lh + 85
d.text((100, y), "A drifting bedtime is a drifting routine.", font=sub, fill=GRAY)
d.text((100, y + 66), "A record shows the pattern.", font=sub, fill=GRAY)

brand = f(BOLD, 48)
url = f(REG, 36)
d.text((100, H - 190), "DoseSimple", font=brand, fill=BLACK)
d.text((100, H - 120), "dosesimple.com", font=url, fill=GRAY)
d.ellipse([W - 160, H - 180, W - 110, H - 130], fill=MARK)
img.save(os.path.join(OUT, "dosesimple_2026-09-10.png"))

# ---------------- RefineSimple (dunkel) ----------------
img = Image.new("RGB", (W, H), "#14171A")
d = ImageDraw.Draw(img)
WHITE = "#F2F4F5"
DGRAY = "#9BA3AB"
ACC = "#42C2A1"
DARK = "#14171A"

eyebrow = f(BOLD, 32)
d.text((100, 150), "WHAT YOUR BODY WOULD TELL YOU", font=eyebrow, fill=ACC)

head = f(BOLD, 92)
y = 260
lh = 128
draw_line_with_markers(d, 100, y, [("You woke up", False)], head, WHITE, ACC)
y += lh
draw_line_with_markers(d, 100, y, [("tired and called", False)], head, WHITE, ACC)
y += lh
draw_line_with_markers(d, 100, y, [("it", False), ("laziness.", True)], head, WHITE, ACC, marker_text_fill=DARK)

sub = f(REG, 44)
y += lh + 90
d.text((100, y), "Tiredness is data.", font=sub, fill=DGRAY)
d.text((100, y + 66), "Not a character flaw.", font=sub, fill=DGRAY)

brand = f(BOLD, 48)
url = f(REG, 36)
d.text((100, H - 190), "RefineSimple", font=brand, fill=WHITE)
d.text((100, H - 120), "refinesimple.com", font=url, fill=DGRAY)
d.rectangle([W - 170, H - 150, W - 100, H - 138], fill=ACC)
img.save(os.path.join(OUT, "refinesimple_2026-09-10.png"))

print("done")
