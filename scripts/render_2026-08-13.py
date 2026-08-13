#!/usr/bin/env python3
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from daily_render import render, REPO

date = "2026-08-13"
outdir = os.path.join(REPO, "posts", date)
os.makedirs(outdir, exist_ok=True)

render(
    out=os.path.join(outdir, f"dosesimple_{date}.png"),
    theme="light",
    headline="Der erste *Wecker* nach dem Urlaub. Die Routine kommt *nicht von allein* zurück.",
    subline="Zwei Wochen Pause löschen keine drei Monate.\nDeine Historie weiß das noch.",
    wordmark="DoseSimple",
    domain="dosesimple.com",
)
render(
    out=os.path.join(outdir, f"refinesimple_{date}.png"),
    theme="dark",
    headline="Erste Einheit nach dem Urlaub. Du musst *nichts aufholen*.",
    subline="Der Plan von vor drei Wochen kennt deinen heutigen Zustand nicht.\nDu darfst leichter wieder einsteigen.",
    wordmark="RefineSimple",
    domain="refinesimple.com",
)
