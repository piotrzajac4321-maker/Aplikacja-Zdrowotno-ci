-- =====================================================
-- ZielonaApteka — schemat bazy danych (Supabase / PostgreSQL)
-- Wykonaj w SQL Editor w panelu Supabase.
-- =====================================================

CREATE EXTENSION IF NOT EXISTS pg_trgm;

-- 1. Kategorie schorzeń ---------------------------------
CREATE TABLE IF NOT EXISTS categories (
    id          bigserial PRIMARY KEY,
    slug        text NOT NULL UNIQUE,
    name_pl     text NOT NULL,
    description text,
    icon        text,
    sort_order  int  NOT NULL DEFAULT 0,
    created_at  timestamptz NOT NULL DEFAULT now()
);

-- 2. Leki apteczne --------------------------------------
CREATE TABLE IF NOT EXISTS medications (
    id               bigserial PRIMARY KEY,
    slug             text NOT NULL UNIQUE,
    name_pl          text NOT NULL,
    active_substance text,
    brand_examples   text,
    purpose_pl       text,
    description_pl   text,
    side_effects_pl  text,
    category_id      bigint REFERENCES categories(id) ON DELETE SET NULL,
    image_url        text,
    created_at       timestamptz NOT NULL DEFAULT now()
);
CREATE INDEX IF NOT EXISTS idx_medications_category ON medications(category_id);
CREATE INDEX IF NOT EXISTS idx_medications_name_trgm
    ON medications USING gin (name_pl gin_trgm_ops);

-- 3. Zioła ----------------------------------------------
CREATE TABLE IF NOT EXISTS herbs (
    id               bigserial PRIMARY KEY,
    slug             text NOT NULL UNIQUE,
    name_pl          text NOT NULL,
    latin_name       text,
    description_pl   text,
    how_to_use_pl    text,
    cautions_pl      text,
    appearance_pl    text,                  -- wygląd zioła (jak rozpoznać)
    where_to_find_pl text,                  -- gdzie kupić / czy rośnie dziko w PL
    image_url        text,
    created_at       timestamptz NOT NULL DEFAULT now()
);

-- Migracja: dodaj kolumny dla istniejących baz utworzonych przed tymi polami
ALTER TABLE herbs ADD COLUMN IF NOT EXISTS appearance_pl    text;
ALTER TABLE herbs ADD COLUMN IF NOT EXISTS where_to_find_pl text;
-- Rodzaj wpisu: 'zielo' (domyślnie), 'owoc', 'warzywo', 'pokarm'
ALTER TABLE herbs ADD COLUMN IF NOT EXISTS kind             text NOT NULL DEFAULT 'zielo';

-- 4b. Zamienniki niezdrowej żywności --------------------
CREATE TABLE IF NOT EXISTS food_swaps (
    id                bigserial PRIMARY KEY,
    slug              text NOT NULL UNIQUE,
    unhealthy_name_pl text NOT NULL,           -- "Olej rzepakowy rafinowany"
    unhealthy_why_pl  text,                    -- dlaczego niezdrowy
    healthy_name_pl   text NOT NULL,           -- "Łój wołowy / smalec"
    healthy_why_pl    text,                    -- dlaczego lepszy
    rationale_pl      text,                    -- dodatkowy kontekst
    icon_unhealthy    text,                    -- np. 🥡, 🍟
    icon_healthy      text,                    -- np. 🥩, 🍯
    sort_order        int NOT NULL DEFAULT 0,
    created_at        timestamptz NOT NULL DEFAULT now()
);

-- 4. Powiązania lek <-> zioło (many-to-many) ------------
CREATE TABLE IF NOT EXISTS medication_herbs (
    medication_id bigint NOT NULL REFERENCES medications(id) ON DELETE CASCADE,
    herb_id       bigint NOT NULL REFERENCES herbs(id)       ON DELETE CASCADE,
    rationale_pl  text,
    strength      smallint NOT NULL DEFAULT 3 CHECK (strength BETWEEN 1 AND 5),
    PRIMARY KEY (medication_id, herb_id)
);
CREATE INDEX IF NOT EXISTS idx_medherbs_med  ON medication_herbs(medication_id);
CREATE INDEX IF NOT EXISTS idx_medherbs_herb ON medication_herbs(herb_id);

-- =====================================================
-- Row Level Security: tylko publiczny SELECT
-- =====================================================
ALTER TABLE categories       ENABLE ROW LEVEL SECURITY;
ALTER TABLE medications      ENABLE ROW LEVEL SECURITY;
ALTER TABLE herbs            ENABLE ROW LEVEL SECURITY;
ALTER TABLE medication_herbs ENABLE ROW LEVEL SECURITY;
ALTER TABLE food_swaps       ENABLE ROW LEVEL SECURITY;

DROP POLICY IF EXISTS "public read categories"       ON categories;
DROP POLICY IF EXISTS "public read medications"      ON medications;
DROP POLICY IF EXISTS "public read herbs"            ON herbs;
DROP POLICY IF EXISTS "public read medication_herbs" ON medication_herbs;
DROP POLICY IF EXISTS "public read food_swaps"       ON food_swaps;

CREATE POLICY "public read categories"       ON categories       FOR SELECT USING (true);
CREATE POLICY "public read medications"      ON medications      FOR SELECT USING (true);
CREATE POLICY "public read herbs"            ON herbs            FOR SELECT USING (true);
CREATE POLICY "public read medication_herbs" ON medication_herbs FOR SELECT USING (true);
CREATE POLICY "public read food_swaps"       ON food_swaps       FOR SELECT USING (true);
