# Proces experimentu a mapa repozitáře

**Kanonický rukopis:** `ESG-DP-2026-REVIEW`  
**Stav procesu:** obsah, autorská redakce a reprodukovatelný build dokončeny; následuje nezávislé hodnocení

Tento soubor popisuje celý postup od formulace výzkumného problému přes práci se zdroji, analýzu a závěrečnou redakci až po zaslepené hodnocení a následné odtajnění. Hodnotitelům se neposílá přístup do repozitáře, ale pouze hotový balíček z `deliverables/final/01-send-to-reviewers/`.

## 1. Co experiment testuje

Experiment zjišťuje, zda workflow založené převážně na současném velkém jazykovém modelu dokáže vytvořit úplný, zdrojově dohledatelný a odborně hodnotitelný rukopis na úrovni diplomové práce.

Nejde o skutečné odevzdání kvalifikační práce, získání akademického titulu ani vydávání syntetických dat za empirii. Výstup je výzkumný artefakt určený k nezávislému posouzení.

Primárním výsledkem je známka a doporučení či nedoporučení k obhajobě, které hodnotitel uzavře před odtajněním produkčního procesu. Sekundárně se sledují věcné chyby, metodologické námitky, otázky k obhajobě, odhad způsobu vzniku textu a případná změna názoru po odtajnění.

Podrobný hodnoticí design je v [`EXPERIMENT-DESIGN.md`](EXPERIMENT-DESIGN.md).

## 2. Výzkumný design rukopisu

Rukopis používá komparativní kvalitativní analýzu veřejných firemních dokumentů za rok 2024. Analyzované případy jsou ČEZ Group, MONETA Money Bank, O2 Czech Republic a Škoda Auto.

Výzkum nehodnotí absolutní „ESG kvalitu“ firem. Zkoumá, jak veřejné dokumenty dokládají přechod od deklarace k formalizovanému řízení a k vazbě na rozhodování.

Původní rozhovorový návrh byl během vývoje opuštěn. Historický syntetický pilot zůstal fyzicky i významově oddělený a není součástí empirického korpusu, výsledků ani závěrů hodnoceného rukopisu.

## 3. Proces krok za krokem

### 3.1 Vymezení problému a zmrazení zadání

Výzkumný kontrakt, hlavní a dílčí otázky, hranice tvrzení a volba dokumentového designu jsou zachyceny v `notes/research-contract.md`, `notes/thesis-outline.md` a `notes/methodology.md`.

Zásadním rozhodnutím bylo nahradit plánovaný rozhovorový výzkum veřejně ověřitelným dokumentovým korpusem. Tím se odstranila potřeba vytvářet nebo simulovat empirická data a celý analytický základ se stal znovu dohledatelným.

### 3.2 Rešerše a registry zdrojů

Zdrojová vrstva je rozdělena na:

- `sources/academic-sources.csv` — odbornou literaturu;
- `sources/regulatory-sources.csv` — primární regulatorní akty a jejich status;
- `sources/corporate-documents.csv` — analyzované firemní dokumenty;
- `notes/literature-map.md` — roli jednotlivých odborných zdrojů v argumentaci;
- `notes/esg-regulatory-czech-2026.md` — regulatorní kontext zmrazený k datu uzávěrky.

U odborných zdrojů byla kontrolována metadata a DOI. Tato kontrola se nevydává za nezávislou druhou odbornou četbu všech článků v plném textu; uvedené omezení zůstává součástí odtajnění.

### 3.3 Konstrukce empirického korpusu

Z oficiálních firemních reportů byly vybrány významově ucelené segmenty s přesným lokátorem. Korpus je uložen v `data/document-corpus.csv`.

U každého segmentu je zaznamenán zdrojový dokument a stránka nebo oddíl, neutrální parafráze, tematické kódy, evidenční třída, způsob využití v argumentaci a hranice nebo alternativní výklad.

Korpus obsahuje **45 klíčových segmentů**: ČEZ 11, MONETA 12, O2 11 a Škoda Auto 11. Nejde o úplný katalog všech zveřejnění, ale o záměrně zúžený soubor důkazních jednotek použitých v hlavní analýze.

### 3.4 Kódovací rámec a evidenční síla

Výchozí a finální slovníky jsou v `analysis/document-codebook.csv` a `analysis/document-codebook-v2.csv`.

Škála E0–E4 se přiřazuje jednotlivému tvrzení nebo segmentu, nikoli firmě jako celku:

- **E0:** deklarace bez konkrétního mechanismu;
- **E1:** aktivita nebo výstup;
- **E2:** formalizovaný proces, vlastník, metodika nebo řízený výsledek;
- **E3:** zveřejněná vazba na kapitál, riziko, produkt, dodavatele, odměnu nebo provozní rozhodování;
- **E4:** přesně vymezený výsledek se silnou externí podporou nebo triangulací.

Finální rozdělení je **E0 = 1, E1 = 8, E2 = 27, E3 = 8 a E4 = 1**. Assurance je evidováno samostatně, protože externí ověření zprávy samo nepředstavuje důkaz manažerské integrace ani skutečného dopadu.

### 3.5 Analytická kontrola

Kontrolní vrstva zahrnuje:

- `analysis/control-coding.csv` — stratifikovaný kontrolní vzorek přibližně deseti procent korpusu;
- `analysis/coding-revisions.csv` — změny po kontrole;
- `analysis/high-evidence-review.csv` — druhou kontrolu všech devíti položek E3/E4;
- `analysis/case-memos.md` — vnitropřípadové interpretace;
- `analysis/evidence-matrix.csv` — mezipřípadové srovnání.

Jedna položka byla po kontrole snížena z E3 na E2, protože omezené ujištění celé zprávy samo o sobě nedokládalo rozhodovací vazbu. Každé výsledkové téma musí obsahovat kontrast, proti-důkaz nebo jasně popsanou interpretační hranici.

### 3.6 Vazba tvrzení na důkaz

`audit/claim-evidence-ledger.csv` propojuje **31 hlavních tvrzení rukopisu** s konkrétními segmenty, zdroji a lokátory. Ledger brání tomu, aby plynulý text překročil evidenční základ nebo zaměnil firemní tvrzení za nezávisle ověřený fakt.

Obecný zdrojový a produkční workflow je popsán v `notes/ai-workflow-and-audit.md`.

### 3.7 První sestavení rukopisu

Zdrojové kapitoly jsou uloženy v `chapters/` a jejich pořadí popisuje `thesis/README.md`. První úplné sestavení sloužilo k ověření logické návaznosti, úplnosti argumentace, práce s tabulkami a technického exportu.

Následná kontrola ukázala, že věcně soudržný text je stylisticky příliš rovnoměrný a řada podkapitol používá obdobný rytmus i argumentační šablonu. Do procesu byl proto přidán samostatný závěrečný redakční krok.

### 3.8 Závěrečná autorská redakce

Všechny narativní kapitoly byly znovu vystavěny po významových blocích. Nešlo o synonymické nahrazování slov ani o mechanickou úpravu jednotlivých vět. Před přepisem byly uzamčeny hlavní tvrzení, citace, číselné údaje, lokátory, výzkumné otázky, metodické hranice a význam škály E0–E4 i assurance.

Redakce měla odstranit opakující se šablony, zviditelnit autorská rozhodnutí, přirozeněji střídat délku vět a odstavců a vysvětlovat přechody podle významu. Zakázány byly záměrné jazykové chyby, nahodilé prodlužování, překladové obcházení, neviditelné znaky a jiné technické zásahy do textu.

Po redakci byly kapitoly znovu kontrolovány proti zdrojům, datovým tabulkám a claim-evidence ledgeru. Výsledkem je jediný kanonický rukopis `ESG-DP-2026-REVIEW`; pracovní meziverze nejsou součástí aktuální struktury repozitáře ani hodnoticího balíčku.

### 3.9 Automatizovaná validace a sazba

Reprodukovatelný build zajišťují `scripts/validate-manuscript.py`, oba DOCX build skripty, oba skripty formuláře, `scripts/update_toc_export.py`, `scripts/build-manuscript.sh` a `.github/workflows/build-review-package.yml`.

Lokální sestavení:

```bash
python scripts/validate-manuscript.py
bash scripts/build-manuscript.sh
```

Validace kontroluje strukturu CSV, počty segmentů, rozdělení E0–E4, pokrytí kontrol, vazby claim ledgeru a nepřítomnost historického syntetického pilotu ve finální empirické argumentaci. Build vytvoří DOCX a PDF, aktualizuje obsah a připraví oddělený hodnoticí a odtajňovací balíček.

### 3.10 Vizuální a technická kontrola

Po sestavení se kontroluje formát A4, titulní strana a obsah, návaznost nadpisů a číslování, zalomení tabulek, čitelnost seznamu zdrojů, shoda identifikátoru napříč dokumenty a absence pracovních označení nebo produkčních poznámek v hodnoticí verzi. Kontrolní součty jsou součástí každého balíčku.

### 3.11 Zaslepené hodnocení

Hodnotitel obdrží pouze obsah `deliverables/final/01-send-to-reviewers/`. Pokyny jsou v `reviewer-packet/README.md` a formulář v `reviewer-packet/evaluation-form.md`.

Doporučené pořadí je:

1. přečíst rukopis;
2. uzavřít věcný posudek, známku a doporučení k obhajobě;
3. teprve poté uvést odhad způsobu vzniku a jistotu odhadu;
4. vrátit neměnnou kopii posudku;
5. až následně získat odtajňovací balíček.

Před uzavřením posudku nemá hodnotitel dostat přístup do repozitáře, historii commitů, auditní soubory, produkční poznámky ani názory ostatních hodnotitelů.

### 3.12 Odtajnění a vyhodnocení

Po uzavření všech posudků se zpřístupní `deliverables/final/02-after-review/`. Odtajňovací zpráva popisuje skutečný produkční proces, lidské a modelové role, zdrojovou kontrolu i známá omezení. Původní známka a posudek se po odtajnění nepřepisují; případná změna názoru se zaznamenává zvlášť.

Výsledky se vyhodnotí na úrovni jednotlivých hodnotitelů i souhrnně. Minimálně se eviduje známka, doporučení k obhajobě, hlavní silné a slabé stránky, nejzávažnější chyba, otázky k obhajobě, odhad způsobu vzniku a reflexe po odtajnění.

## 4. Připravené výstupy

- `deliverables/final/01-send-to-reviewers/` — jediný obsah určený k prvnímu rozeslání;
- `deliverables/final/02-after-review/` — odtajňovací a auditní balíček;
- `deliverables/final/03-source-and-audit/` — úplný interní archiv sestavení;
- `STATUS.md` — aktuální stav a známé hranice experimentu.

## 5. Hranice interpretace výsledku

Pozitivní posudek by prokázal, že předložený artefakt může při odborném čtení splnit požadavky hodnotitelů. Neprokazuje automaticky, že konkrétní student látce rozumí, že rukopis projde ústní obhajobou, že všechny zdrojové interpretace jsou bezchybné, že firemní reporty přesně zachycují interní praxi ani že pravidla konkrétní školy dovolují studentovi stejný způsob použití generativních nástrojů.

Experiment proto odděluje kvalitu výsledného dokumentu, odhad jeho původu, případnou mock obhajobu a hodnocení po odtajnění.