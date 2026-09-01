# Workflow využití AI a auditovatelnost výzkumu

**Účel:** nastavit dohledatelný proces pro literaturu, evidenci tvrzení, práci s verzemi a případné využití generativní AI. Workflow nenahrazuje pravidla FSE UJEP, pokyny vedoucího, informovaný souhlas ani úsudek výzkumníka. Před empirickou fází je nutné ověřit jejich aktuální znění.

## 1. Základní principy

1. **Člověk odpovídá za každé tvrzení.** AI může pomoci s návrhem, strukturou, převodem formátu nebo kontrolními otázkami; není zdrojem faktů ani autorem odpovědným za výzkumné rozhodnutí.
2. **Zdroj před textem.** Tvrzení se nepřebírá proto, že zní věrohodně. Musí vést k dohledanému zdroji, empirickému úryvku nebo transparentně označené interpretaci.
3. **Oddělené datové statusy.** Syntetická, pilotní, empirická a odvozená data mají oddělená umístění a viditelné štítky. Syntetická data se nikdy nesmějí promíchat s empirickým korpusem.
4. **Auditní stopa místo zpětné rekonstrukce.** Vstupy, verze, rozhodnutí a ověření se zapisují průběžně.
5. **Minimalizace dat.** Do externí AI služby se nevkládají osobní, důvěrné ani neanonymizované výzkumné údaje, pokud to výslovně nepovoluje souhlas, smlouva, školní pravidla a režim dané služby.
6. **Přiznání významného použití.** Způsob využití AI se popíše konkrétně podle aktuálních požadavků školy, nikoli vágní větou „AI byla použita“.

## 2. Zotero jako zdrojová vrstva

### 2.1 Struktura kolekcí

Doporučená kolekce `ESG-diplomka`:

- `00_Inbox` — nově zachycené záznamy bez kontroly;
- `01_Core-theory` — institucionální teorie, legitimita, CSR/ESG;
- `02_ESG-performance` — materialita, ratingy, výkonnost;
- `03_Regulation` — CSRD, ESRS a regulatorní změny;
- `04_Czech-context` — české podniky a národní kontext;
- `05_Methods` — tematická analýza, COREQ, vzorek;
- `90_Excluded` — vyřazené zdroje s důvodem;
- `99_Cited` — zdroje skutečně citované v aktuálním rukopisu.

Doporučené tagy: `status/inbox`, `status/metadata-checked`, `status/fulltext-read`, `status/cited`, `evidence/primary`, `evidence/review`, `evidence/regulation`, `method/qualitative`, `topic/E`, `topic/S`, `topic/G`.

### 2.2 Příjem a ověření záznamu

1. Importovat přes DOI, ISBN, knihovní katalog nebo oficiální stránku instituce; ruční import je poslední možnost.
2. Zkontrolovat název, autory, rok, časopis/vydavatele, svazek, číslo, strany, DOI a typ dokumentu proti stránce vydavatele nebo registru.
3. Přiložit legálně získaný plný text nebo stabilní URL a zaznamenat datum přístupu u proměnlivých webových zdrojů.
4. U regulatorního dokumentu uložit vydávající instituci, identifikátor, datum přijetí/účinnosti a přesnou verzi. Tisková zpráva není náhradou právního aktu.
5. Případnou opravu či stažení článku ověřit před citací.
6. Záznam přesunout z `00_Inbox` až po kontrole; automaticky stažená metadata se nepovažují za ověřená.

### 2.3 Poznámka ke zdroji

Každý klíčový zdroj má strukturovanou Zotero poznámku:

- bibliografický účel zdroje;
- výzkumná otázka a design;
- vzorek/kontext;
- hlavní výsledek ve vlastních slovech;
- omezení;
- přesné strany pro možné citace;
- tvrzení, která zdroj **nepodporuje**;
- vazby na položky evidence ledgeru.

Přímé citace musí mít stranu nebo jiný přesný lokátor. AI generované „citace“ a bibliografické záznamy se nepoužívají bez otevření originálu.

## 3. Evidence ledger: tvrzení na úrovni rukopisu

Evidence ledger propojuje konkrétní tvrzení s důkazem a verzí textu. Může být veden jako CSV nebo tabulka se stabilními ID.

### 3.1 Povinná pole

| Pole | Význam |
|---|---|
| `claim_id` | stabilní identifikátor, např. `CLM-0042` |
| `claim_text` | přesné pracovní znění tvrzení |
| `claim_type` | faktické / interpretační / metodické / právní / empirické |
| `scope` | populace, období a podmínky platnosti |
| `evidence_id` | Zotero key, DOI, právní identifikátor, dokument nebo anonymizovaný úryvek |
| `locator` | strana, oddíl, tabulka, řádky přepisu |
| `support_level` | přímá / nepřímá / rozporná / chybí |
| `verification` | kdo a jak otevřel a zkontroloval originál |
| `manuscript_location` | kapitola/oddíl/verze |
| `status` | navrženo / ověřeno / revidovat / odstranit |
| `notes` | omezení, alternativní výklad, konflikt zdrojů |

### 3.2 Pravidla práce

- Jedno složené tvrzení rozdělit, pokud jeho části vyžadují různé zdroje.
- Zdroj může být kvalitní, ale nemusí podporovat konkrétní rozsah tvrzení.
- Sekundární citaci označit a pokud možno dohledat originál.
- U právního tvrzení ověřit aktuálnost k datu rukopisu a rozlišit návrh, přijetí, účinnost a transpozici.
- Rozporující zdroje nezamlčet; zaznamenat je a zúžit tvrzení nebo vysvětlit rozdíl.
- Empirickou výpověď označit jako perspektivu respondenta, ne automaticky jako fakt o celé organizaci.
- Každá významná změna závěru musí zanechat poznámku, které evidenční položky ji vyvolaly.

## 4. Verze a reprodukovatelnost

### 4.1 Stavové úrovně artefaktů

- `draft` — pracovní text bez úplné kontroly;
- `reviewed` — obsah prošel lidskou kontrolou;
- `verified` — tvrzení jsou napojena na ledger a originály byly otevřeny;
- `frozen` — verze použitá pro konkrétní konzultaci, analýzu nebo odevzdání.

Stav se nesmí odvozovat jen z názvu souboru; má být zaznamenán v changelogu nebo metadatech projektu.

### 4.2 Doporučený verzovací postup

1. Malé logické změny ukládat odděleně s popisem důvodu, ne jen „úpravy“.
2. Před velkou transformací textu vytvořit označený checkpoint.
3. Neměnit surové přepisy; opravy ukládat jako novou normalizovanou vrstvu s protokolem změn.
4. Pro analytické exporty zaznamenat datum, výběrová kritéria, použité případy a kontrolní součet souboru.
5. Zachovat vazbu: surový zdroj → anonymizovaná verze → kódovaný úryvek → memo → téma → tvrzení rukopisu.
6. Před konzultací nebo odevzdáním vytvořit manifest artefaktů a verzí.

### 4.3 Minimální changelog rozhodnutí

Každý záznam obsahuje datum, autora rozhodnutí, dotčený artefakt, předchozí stav, nový stav, důvod, použité důkazy a případné AI použití. Nezapisují se přístupové údaje, neveřejné osobní údaje ani celý citlivý vstup.

## 5. Povolené a nepovolené využití AI

### 5.1 Přiměřená podpůrná použití

Podle pravidel školy a konkrétního nástroje může AI pomáhat například s:

- návrhem kontrolního seznamu nebo alternativní struktury;
- generováním otázek pro kritickou kontrolu argumentu;
- formátováním již ověřených metadat;
- návrhem kódu či regulárního výrazu pro datovou transformaci;
- jazykovou úpravou textu, jehož obsah výzkumník ověřil;
- syntetickými daty pro test procesu, pokud jsou výrazně a trvale označena jako **SYNTHETICKÁ / NE EMPIRICKÁ**;
- hledáním možných protiargumentů, které se následně ověří ve zdrojích.

### 5.2 Nepřijatelná použití

- vymýšlení zdrojů, DOI, citací, stran nebo výsledků;
- vydávání syntetických rozhovorů za provedený výzkum;
- automatické kódování skutečných rozhovorů bez metodického zdůvodnění, ochrany dat a lidské kontroly;
- nahrávání identifikovatelných přepisů do neautorizované externí služby;
- převzetí AI shrnutí místo čtení zdroje;
- zatajení použití, pokud mohlo podstatně ovlivnit text, analýzu nebo rozhodnutí;
- používání AI k vytvoření falešné auditní stopy;
- obcházení citačních, autorských, školních nebo technických kontrol.

## 6. Protokol jedné AI interakce

1. **Definovat účel:** co má interakce vyřešit a co naopak rozhodnout nesmí.
2. **Klasifikovat vstup:** veřejný / interní / důvěrný / osobní. Nepovolený vstup neposílat.
3. **Minimalizovat:** poskytnout jen data nutná pro úkol; citlivý obsah anonymizovat ještě před nástrojem.
4. **Zaznamenat:** vyplnit řádek v `audit/ai-use-log-template.csv` nebo pracovní kopii logu.
5. **Uložit bezpečný odkaz na prompt:** ne vkládat tajné údaje ani celý citlivý obsah do logu; použít interní referenci.
6. **Ověřit výstup:** otevřít originální zdroje, přepočítat hodnoty, spustit kód/test nebo porovnat s přepisem podle typu úkolu.
7. **Rozhodnout lidsky:** přijmout, upravit nebo odmítnout; důvod zaznamenat.
8. **Promítnout do ledgeru a verze:** pokud výstup ovlivnil tvrzení, uvést evidenci i verzi artefaktu.
9. **Posoudit přiznání:** označit, zda se použití musí objevit v metodice, poděkování, příloze nebo jiném školou stanoveném místě.

## 7. Datový slovník auditního CSV

Soubor `audit/ai-use-log-template.csv` obsahuje pouze hlavičku určenou ke zkopírování do provozního logu.

| Sloupec | Obsah |
|---|---|
| `event_id` | stabilní ID, např. `AI-2026-0001` |
| `timestamp_iso` | datum a čas v ISO 8601 včetně časové zóny |
| `researcher` | osoba odpovědná za interakci |
| `stage` | literatura / design / sběr / analýza / psaní / kontrola / technické |
| `artifact_path` | dotčený soubor nebo artefakt |
| `artifact_version` | verze před nebo po změně podle poznámky |
| `ai_system` | název služby nebo lokálního nástroje |
| `model_version` | známé označení modelu; `unknown`, pokud jej rozhraní nesděluje |
| `interface` | web / API / editor / lokální |
| `purpose` | úzký účel interakce |
| `input_classification` | public / internal / confidential / personal; citlivé vstupy musí odpovídat schválenému režimu |
| `prompt_ref` | bezpečný interní odkaz na prompt nebo jeho necitlivý archiv |
| `input_summary` | věcný popis vstupu bez osobních údajů a tajemství |
| `output_summary` | popis výstupu, nikoli nekritické potvrzení správnosti |
| `human_decision` | accepted / modified / rejected |
| `verification_method` | konkrétní lidská kontrola |
| `evidence_refs` | claim IDs, Zotero keys, DOI, testy nebo lokátory |
| `changes_made` | co člověk změnil před použitím |
| `risk_flags` | halucinace / bias / privacy / copyright / legal / none / jiné |
| `personal_data_included` | yes / no; `yes` vyžaduje zdokumentovaný oprávněný režim mimo tento log |
| `disclosure_required` | yes / no / review |
| `reviewer` | druhá kontrolující osoba, pokud je požadována |
| `review_date` | datum kontroly |
| `status` | open / verified / rejected / superseded |
| `notes` | omezení a návazná rozhodnutí |

## 8. AI detektory

**Výstup AI detektoru není důkazem autorství, podvodu ani nepovoleného použití.** Tyto nástroje mají nejistou chybovost, mohou znevýhodňovat některé styly a jazyky a neposkytují spolehlivou rekonstrukci vzniku textu.

Z toho plynou dvě pravidla:

1. Detektor nesmí být použit jako jediný ani rozhodující podklad pro obvinění nebo metodický závěr. Případnou pochybnost je nutné posuzovat z auditní stopy, verzí, zdrojových poznámek, znalosti práce a rozhovoru s autorem.
2. **Detektor se nesmí obcházet.** Není přípustné text parafrázovat, „humanizovat“, záměrně zanášet chyby nebo používat jiné nástroje s cílem snížit detekční skóre. Správnou reakcí je transparentní proces, ověřený obsah a pravdivé přiznání použití AI.

Skóre detektoru se standardně do výzkumného auditu nezapisuje jako validace originality. Pokud je jeho použití institucí vynuceno, zapíše se název/verze, datum, nastavení, úplný kontext a zásadní omezení interpretace.

## 9. Kontrolní brány

### Před zařazením zdroje

- metadata ověřena proti originálu;
- plný text nebo oficiální dokument otevřen;
- poznámka obsahuje omezení a lokátory;
- žádná AI generovaná reference nezůstala bez kontroly.

### Před použitím empirického úryvku

- souhlas a režim zpracování jsou v pořádku;
- úryvek je anonymizován;
- vazba na původní přepis je interně dohledatelná;
- interpretace je odlišena od slov respondenta;
- syntetický materiál není součástí korpusu.

### Před uzavřením kapitoly

- významná tvrzení mají `claim_id` a podporu;
- právní a časově proměnlivé informace jsou znovu ověřeny;
- rozpory a omezení nejsou skryty;
- AI log odpovídá skutečnému procesu;
- změny od poslední ověřené verze jsou zkontrolovány.

### Před odevzdáním

- manifest souborů a verzí je uzavřen;
- citace v textu odpovídají Zotero knihovně;
- náhodný vzorek tvrzení je zpětně dohledán k originálu;
- přiznání AI odpovídá školním pravidlům a skutečnému použití;
- nejsou přítomny syntetické pasáže vydávané za empirické;
- audit neobsahuje osobní údaje, přístupové údaje ani důvěrné celé prompty.

## 10. Doporučené rozdělení odpovědnosti

- **Výzkumník:** formulace otázek, souhlas, sběr, interpretace, ověření a finální text.
- **Vedoucí práce:** metodické a institucionální rozhodnutí, přiměřenost rozsahu, pravidla přiznání.
- **Druhý kontrolor:** namátkové ověření evidence ledgeru, kritických právních tvrzení a vybraných analytických vazeb.
- **AI nástroj:** podpůrná transformace nebo generování variant v přesně vymezeném rozsahu; nikdy konečné rozhodnutí.

Dobrá auditovatelnost nespočívá v ukládání všeho bez rozlišení. Spočívá v tom, že lze u významného tvrzení nebo rozhodnutí rekonstruovat jeho původ, verzi, lidské ověření a roli AI — bez porušení soukromí respondentů.
