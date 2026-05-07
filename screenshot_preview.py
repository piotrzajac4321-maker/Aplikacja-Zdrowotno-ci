"""Generuje zrzuty PNG wszystkich stron z `preview/` używając headless Chromium.

Wymaga: playwright + chromium. Uruchom najpierw `python3 render_preview.py`,
żeby wygenerować HTML-e.

Użycie:
    python3 screenshot_preview.py
"""
from __future__ import annotations

import os
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent
PREVIEW = ROOT / "preview"
SHOTS = PREVIEW / "screenshots"

# Każdy element listy: (nazwa_pliku.html, tytuł, szerokość, wysokość, full_page)
PAGES = [
    ("index.html",            "01-strona-glowna-desktop",     1280, 900, True),
    ("index.html",            "02-strona-glowna-mobile",       400, 800, True),
    ("lek-ibuprofen.html",    "03-szczegoly-ibuprofen",       1280, 900, True),
    ("lek-melatonina.html",   "04-szczegoly-melatonina",      1280, 900, True),
    ("lek-omeprazol.html",    "05-szczegoly-omeprazol",       1280, 900, True),
    ("kategoria-bol.html",    "06-kategoria-bol",             1280, 900, True),
    ("kategoria-sen.html",    "07-kategoria-sen",             1280, 900, True),
    ("kategoria-trawienie.html","08-kategoria-trawienie",     1280, 900, True),
    ("szukaj-melat.html",     "09-wyszukiwanie",              1280, 900, True),
    ("o-projekcie.html",      "10-o-projekcie",               1280, 900, True),
    ("404.html",              "11-strona-404",                1280, 900, True),
    ("zamienniki-zywnosci.html","12-zamienniki-zywnosci",     1280, 900, True),
    ("lek-loperamid.html",    "13-lek-z-owocami-warzywami",   1280, 900, True),
]

CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"


def main() -> None:
    SHOTS.mkdir(exist_ok=True)
    print(f"Zapisuję zrzuty do: {SHOTS.relative_to(ROOT)}/")

    with sync_playwright() as p:
        executable = CHROME if os.path.exists(CHROME) else None
        browser = p.chromium.launch(executable_path=executable, args=["--no-sandbox"])
        for filename, label, width, height, full in PAGES:
            page = browser.new_page(viewport={"width": width, "height": height})
            page.goto(f"file://{PREVIEW / filename}")
            page.wait_for_load_state("networkidle", timeout=10000)
            out = SHOTS / f"{label}.png"
            page.screenshot(path=str(out), full_page=full)
            page.close()
            print(f"  ✓ {out.relative_to(ROOT)}  ({width}x{height})")
        browser.close()

    print("\nGotowe.")


if __name__ == "__main__":
    main()
