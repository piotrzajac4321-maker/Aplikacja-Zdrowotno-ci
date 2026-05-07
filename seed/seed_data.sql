-- =====================================================
-- ZielonaApteka — dane startowe
-- Wykonaj w SQL Editor po seed/schema.sql.
-- Bezpieczne do wielokrotnego uruchamiania (ON CONFLICT DO NOTHING).
-- =====================================================

-- Kategorie ---------------------------------------------
INSERT INTO categories (slug, name_pl, description, icon, sort_order) VALUES
('bol',       'Ból',                'Leki i zioła stosowane przy bólu głowy, mięśni i stanach zapalnych.', '🤕', 10),
('sen',       'Sen i uspokojenie',  'Wsparcie zdrowego snu, redukcja stresu i napięcia nerwowego.',         '🌙', 20),
('trawienie', 'Trawienie',          'Niestrawność, wzdęcia, biegunka, zgaga i inne dolegliwości żołądka.',  '🌿', 30)
ON CONFLICT (slug) DO NOTHING;

-- Zioła -------------------------------------------------
INSERT INTO herbs (slug, name_pl, latin_name, description_pl, how_to_use_pl, cautions_pl) VALUES
('wierzba-biala',    'Wierzba biała',     'Salix alba',
 'Kora wierzby zawiera salicynę — naturalny prekursor kwasu salicylowego, działa przeciwbólowo, przeciwgorączkowo i przeciwzapalnie.',
 'Najczęściej w postaci naparu z kory (1 łyżeczka na szklankę wrzątku, 10–15 min) lub gotowych ekstraktów w tabletkach.',
 'Nie stosować przy alergii na salicylany, w ciąży, u dzieci poniżej 12 r.ż. oraz przy chorobach krzepnięcia krwi.'),
('wiazowka-blotna',  'Wiązówka błotna',   'Filipendula ulmaria',
 'Zawiera salicylany i flawonoidy — działa przeciwzapalnie, przeciwbólowo i przeciwgorączkowo, wspiera stawy.',
 'Napar z kwiatów: 1–2 łyżeczki na szklankę wrzątku, 2–3 razy dziennie.',
 'Przeciwwskazania jak przy wierzbie — alergia na salicylany, astma, ciąża.'),
('imbir',            'Imbir',             'Zingiber officinale',
 'Działa przeciwzapalnie, przeciwbólowo i przeciwwymiotnie. Pomaga przy bólach mięśni i miesiączkowych.',
 'Świeży korzeń (plasterki) zalany wrzątkiem, gotowe herbaty lub kapsułki.',
 'Ostrożnie przy lekach przeciwzakrzepowych i kamicy żółciowej.'),
('melisa-lekarska',  'Melisa lekarska',   'Melissa officinalis',
 'Łagodne działanie uspokajające, nasenne i rozkurczowe. Ułatwia zasypianie i redukuje stres.',
 'Napar z liści: 1–2 łyżeczki na szklankę wrzątku, wieczorem.',
 'Możliwe interakcje z lekami uspokajającymi i przeciwtarczycowymi.'),
('kozlek-lekarski',  'Kozłek lekarski (waleriana)', 'Valeriana officinalis',
 'Klasyczne zioło na bezsenność i niepokój. Działa wyciszająco bez efektu otępiającego rano.',
 'Napar z korzenia, krople lub tabletki — przyjmować 30–60 min przed snem.',
 'Nie łączyć z alkoholem i benzodiazepinami; ostrożnie przy prowadzeniu pojazdów.'),
('chmiel-zwyczajny', 'Chmiel zwyczajny',  'Humulus lupulus',
 'Szyszki chmielu działają uspokajająco i nasennie. Często łączone z walerianą i melisą.',
 'Napar z szyszek lub gotowe preparaty złożone.',
 'Nie zaleca się przy depresji oraz w ciąży.'),
('lawenda',          'Lawenda',           'Lavandula angustifolia',
 'Olejek i kwiaty lawendy redukują napięcie, lęk i poprawiają jakość snu.',
 'Napar z kwiatów, olejek do aromaterapii, kapsułki ze standaryzowanym ekstraktem.',
 'Olejek wyłącznie do użytku zewnętrznego lub wziewnego (poza preparatami doustnymi).'),
('czarna-jagoda',    'Czarna jagoda (borówka czernica)', 'Vaccinium myrtillus',
 'Suszone owoce mają działanie ściągające i przeciwbiegunkowe dzięki garbnikom.',
 'Odwar z suszonych owoców (1 łyżka na szklankę, gotować 10 min), 2–3 razy dziennie.',
 'Nie stosować dłużej niż kilka dni; uwaga na zaparcia przy przedawkowaniu.'),
('pieciornik',       'Pięciornik kurze ziele', 'Potentilla erecta',
 'Bogaty w garbniki — działa silnie ściągająco, przeciwbiegunkowo i przeciwzapalnie na śluzówki.',
 'Odwar z kłącza: 1 łyżeczka na szklankę, gotować 5 min.',
 'Krótkotrwale; przy wrażliwym żołądku może powodować mdłości.'),
('koper-wloski',     'Koper włoski',      'Foeniculum vulgare',
 'Owoce kopru działają wiatropędnie i rozkurczowo — łagodzą wzdęcia i kolki.',
 'Napar z rozgniecionych owoców: 1 łyżeczka na szklankę wrzątku, po posiłkach.',
 'Generalnie bezpieczny; ostrożnie przy alergii na rośliny baldaszkowate.'),
('mieta-pieprzowa',  'Mięta pieprzowa',   'Mentha × piperita',
 'Olejek mentolowy działa rozkurczowo na mięśnie gładkie przewodu pokarmowego.',
 'Napar z liści po posiłkach lub kapsułki dojelitowe z olejkiem (IBS).',
 'Nasila refluks żołądkowo-przełykowy; nie stosować u niemowląt.'),
('rumianek',         'Rumianek',          'Matricaria chamomilla',
 'Działa przeciwzapalnie, rozkurczowo i wiatropędnie. Łagodzi podrażnienia żołądka.',
 'Napar z koszyczków kwiatowych: 1 łyżka na szklankę wrzątku.',
 'Rzadkie alergie krzyżowe (ambrozja).'),
('lukrecja',         'Lukrecja',          'Glycyrrhiza glabra',
 'Korzeń lukrecji wspomaga regenerację błony śluzowej żołądka, łagodzi zgagę.',
 'Odwar z korzenia lub gotowe ekstrakty DGL (deglicyrrhized).',
 'Długotrwałe stosowanie podnosi ciśnienie krwi i obniża potas. Nie w nadciśnieniu i ciąży.'),
('siemie-lniane',    'Siemię lniane',     'Linum usitatissimum',
 'Śluzy roślinne pokrywają śluzówkę żołądka i przełyku — łagodzą zgagę i podrażnienia.',
 'Macerat: 1 łyżka nasion zalana letnią wodą na 20–30 min, pić ze śluzem.',
 'Świeżo zmielone siemię — krótkotrwałe przechowywanie.'),
('prawoslaz',        'Prawoślaz lekarski','Althaea officinalis',
 'Korzeń prawoślazu zawiera śluzy łagodzące podrażnienia gardła, przełyku i żołądka.',
 'Macerat na zimno z korzenia (1 łyżka na szklankę, 1–2 godz.).',
 'Może opóźniać wchłanianie innych leków — odstęp 1–2 godz.')
ON CONFLICT (slug) DO NOTHING;

-- Leki --------------------------------------------------
INSERT INTO medications (slug, name_pl, active_substance, brand_examples, purpose_pl, description_pl, side_effects_pl, category_id)
SELECT * FROM (VALUES
('ibuprofen',    'Ibuprofen',    'Ibuprofen',                'Ibuprom, Nurofen, MIG',
 'Ból, gorączka, stany zapalne',
 'Niesteroidowy lek przeciwzapalny (NLPZ) o działaniu przeciwbólowym, przeciwzapalnym i przeciwgorączkowym. Stosowany w bólu głowy, mięśni, miesiączkowym i przy infekcjach.',
 'Podrażnienie żołądka, nudności, ryzyko krwawień z przewodu pokarmowego, wzrost ciśnienia.',
 (SELECT id FROM categories WHERE slug='bol')),
('paracetamol',  'Paracetamol',  'Paracetamol',              'Apap, Panadol, Codipar',
 'Ból, gorączka',
 'Łagodny lek przeciwbólowy i przeciwgorączkowy. Nie ma działania przeciwzapalnego, ale jest dobrze tolerowany przez żołądek.',
 'Przy przedawkowaniu — toksyczne uszkodzenie wątroby. Ostrożnie z alkoholem.',
 (SELECT id FROM categories WHERE slug='bol')),
('aspiryna',     'Aspiryna',     'Kwas acetylosalicylowy',   'Polopiryna, Aspirin',
 'Ból, gorączka, profilaktyka sercowo-naczyniowa',
 'Klasyczny NLPZ. W małych dawkach stosowany jako lek przeciwzakrzepowy. W większych — przeciwbólowo i przeciwzapalnie.',
 'Krwawienia z przewodu pokarmowego, alergie, zespół Reye u dzieci.',
 (SELECT id FROM categories WHERE slug='bol')),
('melatonina',   'Melatonina',   'Melatonina',               'Melatonina LEK-AM, Circadin',
 'Trudności z zasypianiem, jet lag',
 'Hormon wytwarzany przez szyszynkę regulujący rytm dobowy. Stosowany przy bezsenności i zmianach stref czasowych.',
 'Senność rano, bóle głowy, żywe sny. Może wchodzić w interakcje z lekami przeciwzakrzepowymi.',
 (SELECT id FROM categories WHERE slug='sen')),
('hydroksyzyna', 'Hydroksyzyna', 'Hydroksyzyna',             'Atarax, Hydroxyzinum VP',
 'Lęk, niepokój, bezsenność',
 'Lek przeciwhistaminowy o działaniu uspokajającym i przeciwlękowym. Wymaga recepty.',
 'Senność, suchość w ustach, zaburzenia rytmu serca (długie QT). Nie łączyć z alkoholem.',
 (SELECT id FROM categories WHERE slug='sen')),
('loperamid',    'Loperamid',    'Loperamid',                'Stoperan, Imodium, Laremid',
 'Biegunka',
 'Hamuje perystaltykę jelit, wskazany w ostrej, niezakaźnej biegunce u dorosłych.',
 'Zaparcia, bóle brzucha. Niewskazany w biegunce z gorączką lub krwią w stolcu.',
 (SELECT id FROM categories WHERE slug='trawienie')),
('espumisan',    'Espumisan',    'Symetykon',                'Espumisan, Esputicon',
 'Wzdęcia, gazy',
 'Środek przeciwpieniący — rozbija pęcherzyki gazu w jelitach. Nie wchłania się do krwiobiegu.',
 'Praktycznie brak; rzadko reakcje alergiczne.',
 (SELECT id FROM categories WHERE slug='trawienie')),
('omeprazol',    'Omeprazol',    'Omeprazol',                'Polprazol, Helicid, Bioprazol',
 'Zgaga, refluks, choroba wrzodowa',
 'Inhibitor pompy protonowej — zmniejsza wydzielanie kwasu solnego w żołądku.',
 'Bóle głowy, biegunka, długotrwale — niedobór B12 i magnezu, ryzyko złamań.',
 (SELECT id FROM categories WHERE slug='trawienie'))
) AS v(slug, name_pl, active_substance, brand_examples, purpose_pl, description_pl, side_effects_pl, category_id)
ON CONFLICT (slug) DO NOTHING;

-- Powiązania lek <-> zioło ------------------------------
INSERT INTO medication_herbs (medication_id, herb_id, rationale_pl, strength)
SELECT m.id, h.id, r.rationale, r.strength
FROM (VALUES
('ibuprofen',    'wierzba-biala',    'Naturalny salicylan o działaniu przeciwbólowym i przeciwzapalnym — botaniczny pierwowzór aspiryny.', 4),
('ibuprofen',    'wiazowka-blotna',  'Bogata w salicylany — wspiera stawy i działa przeciwzapalnie.', 3),
('paracetamol',  'wierzba-biala',    'Łagodny efekt przeciwbólowy i przeciwgorączkowy.', 3),
('paracetamol',  'imbir',            'Działa przeciwbólowo i przeciwzapalnie, szczególnie w bólach mięśni i miesiączkowych.', 3),
('aspiryna',     'wierzba-biala',    'Bezpośredni botaniczny odpowiednik — kora wierzby była pierwowzorem aspiryny.', 5),
('aspiryna',     'wiazowka-blotna',  'Druga klasyczna roślina salicylanowa.', 4),
('melatonina',   'melisa-lekarska',  'Łagodzi zasypianie i redukuje napięcie wieczorem.', 3),
('melatonina',   'kozlek-lekarski',  'Skraca czas zasypiania i poprawia jakość snu.', 4),
('hydroksyzyna', 'melisa-lekarska',  'Działa przeciwlękowo i uspokajająco.', 3),
('hydroksyzyna', 'chmiel-zwyczajny', 'Wzmacnia działanie waleriany i melisy.', 3),
('hydroksyzyna', 'lawenda',          'Redukuje lęk, poprawia jakość snu.', 4),
('loperamid',    'czarna-jagoda',    'Garbniki działają ściągająco i przeciwbiegunkowo.', 4),
('loperamid',    'pieciornik',       'Silne działanie ściągające na śluzówkę jelit.', 4),
('espumisan',    'koper-wloski',     'Wiatropędnie usuwa nadmiar gazów i łagodzi kolki.', 4),
('espumisan',    'mieta-pieprzowa',  'Rozkurcza mięśnie gładkie jelit.', 4),
('espumisan',    'rumianek',         'Łagodzi podrażnienia i wspiera trawienie.', 3),
('omeprazol',    'lukrecja',         'Wspiera regenerację błony śluzowej żołądka — szczególnie postać DGL.', 4),
('omeprazol',    'siemie-lniane',    'Śluzy chronią przełyk i żołądek przed kwasem.', 3),
('omeprazol',    'prawoslaz',        'Tworzy ochronną warstwę śluzu na śluzówce.', 3)
) AS r(med_slug, herb_slug, rationale, strength)
JOIN medications m ON m.slug = r.med_slug
JOIN herbs       h ON h.slug = r.herb_slug
ON CONFLICT (medication_id, herb_id) DO NOTHING;
