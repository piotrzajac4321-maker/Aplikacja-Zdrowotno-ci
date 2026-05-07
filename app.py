"""ZielonaApteka — aplikacja Flask pokazująca leki i ich ziołowe zamienniki.

Każda funkcja pobierająca dane próbuje najpierw Supabase, a w razie problemu
(brak klienta, błąd sieciowy, pusta baza) automatycznie używa danych demo
z modułu ``demo_data``. Dzięki temu aplikacja zawsze coś pokazuje, nawet jeśli
Supabase nie jest jeszcze skonfigurowany.
"""
import logging
import os

from flask import Flask, abort, render_template, request

import demo_data
from supabase_client import init_error, supabase

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-secret-change-me")

log = logging.getLogger(__name__)


def _supabase_or_none(query):
    """Wykonaj zapytanie Supabase, zwróć dane lub None gdy błąd."""
    if supabase is None:
        return None
    try:
        res = query.execute()
        return res.data
    except Exception as exc:
        log.warning("Zapytanie Supabase nieudane (%s) — używam danych demo.", exc)
        return None


# --- Helpery zapytań ---------------------------------------------------------

def fetch_categories():
    if supabase is not None:
        data = _supabase_or_none(
            supabase.table("categories").select("*").order("sort_order")
        )
        if data:
            return data
    return demo_data.categories()


def fetch_category(slug: str):
    if supabase is not None:
        data = _supabase_or_none(
            supabase.table("categories").select("*").eq("slug", slug).limit(1)
        )
        if data:
            return data[0]
    return demo_data.category(slug)


def fetch_medications_by_category(category_id: int):
    if supabase is not None:
        data = _supabase_or_none(
            supabase.table("medications")
            .select("*, medication_herbs(herb_id)")
            .eq("category_id", category_id)
            .order("name_pl")
        )
        if data is not None:
            for m in data:
                m["herb_count"] = len(m.get("medication_herbs") or [])
            if data:
                return data
    return demo_data.medications_by_category(category_id)


def fetch_medication_detail(slug: str):
    if supabase is not None:
        data = _supabase_or_none(
            supabase.table("medications")
            .select(
                "*, categories(*), "
                "medication_herbs(rationale_pl, strength, herbs(*))"
            )
            .eq("slug", slug)
            .limit(1)
        )
        if data:
            return data[0]
    return demo_data.medication_detail(slug)


def fetch_featured_pairs(limit: int = 4):
    """Kilka pierwszych leków + ich pierwsze zioło — do sekcji 'Popularne zestawienia'."""
    if supabase is not None:
        data = _supabase_or_none(
            supabase.table("medications")
            .select(
                "id, slug, name_pl, purpose_pl, "
                "categories(slug, name_pl, icon), "
                "medication_herbs(herbs(slug, name_pl, latin_name))"
            )
            .order("id")
            .limit(limit)
        )
        if data:
            pairs = []
            for med in data:
                herbs = [link["herbs"] for link in (med.get("medication_herbs") or []) if link.get("herbs")]
                if herbs:
                    pairs.append({"medication": med, "herb": herbs[0]})
            if pairs:
                return pairs
    return demo_data.featured_pairs(limit=limit)


def search_medications(q: str):
    if supabase is not None:
        pattern = f"%{q}%"
        data = _supabase_or_none(
            supabase.table("medications")
            .select("*, categories(slug, name_pl, icon)")
            .or_(
                f"name_pl.ilike.{pattern},"
                f"active_substance.ilike.{pattern},"
                f"brand_examples.ilike.{pattern}"
            )
            .order("name_pl")
            .limit(50)
        )
        if data is not None:
            return data
    return demo_data.search(q)


# --- Routes ------------------------------------------------------------------

def fetch_stats():
    """Liczby do paska statystyk na stronie głównej."""
    if supabase is not None:
        try:
            meds = supabase.table("medications").select("id", count="exact").execute()
            herbs = supabase.table("herbs").select("id", count="exact").execute()
            if meds.count is not None and herbs.count is not None:
                return {"medications": meds.count, "herbs": herbs.count}
        except Exception as exc:
            log.warning("Statystyki Supabase nieudane (%s) — używam danych demo.", exc)
    return {"medications": len(demo_data.MEDICATIONS), "herbs": len(demo_data.HERBS)}


@app.route("/")
def index():
    return render_template(
        "index.html",
        categories=fetch_categories(),
        featured_pairs=fetch_featured_pairs(),
        stats=fetch_stats(),
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
    medications = search_medications(q) if q else []
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


@app.route("/debug")
def debug():
    """Endpoint diagnostyczny — pokazuje skąd biorą się dane i co z konfiguracji."""
    cats = fetch_categories()
    using_supabase = supabase is not None
    sample_query_ok = False
    sample_err = None
    if supabase is not None:
        try:
            res = supabase.table("categories").select("slug").limit(1).execute()
            sample_query_ok = bool(res.data)
        except Exception as exc:
            sample_err = repr(exc)
    return {
        "supabase_client_initialized": using_supabase,
        "supabase_init_error": init_error,
        "supabase_sample_query_ok": sample_query_ok,
        "supabase_sample_query_error": sample_err,
        "categories_count": len(cats),
        "categories_first": cats[0] if cats else None,
        "data_source": "supabase" if (using_supabase and sample_query_ok) else "demo",
        "env_vars_present": {
            "SUPABASE_URL": bool(os.environ.get("SUPABASE_URL")),
            "SUPABASE_KEY": bool(os.environ.get("SUPABASE_KEY")),
            "SECRET_KEY": bool(os.environ.get("SECRET_KEY")),
        },
    }, 200


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
