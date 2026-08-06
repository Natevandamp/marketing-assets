#!/usr/bin/env python3
"""Daily cards 2026-08-06. Fokus: DoseSimple (Schlaf/Routine, Hitzewelle)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from daily_render import render, REPO

date = "2026-08-06"
outdir = os.path.join(REPO, "posts", date)
os.makedirs(outdir, exist_ok=True)

render(
    out=os.path.join(outdir, f"dosesimple_{date}.png"),
    theme="light",
    headline="Drei heiße Nächte. Und du zweifelst an deiner *ganzen Routine*.",
    subline="Vielleicht liegt es nicht an dir.\nDie Woche im Überblick sagt mehr als eine Nacht.",
    wordmark="DoseSimple",
    domain="dosesimple.com",
)
render(
    out=os.path.join(outdir, f"refinesimple_{date}.png"),
    theme="dark",
    headline="Montag verpasst. Und die Woche fühlt sich *verloren* an.",
    subline="Eine Woche ist keine Serie, die reißt.\nSie ist vier, fünf Entscheidungen. Die nächste ist offen.",
    wordmark="RefineSimple",
    domain="refinesimple.com",
)
