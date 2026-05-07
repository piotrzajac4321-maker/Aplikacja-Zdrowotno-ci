"""ZielonaApteka — aplikacja Flask pokazująca leki i ich ziołowe zamienniki."""
import os

from flask import Flask, abort, render_template, request

from supabase_client import supabase

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-secret-change-me")


# --- Helpery zapytań ---------------------------------------------------------

def fetch_categories():
    res = (
        supabase.table("categories")
        .select("*")
        .order("sort_order")
        .execute()
    )
    return res.data or []


def fetch_category(slug: str):
    res = (
        supabase.table("categories")
        .select("*")
        .eq("slug", slug)
        .limit(1)
        .execute()
    )
    return (res.data or [None])[0]


def fetch_medications_by_category(category_id: int):
    res = (
        supabase.table("medications")
        .select("*, medication_herbs(herb_id)")
        .eq("category_id", category_id)
        .order("name_pl")
        .execute()
    )
    meds = res.data or []
    for m in meds:
        m["herb_count"] = len(m.get("medication_herbs") or [])
    return meds


def fetch_medication_detail(slug: str):
    res = (
        supabase.table("medications")
        .select(
            "*, categories(*), "
            "medication_herbs(rationale_pl, strength, herbs(*))"
        )
        .eq("slug", slug)
        .limit(1)
        .execute()
    )
    return (res.data or [None])[0]


def fetch_featured_pairs(limit: int = 4):
    """Kilka pierwszych leków + ich pierwsze zioło — do sekcji 'Popularne zestawienia'."""
    res = (
        supabase.table("medications")
        .select(
            "id, slug, name_pl, purpose_pl, "
            "categories(slug, name_pl, icon), "
            "medication_herbs(herbs(slug, name_pl, latin_name))"
        )
        .order("id")
        .limit(limit)
        .execute()
    )
    pairs = []
    for med in res.data or []:
        herbs = [link["herbs"] for link in (med.get("medication_herbs") or []) if link.get("herbs")]
        if herbs:
            pairs.append({"medication": med, "herb": herbs[0]})
    return pairs


# --- Routes ------------------------------------------------------------------

@app.route("/")
def index():
    return render_template(
        "index.html",
        categories=fetch_categories(),
        featured_pairs=fetch_featured_pairs(),
    )


@app.route("/lek/<slug>")
def medication_detail(slug):
    med = fetch_medication_detail(slug)
    if not med:
        abort(404)
    herbs = [
        {
            "rationale_pl": link.get("rationale_pl"),
            "strength": link.get("strength"),
            **(link.get("herbs") or {}),
        }
        for link in (med.get("medication_herbs") or [])
        if link.get("herbs")
    ]
    return render_template("detail.html", medication=med, herbs=herbs)


@app.route("/kategoria/<slug>")
def category_view(slug):
    category = fetch_category(slug)
    if not category:
        abort(404)
    medications = fetch_medications_by_category(category["id"])
    return render_template(
        "kategoria.html",
        category=category,
        medications=medications,
        categories=fetch_categories(),
    )


@app.route("/szukaj")
def search():
    q = (request.args.get("q") or "").strip()
    medications = []
    if q:
        pattern = f"%{q}%"
        res = (
            supabase.table("medications")
            .select("*, categories(slug, name_pl, icon)")
            .or_(f"name_pl.ilike.{pattern},active_substance.ilike.{pattern},brand_examples.ilike.{pattern}")
            .order("name_pl")
            .limit(50)
            .execute()
        )
        medications = res.data or []
    return render_template(
        "search_results.html",
        q=q,
        medications=medications,
        categories=fetch_categories(),
    )


@app.route("/o-projekcie")
def about():
    return render_template("o_projekcie.html", categories=fetch_categories())


@app.route("/healthz")
def healthz():
    return {"status": "ok"}, 200


@app.errorhandler(404)
def not_found(_):
    try:
        cats = fetch_categories()
    except Exception:
        cats = []
    return render_template("404.html", categories=cats), 404


# --- Context processor -------------------------------------------------------

@app.context_processor
def inject_globals():
    return {"site_name": "ZielonaApteka"}


if __name__ == "__main__":
    app.run(debug=True)
