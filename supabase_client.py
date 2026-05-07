"""Pojedynczy współdzielony klient Supabase.

Jeśli zmienne środowiskowe są niedostępne lub klient nie da się utworzyć,
moduł nie wywala aplikacji — zamiast tego ustawia ``supabase = None`` i loguje
ostrzeżenie. Aplikacja w app.py wykrywa ten stan i przełącza się na dane demo.
"""
import logging
import os

from dotenv import load_dotenv

load_dotenv()
log = logging.getLogger(__name__)

SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

supabase = None
init_error: str | None = None

if not SUPABASE_URL or not SUPABASE_KEY:
    init_error = "Brak SUPABASE_URL lub SUPABASE_KEY w środowisku."
    log.warning("%s Aplikacja przejdzie na dane demo.", init_error)
else:
    try:
        from supabase import Client, create_client
        supabase = create_client(SUPABASE_URL, SUPABASE_KEY)  # type: ignore[assignment]
    except Exception as exc:
        init_error = f"Nie udało się zainicjować klienta Supabase: {exc!r}"
        log.exception("Inicjalizacja Supabase nieudana — przechodzę na dane demo.")
        supabase = None
