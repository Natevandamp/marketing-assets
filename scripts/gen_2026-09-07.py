import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from daily_render import render, REPO

date = "2026-09-07"
outdir = os.path.join(REPO, "posts", date)
os.makedirs(outdir, exist_ok=True)

render(
    out=os.path.join(outdir, f"dosesimple_{date}.png"),
    theme="light",
    headline="Erinnerung *weggedrückt* fühlt sich an wie erledigt.",
    subline="Die Erinnerung kennt nur die Uhrzeit.\nNicht, ob du es genommen hast.",
    wordmark="DoseSimple",
    domain="dosesimple.com",
)
render(
    out=os.path.join(outdir, f"refinesimple_{date}.png"),
    theme="dark",
    headline="Für Arbeit gibt es *Feiertage*. Für Training nur schlechtes Gewissen.",
    subline="Erholung ist kein Aussetzen.\nSie ist Teil des Fortschritts.",
    wordmark="RefineSimple",
    domain="refinesimple.com",
)
