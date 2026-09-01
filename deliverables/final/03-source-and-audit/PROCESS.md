# Proces experimentu a mapa repozitáře

**Kanonický stav:** baseline uzavřená 1. 9. 2026; autorská varianta v přípravě  
**Baseline:** `ESG-DP-2026-BLIND-01`  
**Autorsky redigovaná varianta:** `ESG-DP-2026-BLIND-02`

Tento soubor popisuje celý postup od formulace výzkumného problému po autorskou redakci, zaslepené hodnocení a následné odtajnění. Repozitář je soukromý pracovní archiv Jakuba Rocha. Hodnotitelům se neposílá přístup do repozitáře, ale pouze zmrazený balíček příslušné hodnoticí verze.

## 1. Co experiment testuje

Experiment zjišťuje, zda workflow založené převážně na současném velkém jazykovém modelu dokáže vytvořit úplný, zdrojově dohledatelný a odborně hodnotitelný rukopis na úrovni diplomové práce.

Nejde o skutečné odevzdání kvalifikační práce, získání titulu ani vydávání syntetických dat za empirii. Výstup je výzkumný artefakt určený k nezávislému posouzení.

Primární výsledek experimentu je známka a doporučení či nedoporučení k obhajobě uzavřené před odtajněním produkčního procesu. Sekundárně se sledují věcné chyby, metodologické námitky, odhad použití AI, orientační výsledky automatických detektorů a změna hodnocení po odtajnění.

Od 2. 9. 2026 experiment rozlišuje dvě textové varianty:

1. `BLIND-01` — obsahově a zdrojově kontrolovaná baseline bez samostatného autorského redakčního průchodu;
2. `BLIND-02` — stejný výzkumný základ po závěrečné autorské redakci, která znovu vystaví prózu při zachování dat, tvrzení a citací.

Podrobný design je v [`EXPERIMENT-DESIGN.md`](EXPERIMENT-DESIGN.md). Závazný protokol posledního redakčního kroku je v [`AUTHORIAL-REVISION.md`](AUTHORIAL-REVISION.md).

## 2. Finální výzkumný design

Rukopis používá komparativní kvalitativní analýzu veřejných firemních dokumentů za rok 2024. Analyzované případy jsou:

- ČEZ Group;
- MONETA Money Bank;
- O2 Czech Republic;
- Škoda Auto.

Výzkum nehodnotí „skutečnou ESG kvalitu“ firem. Zkoumá, jak veřejné dokumenty dokládají přechod od deklarace k formalizovanému řízení a k vazbě na rozhodování.

Původní syntetický rozhovorový pilot zůstává v repozitáři pouze jako historický test workflow. Není součástí empirického korpusu ani výsledků finálního rukopisu.

## 3. Proces krok za krokem

### 3.1 Vymezení problému a zmrazení zadání

Výzkumný kontrakt, otázky, hranice tvrzení a volba dokumentového designu jsou zachyceny v:

- `notes/research-contract.md`;
- `notes/thesis-outline.md`;
- `notes/methodology.md`.

Zásadní změnou proti prvnímu návrhu bylo opuštění fingovaných rozhovorů a přechod k veřejně ověřitelnému dokumentovému korpusu.

### 3.2 Rešerše a registr zdrojů

Zdrojová vrstva je rozdělena na:

- `sources/academic-sources.csv` — odborná literatura;
- `sources/regulatory-sources.csv` — primární regulatorní akty a jejich status;
- `sources/corporate-documents.csv` — analyzované firemní dokumenty;
- `notes/literature-map.md` — role jednotlivých odborných zdrojů v argumentaci;
- `notes/esg-regulatory-czech-2026.md` — regulatorní kontext zmrazený k datu uzávěrky.

Metadata a DOI byly ověřeny, ale samotné bibliografické ověření není vydáváno za plnou druhou odbornou četbu všech zdrojů.

### 3.3 Konstrukce empirického korpusu

Z oficiálních firemních reportů byly vybrány významově ucelené segmenty s přesným lokátorem. Finální korpus je v `data/document-corpus.csv`.

Každý segment rozlišuje zejména:

- zdrojový dokument a stránku nebo oddíl;
- neutrální parafrázi;
- analytické kódy;
- evidenční třídu;
- způsob použití v argumentaci;
- hranici nebo omezení tvrzení.

Finální korpus obsahuje **45 klíčových segmentů**: ČEZ 11, MONETA 12, O2 11 a Škoda Auto 11.

### 3.4 Kódovací rámec a evidenční síla

Výchozí a finální slovníky jsou v:

- `analysis/document-codebook.csv`;
- `analysis/document-codebook-v2.csv`.

Škála E0–E4 se nepřiřazuje firmě jako celku, ale jednotlivému tvrzení nebo segmentu:

- **E0:** deklarace bez mechanismu;
- **E1:** konkrétní aktivita nebo výstup;
- **E2:** formalizovaný proces, vlastník, metodika nebo řízený výsledek;
- **E3:** doložená vazba na kapitál, riziko, produkt, dodavatele, odměnu nebo provozní rozhodování;
- **E4:** přesně vymezený konkrétní výsledek se silnou externí podporou nebo triangulací.

Finální rozdělení je **E0 = 1, E1 = 8, E2 = 27, E3 = 8, E4 = 1**.

Assurance je evidováno odděleně. Ověření reportu samo o sobě nezvyšuje automaticky každé tvrzení na E3 nebo E4.

### 3.5 Analytická kontrola

Kontrolní vrstva zahrnuje:

- `analysis/control-coding.csv` — stratifikovaný kontrolní vzorek přibližně 10 % korpusu;
- `analysis/coding-revisions.csv` — změny po kontrole;
- `analysis/high-evidence-review.csv` — druhá kontrola všech devíti položek E3/E4;
- `analysis/case-memos.md` — vnitropřípadové interpretace;
- `analysis/evidence-matrix.csv` — mezipřípadové srovnání.

Jedna položka byla po kontrole snížena z E3 na E2, protože omezené ujištění celé zprávy samo nedokládalo rozhodovací vazbu. Každé výsledkové téma musí obsahovat kontrast, proti-důkaz nebo jasně popsanou interpretační hranici.

### 3.6 Vazba tvrzení na důkaz

`audit/claim-evidence-ledger.csv` propojuje **31 hlavních tvrzení rukopisu** s konkrétními segmenty, zdroji a lokátory. Ledger slouží jako kontrola proti tomu, aby plynulý text překročil evidenční základ.

Obecný AI a zdrojový workflow je popsán v `notes/ai-workflow-and-audit.md`.

### 3.7 Psaní rukopisu

Zdrojové kapitoly baseline jsou uloženy v `chapters/` a jejich pořadí popisuje `thesis/README.md`:

1. front matter a abstrakty;
2. úvod;
3. teoretický rámec;
4. regulatorní kontext;
5. metodologie;
6. výsledky;
7. diskuse;
8. závěr;
9. seznam zdrojů.

Rukopis `BLIND-01` má v exportované verzi 70 stran A4. Firemní tvrzení, analytická interpretace, metrika, omezení a externí assurance jsou v metodice rozlišovány jako odlišné typy evidence.

### 3.8 Automatizovaná validace a sazba

Reprodukovatelný build zajišťují:

- `scripts/validate-manuscript.py`;
- `scripts/build_docx.py` a `scripts/build_docx_v2.py`;
- `scripts/build_evaluation_form.py` a `scripts/build_evaluation_form_v2.py`;
- `scripts/update_toc_export.py`;
- `scripts/build-manuscript.sh`;
- `.github/workflows/build-review-package.yml`.

Lokální sestavení baseline:

```bash
python scripts/validate-manuscript.py
bash scripts/build-manuscript.sh
```

Validace kontroluje strukturu CSV, počty segmentů, rozdělení E0–E4, pokrytí kontrol, vazby claim ledgeru a absenci syntetického pilotu ve finální empirické argumentaci. Build vytvoří DOCX a PDF, aktualizuje obsah a připraví oddělené předhodnoticí a odtajňovací archivy.

### 3.9 Vizuální a technická kontrola baseline

Finální DOCX `BLIND-01` byl vyrenderován po všech 70 stranách. Kontrolovala se sazba, tabulky, dělení nadpisů, seznam zdrojů, číslování a shoda PDF s kontrolním renderem. GitHub Actions současně ověřuje formát A4, přítomnost klíčových částí textu a vytvoření všech balíčků.

### 3.10 Autorská redakce (humanizer pass)

Tento krok byl přidán po předběžném zjištění, že obsahově kvalitní text baseline vykazuje výrazně homogenní styl a automatické detektory jej označují jako vysoce pravděpodobně generovaný.

Autorská redakce není synonymický spinner. Kapitoly se znovu vystavují po významových blocích. Před přepisem se zmrazí nosná tvrzení, citace, číselné údaje a metodické hranice. Po přepisu se každá kapitola znovu kontroluje proti zdrojům a claim-evidence ledgeru.

Povinné artefakty:

- `AUTHORIAL-REVISION.md` — úplný protokol;
- `prompts/authorial-revision.md` — reprodukovatelný redakční prompt;
- `analysis/style-benchmark.md` — diagnóza baseline;
- `audit/authorial-revision-log.csv` — evidence změn;
- `audit/detector-benchmark.csv` — výsledky fixních testů;
- `scripts/style-audit.py` — povrchová stylistická diagnostika;
- `variants/authorial-pass/chapters/` — zdrojové kapitoly `BLIND-02`.

Základní pravidla:

1. `BLIND-01` se nepřepisuje;
2. význam, data a zdroje mají přednost před stylistickým výsledkem;
3. nepřidávají se záměrné chyby, vata ani technické triky pro obcházení detektorů;
4. detektorové skóre je vedlejší údaj, ne důkaz autorství;
5. musí být zaznamenáno, zda konkrétní změnu provedl LLM, člověk, nebo kombinace obou;
6. `BLIND-02` dostane vlastní identifikátor, kontrolní součet a výstupní složku.

Před plošnou redakcí se používá pilotní úryvek teorie. Stejný úsek se testuje před a po přepisu. Teprve podle zdrojové kontroly, čitelnosti a vedlejšího benchmarku se styl aplikuje na celý rukopis.

### 3.11 Zaslepené hodnocení

Hodnotitel dostává pouze obsah složky konkrétní zmrazené varianty. U baseline jde o:

`deliverables/2026-09-01/01-send-to-reviewers/`

Pokyny jsou v `reviewer-packet/README.md` a hodnoticí formulář v `reviewer-packet/evaluation-form.md`.

Pořadí musí zůstat následující:

1. přečíst rukopis;
2. uzavřít věcný posudek, známku a doporučení k obhajobě;
3. uvést odhad způsobu vzniku a jistotu odhadu;
4. vrátit neměnnou kopii posudku;
5. teprve potom získat odtajňovací balíček.

Hodnotitel před uzavřením posudku nemá dostat přístup do repozitáře, historii commitů, auditní soubory ani názory ostatních hodnotitelů.

Pokud budou hodnoceny obě varianty, nesmí tentýž hodnotitel dostat druhou verzi bez samostatně zaznamenaného designu. Ideální je buď náhodné rozdělení hodnotitelů mezi `BLIND-01` a `BLIND-02`, nebo nejprve uzavřené hodnocení jedné verze a teprve poté výslovně označené komparativní čtení. Jinak by znalost první varianty zkreslila druhý posudek.

### 3.12 Odtajnění a vyhodnocení

Po uzavření všech posudků se zpřístupní příslušný odtajňovací balíček. U baseline je uložen v:

`deliverables/2026-09-01/02-after-review/`

Odtajňovací zpráva je v `reviewer-packet/reveal-note.md`. Původní známky a posudky se po odtajnění nepřepisují; případná změna názoru se zaznamenává jako samostatná následná reflexe.

U `BLIND-02` musí odtajnění navíc obsahovat redakční log, použitý prompt, informaci o lidském a strojovém podílu a srovnání s baseline. Samotné snížení detektorového skóre se neinterpretuje jako důkaz vyššího lidského podílu.

## 4. Připravené výstupy

### Baseline `BLIND-01`

- `deliverables/2026-09-01/01-send-to-reviewers/` — jediný obsah určený k prvnímu rozeslání;
- `deliverables/2026-09-01/02-after-review/` — auditní a odtajňovací balíček;
- `deliverables/2026-09-01/03-complete-build/` — úplný archiv verze a procesní dokumentace.

### Autorská varianta `BLIND-02`

- `variants/authorial-pass/` — pracovní struktura;
- cílová složka `deliverables/<datum-BLIND-02>/` vznikne až po dokončení redakce, zdrojové kontroly a nového buildu.

`STATUS.md` eviduje aktuální stav a známé hranice experimentu.

## 5. Hranice interpretace výsledku

Úspěšný posudek by prokázal, že předložený artefakt může při odborném čtení splnit požadavky hodnotitelů. Neprokazuje automaticky, že:

- konkrétní student látce rozumí;
- rukopis projde ústní obhajobou;
- každá citace byla nezávisle přečtena druhým odborníkem;
- firemní reporty přesně zachycují interní praxi;
- lze výsledek zobecnit na jiné obory, školy nebo typy výzkumu;
- nízké skóre AI detektoru potvrzuje lidské autorství;
- vysoké skóre AI detektoru potvrzuje strojové autorství.

Proto se odděleně eviduje kvalita rukopisu, konkrétní produkční varianta, odhad původu, detektorový benchmark, případná mock obhajoba a hodnocení po odtajnění.
