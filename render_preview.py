"""Generuje statyczne pliki HTML w katalogu `preview/` na podstawie szablonów Jinja2
i przykładowych danych z `demo_data.py`. Pozwala obejrzeć wygląd aplikacji
bez instalowania Flaska, bez konfiguracji Supabase i bez uruchamiania serwera.

Użycie:
    python3 render_preview.py
Następnie otwórz w przeglądarce:
    preview/index.html
"""
from __future__ import annotations

import shutil
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

import demo_data

ROOT = Path(__file__).resolve().parent
TEMPLATES = ROOT / "templates"
STATIC_SRC = ROOT / "static"
PREVIEW = ROOT / "preview"
PREVIEW_STATIC = PREVIEW / "static"


# --- Stand-in dla Flask url_for() --------------------------------------------

def url_for(endpoint: str, **kwargs) -> str:
    if endpoint == "static":
        return f"./static/{kwargs.get('filename', '')}"
    if endpoint == "index":
        return "index.html"
    if endpoint == "medication_detail":
        return f"lek-{kwargs['slug']}.html"
    if endpoint == "category_view":
        return f"kategoria-{kwargs['slug']}.html"
    if endpoint == "search":
        return "szukaj.html"
    if endpoint == "about":
        return "o-projekcie.html"
    return "#"


# --- Setup -------------------------------------------------------------------

env = Environment(
    loader=FileSystemLoader(str(TEMPLATES)),
    autoescape=select_autoescape(["html"]),
)
env.globals["url_for"] = url_for
env.globals["site_name"] = "ZielonaApteka"


def render(template_name: str, output_path: Path, **context) -> None:
    template = env.get_template(template_name)
    html = template.render(**context)
    output_path.write_text(html, encoding="utf-8")
    print(f"  ✓ {output_path.relative_to(ROOT)}")


# --- Główna logika -----------------------------------------------------------

def main() -> None:
    if PREVIEW.exists():
        shutil.rmtree(PREVIEW)
    PREVIEW.mkdir()

    # Skopiuj statyczne assety
    if STATIC_SRC.exists():
        shutil.copytree(STATIC_SRC, PREVIEW_STATIC)
        print(f"  ✓ skopiowano {STATIC_SRC.relative_to(ROOT)} -> {PREVIEW_STATIC.relative_to(ROOT)}")

    cats = demo_data.categories()

    # Helper: każda strona przygotowana do "kontekstu szablonu"
    print("\nGeneruję strony…")

    # 1. Strona główna
    render(
        "index.html",
        PREVIEW / "index.html",
        categories=cats,
        featured_pairs=demo_data.featured_pairs(limit=4),
    )

    # 2. Strony szczegółów dla każdego leku
    for med_summary in demo_data.MEDICATIONS:
        med = demo_data.medication_detail(med_summary["slug"])
        herbs = [
            {**(link["herbs"]), "rationale_pl": link["rationale_pl"], "strength": link["strength"]}
            for link in (med.get("medication_herbs") or [])
        ]
        render(
            "detail.html",
            PREVIEW / f"lek-{med['slug']}.html",
            medication=med,
            herbs=herbs,
            categories=cats,
        )

    # 3. Strony kategorii
    for cat in cats:
        render(
            "kategoria.html",
            PREVIEW / f"kategoria-{cat['slug']}.html",
            category=cat,
            medications=demo_data.medications_by_category(cat["id"]),
            categories=cats,
        )

    # 4. Wyszukiwanie — pusta + przykładowy wynik
    render(
        "search_results.html",
        PREVIEW / "szukaj.html",
        q="",
        medications=[],
        categories=cats,
    )
    render(
        "search_results.html",
        PREVIEW / "szukaj-melat.html",
        q="melat",
        medications=demo_data.search("melat"),
        categories=cats,
    )

    # 5. Strony statyczne
    render("o_projekcie.html", PREVIEW / "o-projekcie.html", categories=cats)
    render("404.html",         PREVIEW / "404.html",         categories=cats)

    print(f"\nGotowe! Otwórz w przeglądarce:\n  {PREVIEW / 'index.html'}")


if __name__ == "__main__":
    main()
