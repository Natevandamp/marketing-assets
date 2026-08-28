#!/usr/bin/env python3
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from daily_render import render, REPO

date = "2026-08-28"
outdir = os.path.join(REPO, "posts", date)
os.makedirs(outdir, exist_ok=True)

render(
    out=os.path.join(outdir, f"dosesimple_{date}.png"),
    theme="light",
    headline="Niemand lässt eine Dosis *absichtlich* aus.",
    subline="Der Tag war nur voll.\nUnd gestern sah genauso aus wie heute.",
    wordmark="DoseSimple",
    domain="dosesimple.com",
)
render(
    out=os.path.join(outdir, f"refinesimple_{date}.png"),
    theme="dark",
    headline="Einen PR kann man nicht *planen*.",
    subline="Aber man kann ihn kommen sehen.\nSchlaf, Erholung, Belastung —\nstarke Tage kündigen sich an.",
    wordmark="RefineSimple",
    domain="refinesimple.com",
)
