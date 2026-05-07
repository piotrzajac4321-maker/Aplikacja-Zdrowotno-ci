# ZielonaApteka

Aplikacja webowa pokazująca popularne leki apteczne obok ich naturalnych, ziołowych zamienników.

> ⓘ Treści mają charakter wyłącznie informacyjny i nie zastępują porady lekarza ani farmaceuty.

## Stack

- **Backend / framework:** Python 3.12 + Flask 3
- **Szablony:** Jinja2
- **Baza danych:** Supabase (PostgreSQL w chmurze)
- **CSS:** Tailwind CSS przez CDN
- **Deploy:** Render.com (free tier) z Gunicornem

## Lokalne uruchomienie

### 1. Środowisko Python

```bash
python -m venv .venv
source .venv/bin/activate         # Linux/Mac
# .venv\Scripts\activate          # Windows
pip install -r requirements.txt
```

### 2. Supabase (osobny projekt!)

Załóż **dedykowany** projekt na [supabase.com](https://supabase.com) (np. `zielona-apteka` — nie współdziel z innymi aplikacjami).

W panelu Supabase otwórz **SQL Editor** i wykonaj kolejno:

1. `seed/schema.sql` — tworzy tabele i polityki RLS
2. `seed/seed_data.sql` — wypełnia bazę kategoriami, lekami i ziołami

Skopiuj z **Settings → API**:
- `Project URL`
- `anon` `public` API key

### 3. Plik `.env`

```bash
cp .env.example .env
```

Wypełnij `.env` skopiowanymi wartościami z Supabase.

### 4. Start

```bash
flask --app app run --debug
```

Otwórz [http://127.0.0.1:5000](http://127.0.0.1:5000).

## Struktura

```
.
├── app.py                    # Flask + route'y
├── supabase_client.py        # Klient Supabase
├── seed/
│   ├── schema.sql            # CREATE TABLE + RLS
│   └── seed_data.sql         # Dane startowe
├── templates/                # Jinja2
│   ├── base.html
│   ├── index.html
│   ├── detail.html
│   ├── kategoria.html
│   ├── search_results.html
│   ├── o_projekcie.html
│   ├── 404.html
│   └── partials/
└── static/
    ├── css/style.css
    └── img/logo.svg
```

## Route'y

| URL | Opis |
|-----|------|
| `/` | Strona główna: hero, kategorie, popularne zestawienia |
| `/lek/<slug>` | Szczegóły leku + lista ziołowych alternatyw |
| `/kategoria/<slug>` | Wszystkie leki w kategorii |
| `/szukaj?q=...` | Wyszukiwarka |
| `/o-projekcie` | Disclaimer + opis projektu |
| `/healthz` | Health check (200 OK) |

## Deploy na Render.com

1. Wypchnij repozytorium na GitHub.
2. [render.com](https://render.com) → **New** → **Web Service** → wybierz repo.
3. Build command: `pip install -r requirements.txt`
4. Start command: `gunicorn app:app`
5. W zakładce **Environment** dodaj:
   - `SUPABASE_URL`
   - `SUPABASE_KEY`
   - `SECRET_KEY` (długi losowy ciąg)

## Disclaimer

Projekt edukacyjny. Informacje o ziołach pochodzą z publicznych źródeł (m.in. monografie ESCOP, PZH). Nie zastępują konsultacji lekarskiej ani farmaceutycznej. Przed użyciem ziół skonsultuj się ze specjalistą — szczególnie w ciąży, podczas karmienia piersią, u dzieci i przy przewlekłym przyjmowaniu leków.
