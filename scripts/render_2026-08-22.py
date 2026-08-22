#!/usr/bin/env python3
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from daily_render import render, REPO

date = "2026-08-22"
outdir = os.path.join(REPO, "posts", date)
os.makedirs(outdir, exist_ok=True)

Q0, Q1 = "„", "“"  # German quotes

render(
    out=os.path.join(outdir, f"dosesimple_{date}.png"),
    theme="light",
    headline=f"{Q0}Nehmen Sie es regelmäßig?{Q1} *{Q0}Ich glaube, ja.{Q1}*",
    subline=f"Zwischen {Q0}fast immer{Q1} und {Q0}wirklich immer{Q1}\nliegen ein paar vergessene Abende.".replace(" und ", " und\n"),
    wordmark="DoseSimple",
    domain="dosesimple.com",
)
render(
    out=os.path.join(outdir, f"refinesimple_{date}.png"),
    theme="dark",
    headline="Zwei verpasste Einheiten passen nicht in *einen Samstag*.",
    subline="Nachholen klingt nach Disziplin.\nDein Körper führt kein Schuldenkonto.\nEr zählt Belastung.",
    wordmark="RefineSimple",
    domain="refinesimple.com",
)
