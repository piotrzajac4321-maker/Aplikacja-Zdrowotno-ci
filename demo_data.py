"""Przykładowe dane do podglądu wyglądu aplikacji bez Supabase.

Struktura odzwierciedla to, co normalnie zwraca Supabase, dzięki czemu te same
szablony Jinja2 działają zarówno w trybie demo, jak i z prawdziwą bazą.
"""

CATEGORIES = [
    {"id": 1, "slug": "bol", "name_pl": "Ból", "icon": "🤕", "sort_order": 10,
     "description": "Leki i zioła stosowane przy bólu głowy, mięśni i stanach zapalnych."},
    {"id": 2, "slug": "sen", "name_pl": "Sen i uspokojenie", "icon": "🌙", "sort_order": 20,
     "description": "Wsparcie zdrowego snu, redukcja stresu i napięcia nerwowego."},
    {"id": 3, "slug": "trawienie", "name_pl": "Trawienie", "icon": "🌿", "sort_order": 30,
     "description": "Niestrawność, wzdęcia, biegunka, zgaga i inne dolegliwości żołądka."},
]

HERBS = [
    {"id": 1,  "slug": "wierzba-biala",   "name_pl": "Wierzba biała",   "latin_name": "Salix alba",
     "description_pl": "Kora wierzby zawiera salicynę — naturalny prekursor kwasu salicylowego.",
     "how_to_use_pl": "Napar z kory: 1 łyżeczka na szklankę wrzątku, 10–15 min, lub kapsułki.",
     "cautions_pl":   "Nie stosować przy alergii na salicylany, w ciąży i u dzieci poniżej 12 r.ż."},
    {"id": 2,  "slug": "wiazowka-blotna", "name_pl": "Wiązówka błotna", "latin_name": "Filipendula ulmaria",
     "description_pl": "Salicylany i flawonoidy — działanie przeciwzapalne i przeciwgorączkowe.",
     "how_to_use_pl": "Napar z kwiatów: 1–2 łyżeczki na szklankę, 2–3 razy dziennie.",
     "cautions_pl":   "Alergia na salicylany, astma, ciąża."},
    {"id": 3,  "slug": "imbir",           "name_pl": "Imbir",           "latin_name": "Zingiber officinale",
     "description_pl": "Działa przeciwzapalnie, przeciwbólowo i przeciwwymiotnie.",
     "how_to_use_pl": "Świeży korzeń, herbaty lub kapsułki.",
     "cautions_pl":   "Ostrożnie przy lekach przeciwzakrzepowych i kamicy żółciowej."},
    {"id": 4,  "slug": "melisa-lekarska", "name_pl": "Melisa lekarska", "latin_name": "Melissa officinalis",
     "description_pl": "Łagodne uspokajające, nasenne i rozkurczowe.",
     "how_to_use_pl": "Napar z liści: 1–2 łyżeczki na szklankę, wieczorem.",
     "cautions_pl":   "Możliwe interakcje z lekami uspokajającymi."},
    {"id": 5,  "slug": "kozlek-lekarski", "name_pl": "Kozłek lekarski (waleriana)", "latin_name": "Valeriana officinalis",
     "description_pl": "Klasyczne zioło na bezsenność i niepokój.",
     "how_to_use_pl": "Krople, tabletki lub napar z korzenia, 30–60 min przed snem.",
     "cautions_pl":   "Nie łączyć z alkoholem i benzodiazepinami."},
    {"id": 6,  "slug": "chmiel-zwyczajny","name_pl": "Chmiel zwyczajny","latin_name": "Humulus lupulus",
     "description_pl": "Szyszki działają uspokajająco i nasennie.",
     "how_to_use_pl": "Napar z szyszek lub preparaty złożone.",
     "cautions_pl":   "Nie zaleca się przy depresji oraz w ciąży."},
    {"id": 7,  "slug": "lawenda",         "name_pl": "Lawenda",         "latin_name": "Lavandula angustifolia",
     "description_pl": "Olejek i kwiaty redukują napięcie i lęk.",
     "how_to_use_pl": "Napar z kwiatów, aromaterapia, kapsułki.",
     "cautions_pl":   "Olejek wyłącznie zewnętrznie/wziewnie."},
    {"id": 8,  "slug": "czarna-jagoda",   "name_pl": "Czarna jagoda (borówka czernica)", "latin_name": "Vaccinium myrtillus",
     "description_pl": "Suszone owoce — działanie ściągające i przeciwbiegunkowe.",
     "how_to_use_pl": "Odwar z suszonych owoców, 2–3 razy dziennie.",
     "cautions_pl":   "Krótkotrwale; uwaga na zaparcia."},
    {"id": 9,  "slug": "pieciornik",      "name_pl": "Pięciornik kurze ziele", "latin_name": "Potentilla erecta",
     "description_pl": "Bogaty w garbniki — silne działanie ściągające.",
     "how_to_use_pl": "Odwar z kłącza: 1 łyżeczka na szklankę, 5 min.",
     "cautions_pl":   "Krótkotrwale; może powodować mdłości."},
    {"id": 10, "slug": "koper-wloski",    "name_pl": "Koper włoski",    "latin_name": "Foeniculum vulgare",
     "description_pl": "Owoce kopru działają wiatropędnie i rozkurczowo.",
     "how_to_use_pl": "Napar z rozgniecionych owoców po posiłkach.",
     "cautions_pl":   "Alergia na rośliny baldaszkowate."},
    {"id": 11, "slug": "mieta-pieprzowa", "name_pl": "Mięta pieprzowa", "latin_name": "Mentha × piperita",
     "description_pl": "Olejek mentolowy działa rozkurczowo na jelita.",
     "how_to_use_pl": "Napar z liści lub kapsułki dojelitowe (IBS).",
     "cautions_pl":   "Nasila refluks; nie u niemowląt."},
    {"id": 12, "slug": "rumianek",        "name_pl": "Rumianek",        "latin_name": "Matricaria chamomilla",
     "description_pl": "Przeciwzapalnie, rozkurczowo i wiatropędnie.",
     "how_to_use_pl": "Napar z koszyczków: 1 łyżka na szklankę.",
     "cautions_pl":   "Rzadkie alergie krzyżowe (ambrozja)."},
    {"id": 13, "slug": "lukrecja",        "name_pl": "Lukrecja",        "latin_name": "Glycyrrhiza glabra",
     "description_pl": "Korzeń wspomaga regenerację błony śluzowej żołądka.",
     "how_to_use_pl": "Odwar lub ekstrakty DGL (deglicyrrhized).",
     "cautions_pl":   "Długotrwale podnosi ciśnienie. Nie w nadciśnieniu i ciąży."},
    {"id": 14, "slug": "siemie-lniane",   "name_pl": "Siemię lniane",   "latin_name": "Linum usitatissimum",
     "description_pl": "Śluzy pokrywają śluzówkę żołądka — łagodzą zgagę.",
     "how_to_use_pl": "Macerat: 1 łyżka nasion w letniej wodzie 20–30 min.",
     "cautions_pl":   "Świeżo zmielone — krótkie przechowywanie."},
    {"id": 15, "slug": "prawoslaz",       "name_pl": "Prawoślaz lekarski", "latin_name": "Althaea officinalis",
     "description_pl": "Korzeń zawiera śluzy łagodzące podrażnienia.",
     "how_to_use_pl": "Macerat na zimno z korzenia, 1–2 godz.",
     "cautions_pl":   "Może opóźniać wchłanianie innych leków — odstęp 1–2 h."},
    {"id": 16, "slug": "harpagofyt",      "name_pl": "Czarci pazur (harpagofyt)", "latin_name": "Harpagophytum procumbens",
     "description_pl": "Korzeń o silnym działaniu przeciwbólowym i przeciwzapalnym, szczególnie w bólach stawów.",
     "how_to_use_pl": "Standaryzowane kapsułki 400–600 mg dziennie.",
     "cautions_pl":   "Wrzody, kamica żółciowa, ciąża; obniża cukier."},
    {"id": 17, "slug": "dziurawiec",      "name_pl": "Dziurawiec zwyczajny", "latin_name": "Hypericum perforatum",
     "description_pl": "Tradycyjnie przy łagodnej depresji, niepokoju i bezsenności.",
     "how_to_use_pl": "Napar: 1 łyżeczka na szklankę, 2 razy dziennie.",
     "cautions_pl":   "Bardzo dużo interakcji lekowych! Fotouczulający."},
    {"id": 18, "slug": "owies",           "name_pl": "Owies zwyczajny", "latin_name": "Avena sativa",
     "description_pl": "Niedojrzałe ziarno odżywia układ nerwowy.",
     "how_to_use_pl": "Owsianka, napar ze słomy, nalewki.",
     "cautions_pl":   "Uwaga przy celiakii (zanieczyszczenia)."},
    {"id": 19, "slug": "senes",           "name_pl": "Senes (strączyniec)", "latin_name": "Senna alexandrina",
     "description_pl": "Liście i strąki działają silnie przeczyszczająco.",
     "how_to_use_pl": "Napar lub tabletki, krótkotrwale.",
     "cautions_pl":   "Nie przewlekle, nie w ciąży i u dzieci."},
    {"id": 20, "slug": "babka-jajowata",  "name_pl": "Babka jajowata (psyllium)", "latin_name": "Plantago ovata",
     "description_pl": "Łuski tworzą żel — błonnik regulujący wypróżnienia.",
     "how_to_use_pl": "Łyżeczka łusek z dużą szklanką wody dziennie.",
     "cautions_pl":   "Pij dużo wody; odstęp 2 h od leków."},
    {"id": 21, "slug": "ostropest",       "name_pl": "Ostropest plamisty", "latin_name": "Silybum marianum",
     "description_pl": "Sylimaryna chroni komórki wątroby.",
     "how_to_use_pl": "Mielone nasiona (1 łyżka dziennie) lub kapsułki.",
     "cautions_pl":   "Możliwa alergia u uczulonych na astrowate."},
    {"id": 22, "slug": "karczoch",        "name_pl": "Karczoch zwyczajny", "latin_name": "Cynara scolymus",
     "description_pl": "Pobudza wydzielanie żółci i trawienie tłuszczów.",
     "how_to_use_pl": "Kapsułki z ekstraktem lub napar.",
     "cautions_pl":   "Niedrożność dróg żółciowych, kamica."},
    {"id": 23, "slug": "mniszek",         "name_pl": "Mniszek lekarski", "latin_name": "Taraxacum officinale",
     "description_pl": "Wspiera wątrobę i nerki, działa moczopędnie.",
     "how_to_use_pl": "Napar, kawa z korzenia mniszka.",
     "cautions_pl":   "Niedrożność dróg żółciowych."},
]

MEDICATIONS = [
    {"id": 1, "slug": "ibuprofen",    "name_pl": "Ibuprofen",
     "active_substance": "Ibuprofen", "brand_examples": "Ibuprom, Nurofen, MIG",
     "purpose_pl": "Ból, gorączka, stany zapalne",
     "description_pl": "Niesteroidowy lek przeciwzapalny (NLPZ). Stosowany w bólu głowy, mięśni, miesiączkowym i przy infekcjach.",
     "side_effects_pl": "Podrażnienie żołądka, nudności, ryzyko krwawień z przewodu pokarmowego, wzrost ciśnienia.",
     "category_id": 1},
    {"id": 2, "slug": "paracetamol",  "name_pl": "Paracetamol",
     "active_substance": "Paracetamol", "brand_examples": "Apap, Panadol, Codipar",
     "purpose_pl": "Ból, gorączka",
     "description_pl": "Łagodny lek przeciwbólowy i przeciwgorączkowy. Dobrze tolerowany przez żołądek.",
     "side_effects_pl": "Przy przedawkowaniu — toksyczne uszkodzenie wątroby.",
     "category_id": 1},
    {"id": 3, "slug": "aspiryna",     "name_pl": "Aspiryna",
     "active_substance": "Kwas acetylosalicylowy", "brand_examples": "Polopiryna, Aspirin",
     "purpose_pl": "Ból, gorączka, profilaktyka sercowo-naczyniowa",
     "description_pl": "Klasyczny NLPZ. W małych dawkach — przeciwzakrzepowo. W większych — przeciwbólowo i przeciwzapalnie.",
     "side_effects_pl": "Krwawienia z przewodu pokarmowego, alergie, zespół Reye u dzieci.",
     "category_id": 1},
    {"id": 4, "slug": "melatonina",   "name_pl": "Melatonina",
     "active_substance": "Melatonina", "brand_examples": "Melatonina LEK-AM, Circadin",
     "purpose_pl": "Trudności z zasypianiem, jet lag",
     "description_pl": "Hormon szyszynki regulujący rytm dobowy. Pomaga przy bezsenności i zmianach stref czasowych.",
     "side_effects_pl": "Senność rano, bóle głowy, żywe sny.",
     "category_id": 2},
    {"id": 5, "slug": "hydroksyzyna", "name_pl": "Hydroksyzyna",
     "active_substance": "Hydroksyzyna", "brand_examples": "Atarax, Hydroxyzinum VP",
     "purpose_pl": "Lęk, niepokój, bezsenność",
     "description_pl": "Lek przeciwhistaminowy o działaniu uspokajającym i przeciwlękowym. Wymaga recepty.",
     "side_effects_pl": "Senność, suchość w ustach, zaburzenia rytmu serca.",
     "category_id": 2},
    {"id": 6, "slug": "loperamid",    "name_pl": "Loperamid",
     "active_substance": "Loperamid", "brand_examples": "Stoperan, Imodium, Laremid",
     "purpose_pl": "Biegunka",
     "description_pl": "Hamuje perystaltykę jelit, wskazany w ostrej, niezakaźnej biegunce.",
     "side_effects_pl": "Zaparcia, bóle brzucha. Niewskazany przy gorączce lub krwi w stolcu.",
     "category_id": 3},
    {"id": 7, "slug": "espumisan",    "name_pl": "Espumisan",
     "active_substance": "Symetykon", "brand_examples": "Espumisan, Esputicon",
     "purpose_pl": "Wzdęcia, gazy",
     "description_pl": "Środek przeciwpieniący — rozbija pęcherzyki gazu w jelitach.",
     "side_effects_pl": "Praktycznie brak; rzadko reakcje alergiczne.",
     "category_id": 3},
    {"id": 8, "slug": "omeprazol",    "name_pl": "Omeprazol",
     "active_substance": "Omeprazol", "brand_examples": "Polprazol, Helicid, Bioprazol",
     "purpose_pl": "Zgaga, refluks, choroba wrzodowa",
     "description_pl": "Inhibitor pompy protonowej — zmniejsza wydzielanie kwasu solnego.",
     "side_effects_pl": "Bóle głowy, biegunka; długotrwale — niedobór B12 i magnezu.",
     "category_id": 3},
    {"id": 9, "slug": "ketoprofen",   "name_pl": "Ketoprofen",
     "active_substance": "Ketoprofen", "brand_examples": "Ketonal, Bi-Profenid, Profenid",
     "purpose_pl": "Ból, stany zapalne stawów",
     "description_pl": "NLPZ silnie przeciwbólowy — bóle stawów, mięśni, pooperacyjne.",
     "side_effects_pl": "Podrażnienie żołądka, owrzodzenia, problemy nerkowe, fotoalergia.",
     "category_id": 1},
    {"id": 10, "slug": "diclofenac",  "name_pl": "Diclofenac",
     "active_substance": "Diklofenak", "brand_examples": "Voltaren, Olfen, Naklofen",
     "purpose_pl": "Ból, zapalenie stawów",
     "description_pl": "NLPZ doustny i miejscowy (żel) — bóle kostno-stawowe, urazy, dna.",
     "side_effects_pl": "Powikłania sercowo-naczyniowe przy długim stosowaniu, podrażnienie żołądka.",
     "category_id": 1},
    {"id": 11, "slug": "naproksen",   "name_pl": "Naproksen",
     "active_substance": "Naproksen", "brand_examples": "Naproxen, Aleve, Naprosyn",
     "purpose_pl": "Ból, gorączka, zapalenie",
     "description_pl": "NLPZ o długim działaniu (do 12 h). Bóle miesiączkowe i głowy.",
     "side_effects_pl": "Podrażnienie żołądka, retencja płynów, ostrożnie u sercowych.",
     "category_id": 1},
    {"id": 12, "slug": "drotaweryna", "name_pl": "No-Spa",
     "active_substance": "Drotaweryna", "brand_examples": "No-Spa, Galospa, Drotaverin",
     "purpose_pl": "Bóle skurczowe (kolka, miesiączkowy)",
     "description_pl": "Lek rozkurczowy na mięśnie gładkie — kolka jelitowa, żółciowa, nerkowa.",
     "side_effects_pl": "Spadki ciśnienia, zawroty głowy.",
     "category_id": 1},
    {"id": 13, "slug": "doksylamina", "name_pl": "Doksylamina",
     "active_substance": "Doksylamina", "brand_examples": "Noctis, Donormyl",
     "purpose_pl": "Krótkotrwała bezsenność",
     "description_pl": "Antyhistaminowy I generacji o silnym działaniu nasennym. Bez recepty.",
     "side_effects_pl": "Senność rano, suchość w ustach, zaparcia.",
     "category_id": 2},
    {"id": 14, "slug": "magne-b6",    "name_pl": "Magne B6",
     "active_substance": "Magnez + witamina B6", "brand_examples": "Magne B6, Magnefar B6, Slow Mag",
     "purpose_pl": "Niedobór magnezu, napięcie nerwowe, sen",
     "description_pl": "Suplementacja magnezu z B6 wspiera układ nerwowy i sen.",
     "side_effects_pl": "Biegunka przy dużych dawkach.",
     "category_id": 2},
    {"id": 15, "slug": "zolpidem",    "name_pl": "Stilnox (Zolpidem)",
     "active_substance": "Zolpidem", "brand_examples": "Stilnox, Hypnogen, Nasen",
     "purpose_pl": "Ciężka bezsenność (na receptę)",
     "description_pl": "Niebenzodiazepinowy lek nasenny o szybkim działaniu, krótkotrwale.",
     "side_effects_pl": "Uzależnienie, ataksja, halucynacje, lunatykowanie.",
     "category_id": 2},
    {"id": 16, "slug": "ranitydyna",  "name_pl": "Ranigast",
     "active_substance": "Ranitydyna / Famotydyna", "brand_examples": "Ranigast, Pepcid, Famogast",
     "purpose_pl": "Zgaga, nadkwaśność",
     "description_pl": "Bloker H2 — łagodniejszy od IPP.",
     "side_effects_pl": "Bóle głowy, biegunka.",
     "category_id": 3},
    {"id": 17, "slug": "smecta",      "name_pl": "Smecta",
     "active_substance": "Diosmektyt", "brand_examples": "Smecta, Smectago",
     "purpose_pl": "Ostra biegunka",
     "description_pl": "Krzemian glinu wiążący toksyny i drobnoustroje.",
     "side_effects_pl": "Zaparcia; odstęp 2 h od innych leków.",
     "category_id": 3},
    {"id": 18, "slug": "bisakodyl",   "name_pl": "Dulcolax (Bisakodyl)",
     "active_substance": "Bisakodyl", "brand_examples": "Dulcolax, Bisacodyl",
     "purpose_pl": "Zaparcia",
     "description_pl": "Stymuluje perystaltykę jelita grubego po 6–12 godzinach.",
     "side_effects_pl": "Skurcze, biegunka, utrata elektrolitów.",
     "category_id": 3},
    {"id": 19, "slug": "forlax",      "name_pl": "Forlax (Makrogol)",
     "active_substance": "Makrogol 4000", "brand_examples": "Forlax, Movicol, Fortrans",
     "purpose_pl": "Zaparcia",
     "description_pl": "Osmotyczny — wiąże wodę w jelicie. Bezpieczny długoterminowo.",
     "side_effects_pl": "Wzdęcia, lekkie odwodnienie.",
     "category_id": 3},
    {"id": 20, "slug": "hepatil",     "name_pl": "Hepatil",
     "active_substance": "Asparaginian L-ornityny", "brand_examples": "Hepatil, Hepatil Trawienie",
     "purpose_pl": "Wsparcie wątroby",
     "description_pl": "Wspomaga detoksykację amoniaku w wątrobie.",
     "side_effects_pl": "Generalnie bezpieczny; ostrożnie przy nerkach.",
     "category_id": 3},
]

# (medication_slug, herb_slug, rationale, strength)
MEDICATION_HERBS = [
    ("ibuprofen",    "wierzba-biala",    "Naturalny salicylan — botaniczny pierwowzór aspiryny.", 4),
    ("ibuprofen",    "wiazowka-blotna",  "Bogata w salicylany — wspiera stawy i działa przeciwzapalnie.", 3),
    ("paracetamol",  "wierzba-biala",    "Łagodny efekt przeciwbólowy i przeciwgorączkowy.", 3),
    ("paracetamol",  "imbir",            "Działa przeciwbólowo i przeciwzapalnie.", 3),
    ("aspiryna",     "wierzba-biala",    "Bezpośredni botaniczny odpowiednik aspiryny.", 5),
    ("aspiryna",     "wiazowka-blotna",  "Druga klasyczna roślina salicylanowa.", 4),
    ("melatonina",   "melisa-lekarska",  "Łagodzi zasypianie i redukuje napięcie wieczorem.", 3),
    ("melatonina",   "kozlek-lekarski",  "Skraca czas zasypiania i poprawia jakość snu.", 4),
    ("hydroksyzyna", "melisa-lekarska",  "Działa przeciwlękowo i uspokajająco.", 3),
    ("hydroksyzyna", "chmiel-zwyczajny", "Wzmacnia działanie waleriany i melisy.", 3),
    ("hydroksyzyna", "lawenda",          "Redukuje lęk, poprawia jakość snu.", 4),
    ("loperamid",    "czarna-jagoda",    "Garbniki działają ściągająco i przeciwbiegunkowo.", 4),
    ("loperamid",    "pieciornik",       "Silne działanie ściągające na śluzówkę jelit.", 4),
    ("espumisan",    "koper-wloski",     "Wiatropędnie usuwa gazy i łagodzi kolki.", 4),
    ("espumisan",    "mieta-pieprzowa",  "Rozkurcza mięśnie gładkie jelit.", 4),
    ("espumisan",    "rumianek",         "Łagodzi podrażnienia i wspiera trawienie.", 3),
    ("omeprazol",    "lukrecja",         "Wspiera regenerację błony śluzowej żołądka.", 4),
    ("omeprazol",    "siemie-lniane",    "Śluzy chronią przełyk i żołądek przed kwasem.", 3),
    ("omeprazol",    "prawoslaz",        "Tworzy ochronną warstwę śluzu na śluzówce.", 3),
    ("ketoprofen",   "wierzba-biala",    "Salicylany działają przeciwzapalnie i przeciwbólowo.", 4),
    ("ketoprofen",   "harpagofyt",       "Czarci pazur — silne wsparcie przy bólach stawów i kręgosłupa.", 5),
    ("ketoprofen",   "imbir",            "Działa przeciwzapalnie i przeciwbólowo na stawy.", 3),
    ("diclofenac",   "wierzba-biala",    "Naturalny salicylan o działaniu przeciwzapalnym.", 4),
    ("diclofenac",   "harpagofyt",       "Tradycyjne wsparcie przy zapaleniach stawów.", 4),
    ("diclofenac",   "wiazowka-blotna",  "Salicylany roślinne łagodzące stany zapalne.", 3),
    ("naproksen",    "wierzba-biala",    "Klasyczny botaniczny prekursor NLPZ.", 4),
    ("naproksen",    "wiazowka-blotna",  "Wspiera leczenie bólów reumatycznych.", 3),
    ("drotaweryna",  "mieta-pieprzowa",  "Olejek mentolowy rozkurcza mięśnie gładkie jelit.", 4),
    ("drotaweryna",  "koper-wloski",     "Działa rozkurczowo i wiatropędnie.", 3),
    ("drotaweryna",  "melisa-lekarska",  "Łagodne działanie rozkurczowe i uspokajające.", 3),
    ("doksylamina",  "kozlek-lekarski",  "Tradycyjne zioło na sen.", 4),
    ("doksylamina",  "melisa-lekarska",  "Łagodzi zasypianie.", 3),
    ("doksylamina",  "chmiel-zwyczajny", "Działa nasennie, wzmacnia walerianę.", 3),
    ("magne-b6",     "owies",            "Niedojrzałe ziarno owsa odżywia układ nerwowy.", 3),
    ("magne-b6",     "melisa-lekarska",  "Łagodzi napięcie nerwowe.", 3),
    ("zolpidem",     "kozlek-lekarski",  "Najsilniejsze tradycyjne zioło na bezsenność.", 4),
    ("zolpidem",     "chmiel-zwyczajny", "Wzmacnia działanie waleriany.", 3),
    ("zolpidem",     "lawenda",          "Redukuje napięcie i lęk wieczorem.", 3),
    ("ranitydyna",   "lukrecja",         "DGL wspiera regenerację błony śluzowej.", 4),
    ("ranitydyna",   "prawoslaz",        "Tworzy ochronną warstwę śluzu.", 3),
    ("ranitydyna",   "siemie-lniane",    "Łagodzi zgagę i podrażnienia.", 3),
    ("smecta",       "czarna-jagoda",    "Garbniki działają ściągająco i przeciwbiegunkowo.", 4),
    ("smecta",       "pieciornik",       "Silne działanie ściągające na śluzówkę jelit.", 4),
    ("smecta",       "prawoslaz",        "Łagodzi podrażnienia śluzówki.", 3),
    ("bisakodyl",    "senes",            "Tradycyjny stymulujący środek przeczyszczający.", 4),
    ("bisakodyl",    "babka-jajowata",   "Łagodniejsza alternatywa — błonnik regulujący wypróżnienia.", 3),
    ("forlax",       "siemie-lniane",    "Łagodne działanie regulujące jelita poprzez śluzy.", 4),
    ("forlax",       "babka-jajowata",   "Psyllium reguluje wypróżnienia bez podrażnień.", 5),
    ("hepatil",      "ostropest",        "Sylimaryna chroni i regeneruje komórki wątroby.", 5),
    ("hepatil",      "karczoch",         "Wspiera wydzielanie żółci i trawienie tłuszczów.", 4),
    ("hepatil",      "mniszek",          "Wspomaga oczyszczanie wątroby.", 3),
]


# --- Helpery odpowiadające zapytaniom Supabase --------------------------------

def _category_by_id(cid):
    return next((c for c in CATEGORIES if c["id"] == cid), None)


def _herb_by_slug(slug):
    return next((h for h in HERBS if h["slug"] == slug), None)


def categories():
    return sorted(CATEGORIES, key=lambda c: c["sort_order"])


def category(slug):
    return next((c for c in CATEGORIES if c["slug"] == slug), None)


def medications_by_category(category_id):
    out = []
    for m in MEDICATIONS:
        if m["category_id"] != category_id:
            continue
        herb_count = sum(1 for (mslug, _, _, _) in MEDICATION_HERBS if mslug == m["slug"])
        out.append({**m, "herb_count": herb_count, "categories": _category_by_id(m["category_id"])})
    return sorted(out, key=lambda m: m["name_pl"])


def medication_detail(slug):
    med = next((m for m in MEDICATIONS if m["slug"] == slug), None)
    if not med:
        return None
    cat = _category_by_id(med["category_id"])
    links = []
    for (mslug, hslug, rationale, strength) in MEDICATION_HERBS:
        if mslug != slug:
            continue
        herb = _herb_by_slug(hslug)
        if herb:
            links.append({"rationale_pl": rationale, "strength": strength, "herbs": herb})
    return {**med, "categories": cat, "medication_herbs": links}


def featured_pairs(limit=4):
    pairs = []
    for med in MEDICATIONS[:limit]:
        first = next(((h, r) for (m, h, r, _) in MEDICATION_HERBS if m == med["slug"]), None)
        if not first:
            continue
        herb = _herb_by_slug(first[0])
        pairs.append({
            "medication": {**med, "categories": _category_by_id(med["category_id"])},
            "herb": herb,
        })
    return pairs


def search(query):
    q = (query or "").strip().lower()
    if not q:
        return []
    out = []
    for m in MEDICATIONS:
        haystack = " ".join(filter(None, [m.get("name_pl"), m.get("active_substance"), m.get("brand_examples")])).lower()
        if q in haystack:
            out.append({**m, "categories": _category_by_id(m["category_id"])})
    return sorted(out, key=lambda m: m["name_pl"])
