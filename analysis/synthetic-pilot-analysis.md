# Analýza syntetického pilotu

> **ZÁSADNÍ OMEZENÍ: SYNTHETICKÁ / NE EMPIRICKÁ ANALÝZA.**
> Analýza pracuje výhradně s uměle vytvořenými rozhovory S01–S06 v `data/synthetic-pilot-interviews.md`. Témata, kódy, matice, „citace“ i závěry jsou demonstrací analytického procesu, nikoli poznatky o českých podnicích. Nelze je uvádět ve výsledkové části jako empirii ani je použít k zobecnění.

## 1. Analytický záměr

Cílem pilotní analýzy je ověřit:

1. zda navržený scénář vytváří materiál relevantní k hlavní a dílčím výzkumným otázkám;
2. zda lze rozlišit označení ESG, jednotlivé praxe, formalizované řízení a externí reporting;
3. zda je analytická cesta od úryvku přes kód k tématu transparentní;
4. kde hrozí předčasné potvrzování pracovních očekávání;
5. jaké doplňující sondy a evidenční pravidla budou potřeba pro skutečná data.

Metodickým rámcem je reflexivní tematická analýza. Počty kódů se používají jen jako navigační pomůcka, nikoli jako statistický důkaz významnosti tématu.

## 2. Analytický proces krok za krokem

### Krok A — seznámení s materiálem

Každý syntetický profil byl přečten jako celek. První memo zachytilo tři opakující se napětí:

- označení ESG versus fakticky prováděné praxe;
- externí požadavek versus interní provozní důvod;
- množství reportovaných dat versus jejich využití v rozhodování.

Současně byly označeny kontrasty: S03 má silnou formalizaci, S04 personálně křehkou koordinaci, zatímco S05 silné provozní vlastnictví bez ESG rámce.

### Krok B — první cyklus kódování

Kódování bylo sémantické i latentní. První sada kódů kombinovala otázkami předpokládané oblasti a otevřené kódy vzniklé při čtení.

| Kód | Pracovní definice | Zahrnout | Nezahrnout |
|---|---|---|---|
| `label-practice-gap` | Praxe existuje, ale organizace ji nenazývá ESG, nebo nálepka neodpovídá řízení | explicitní distanc od označení při popisu praxe | pouhá absence slova ESG bez popisu praxe |
| `external-trigger` | Prvotní impuls přichází od regulátora, zákazníka, banky či skupiny | audit, tendr, reportovací požadavek | obecná společenská očekávání bez konkrétního aktéra |
| `operational-anchor` | Agenda přetrvává díky úsporám, riziku, bezpečnosti či provoznímu výkonu | měřená energie, zmetkovitost, rizikové rozhodnutí | pouze očekávaný reputační přínos |
| `fragmented-ownership` | Odpovědnost je rozdělena bez funkční koordinace nebo jasného vlastníka | mezery mezi financemi, HR, provozem | rozdělení rolí s jasným výborem a eskalací |
| `person-dependency` | Proces stojí na jedné osobě a nemá zastupitelnost | agenda se zastaví při absenci | běžný určený vlastník s dokumentací |
| `data-friction` | Problém dostupnosti, definice, srovnatelnosti nebo původu dat | opakovaný sběr, odhady, chybějící Scope 3 | nesouhlas s cílem ESG bez datové dimenze |
| `reporting-decision-gap` | Data jsou sbírána pro výkaz, ale jejich vazba na rozhodnutí je slabá | detail pouze pro report | ukazatel použitý v investičním či rizikovém rozhodnutí |
| `benefit-evidence-tier` | Respondent rozlišuje doložený, nepřímý a očekávaný přínos | před/po, korelace, osobní odhad | obecné pozitivní tvrzení bez možnosti zařazení |
| `deadline-not-pressure` | Regulatorní změna posune harmonogram, ale jiné tlaky pokračují | pokračující zákaznické/skupinové požadavky | úplné ukončení agendy |
| `translation-work` | Aktéři převádějí abstraktní ESG do provozního jazyka | „méně zmetků“, energie, riziko | prosté zjednodušení formuláře |

### Krok C — ukázka kódování na úrovni úryvku

V tabulce jsou syntetické úryvky z pilotního souboru. Uvozovky zde neoznačují skutečné výroky.

| Případ | Syntetický úryvek | První kódy | Analytická poznámka |
|---|---|---|---|
| S01 | „Rozpočet prošel až tehdy, když se ukázala návratnost energie.“ | `external-trigger`, `operational-anchor`, `translation-work` | Externí impuls sám nestačí; legitimita investice vzniká provozním překladem. |
| S02 | „Máme pravidla … ale nikdy jsme tomu nedali jednu nálepku.“ | `label-practice-gap` | Absence ESG značky není absencí E/S/G praxe. |
| S03 | „Formalizace zvýšila kontrolu, ale také počet lidí, kteří kontrolují stejnou hodnotu.“ | `data-friction`, `reporting-decision-gap` | Governance může současně zvýšit dohledatelnost i transakční náklady. |
| S04 | „Když mám dovolenou, ESG … stojí.“ | `person-dependency`, `fragmented-ownership` | Formální existence agendy nezaručuje organizační zakotvení. |
| S05 | „Méně zmetků, méně plynu a bezpečnější hala…“ | `translation-work`, `operational-anchor`, `label-practice-gap` | Provozní jazyk podporuje přijetí, ale může skrýt chybějící systémový přehled. |
| S06 | „Dostaneme čtyřicet nejistých odpovědí.“ | `data-friction`, `reporting-decision-gap` | Větší rozsah sběru nemusí znamenat kvalitnější důkaz pro rozhodnutí. |

### Krok D — druhý cyklus a revize kódů

Po porovnání případů byly provedeny tyto změny:

1. Původní kód „regulatorní tlak“ byl rozdělen na `external-trigger` a `deadline-not-pressure`, protože impuls a přetrvávání agendy jsou odlišné procesy.
2. „Přínosy ESG“ byl nahrazen kódem `benefit-evidence-tier`, aby analýza nerozpoznávala jako rovnocenné měřený výsledek, korelaci a očekávání.
3. `fragmented-ownership` byl oddělen od `person-dependency`: distribuovaná odpovědnost může fungovat, závislost na jedné osobě je jiný mechanismus křehkosti.
4. Byl přidán `translation-work`, protože přijetí agendy se v syntetických případech mění podle jazyka, kterým je představena.

### Krok E — konstrukce kandidátních témat

Kódy nebyly mechanicky seskupeny podle otázek scénáře. Kandidátní témata byla formulována jako tvrzení o vztazích mezi kódy:

- externí tlak spouští sběr, ale provozní zakotvení rozhoduje o pokračování;
- organizace může mít ESG systém bez silné praxe nebo silnou praxi bez ESG identity;
- kvalita governance spočívá spíše ve vlastnictví a rozhodovací vazbě než v množství ukazatelů;
- regulatorní změna mění tempo a rozsah, nikoli všechny zdroje tlaku;
- tvrzení o přínosech mají různé stupně evidenční síly.

### Krok F — kontrola proti případům a záporným příkladům

Každé kandidátní téma bylo porovnáno se všemi šesti syntetickými případy. Hledaly se rozpory, nikoli jen podporující úryvky. Výsledná témata níže proto obsahují hranice a negativní případy.

## 3. Případová kódová matice

`●` = kód je v syntetickém případu výrazný; `○` = přítomný okrajově; `—` = v konstruovaném materiálu nezachycen.

| Kód / případ | S01 | S02 | S03 | S04 | S05 | S06 |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| `label-practice-gap` | ○ | ● | — | ○ | ● | — |
| `external-trigger` | ● | ○ | ● | ● | ○ | ● |
| `operational-anchor` | ● | ○ | ● | ○ | ● | ● |
| `fragmented-ownership` | ● | ○ | — | ● | ○ | ○ |
| `person-dependency` | — | — | — | ● | — | — |
| `data-friction` | ● | ○ | ● | ● | ○ | ● |
| `reporting-decision-gap` | ○ | ○ | ● | ● | ○ | ● |
| `benefit-evidence-tier` | ● | ● | ● | ● | ● | ● |
| `deadline-not-pressure` | ● | ○ | ● | ● | ○ | ● |
| `translation-work` | ● | ● | ○ | ○ | ● | ○ |

Tato matice je kontrolní pomůcka. Vzhledem k tomu, že případy byly záměrně konstruovány, nesmí být četnost interpretována jako prevalence ve skutečné populaci.

## 4. Výsledná pilotní témata

### Téma 1 — Externí impuls potřebuje provozní kotvu

**Centrální myšlenka:** Regulace, zákazník nebo skupina mohou zahájit sběr dat, ale pokračování aktivity je v syntetickém materiálu spojeno s překladem do úspor, rizika, bezpečnosti, retence nebo obchodní podmínky.

**Stavební kódy:** `external-trigger`, `operational-anchor`, `translation-work`, `deadline-not-pressure`.

**Rozsah:** Téma se týká mechanismu udržení agendy, ne tvrzení, že všechny provozně ukotvené praktiky jsou efektivní nebo udržitelné.

**Negativní případ:** S03 ponechává část agendy i kvůli skupinovému minimu, tedy bez nutnosti lokálně prokázané návratnosti. Externí vlastnictví proto může samo tvořit stabilní kotvu.

### Téma 2 — Nálepka, praxe, systém a report jsou čtyři odlišné vrstvy

**Centrální myšlenka:** S02 a S05 demonstrují praxe bez ESG identity; S03 demonstruje plně formalizovaný systém; S04 ukazuje, že politika a výpočet samy o sobě nezaručují průběžné řízení.

**Stavební kódy:** `label-practice-gap`, `reporting-decision-gap`, `fragmented-ownership`.

**Rozsah:** Téma nehodnotí, která vrstva je morálně či ekonomicky „lepší“. Slouží k zabránění kategorické chybě při interpretaci.

**Negativní případ:** U S03 jsou reporting a rozhodování částečně propojené. Reportovací formalizace tedy nemusí být pouze administrativní fasádou.

### Téma 3 — Governance se pozná podle odpovědnosti a použití dat, ne podle jejich objemu

**Centrální myšlenka:** Rozdělení rolí může být funkční, pokud existuje sponzor, vlastník dat a eskalace. Bez nich vzniká křehkost, duplicita nebo závislost na jednotlivci. Více položek nemusí zvyšovat rozhodovací kvalitu.

**Stavební kódy:** `fragmented-ownership`, `person-dependency`, `data-friction`, `reporting-decision-gap`.

**Rozsah:** Nejde o odmítnutí standardizace; tématem je vazba mezi sběrem, kontrolou a rozhodnutím.

**Negativní případ:** S05 funguje provozně bez centrální koordinace. Centralizace proto není nutnou podmínkou každého dílčího výsledku, může však být potřebná pro souhrnnou auditovatelnost.

### Téma 4 — Regulatorní změna přeuspořádává tempo, ne celé pole tlaků

**Centrální myšlenka:** V konstruovaných případech se odkládá software, poradenství nebo detail výkazu, zatímco pokračují požadavky odběratelů, skupiny, rizikového řízení a provozních úspor.

**Stavební kódy:** `deadline-not-pressure`, `external-trigger`, `operational-anchor`.

**Rozsah:** Jde o otázku pro empirické ověření, nikoli o závěr o účinku konkrétní právní změny.

**Negativní případ:** U S02 a S05 je přímý regulatorní vliv velmi slabý. Změna harmonogramu proto nemusí být pro část podniků relevantní vůbec.

### Téma 5 — „Přínos“ je potřeba rozdělit podle síly důkazu

**Centrální myšlenka:** Syntetické odpovědi zahrnují měření před/po, splnění obchodní podmínky, korelaci, procesní zkušenost i očekávání. Jejich sloučení by nadhodnotilo evidenci.

**Stavební kódy:** `benefit-evidence-tier`, `operational-anchor`, `reporting-decision-gap`.

**Navržená evidenční škála:**
A — přímo měřený výsledek s popsanou srovnávací základnou;
B — doložený procesní nebo obchodní výsledek bez kauzální atribuce;
C — nepřímá indicie či korelace;
D — očekávání, odhad nebo osobní interpretace.

**Negativní případ:** Ani úroveň A automaticky neprokazuje, že změnu způsobilo právě ESG opatření. Pro kauzální tvrzení by byl nutný odpovídající design.

## 5. Vazba na výzkumné otázky

> **NÁSLEDUJÍCÍ ODPOVĚDI JSOU POUZE TESTEM ANALYTICKÉHO RÁMCE NA SYNTHETICKÝCH DATECH.**

| Výzkumná oblast | Co pilot umožňuje analyzovat | Co z pilotu nelze tvrdit |
|---|---|---|
| Konkrétní praxe a rozhodování | rozdíl mezi jednotlivým opatřením, systémem a reportem | rozšířenost praktik v českých podnicích |
| Motivy | kombinace regulace, trhu, skupiny, nákladů a hodnot | pořadí či relativní sílu motivů v populaci |
| Bariéry | kapacitu, jazyk, data, duplicity a nejasné vlastnictví | skutečnou četnost nebo finanční velikost bariér |
| Přínosy | různé stupně doložení a nutnost sondovat metodu měření | kauzální dopad ESG na výkon |
| Přímý versus nepřímý tlak | typologii možných mechanismů | reprezentativní rozdíly mezi skupinami firem |
| Změna 2025–2026 | otázku tempa versus přetrvávajícího tlaku | reálný účinek konkrétní legislativy bez empirických a právních zdrojů |

## 6. Reflexivní memo a rizika zkreslení

Pracovní kontrakt už předpokládá, že provozně ukotvená opatření budou trvalejší a že regulatorní zjednodušení neodstraní tržní tlak. Syntetické profily byly vytvořeny se znalostí těchto očekávání, takže jejich následné „potvrzení“ je kruhové. Pilot proto nelze použít jako podporu očekávání; může pouze odhalit, jak snadno by analytik hledal potvrzující materiál.

Při skutečné analýze budou nutné tyto brzdy:

- před kódováním zaznamenat očekávání analytika a jejich možné zdroje;
- aktivně vyhledávat případy, kde čistě regulatorní projekt přetrval nebo provozně výhodné opatření zaniklo;
- oddělit výpověď respondenta od dokumentárního důkazu a od interpretace výzkumníka;
- uchovat změny kódů a důvody jejich sloučení či rozdělení;
- neprezentovat četnost zmínek jako důležitost nebo prevalenci;
- vracet se k celému případu, aby vytržené citace nepřebily kontext.

## 7. Úpravy před skutečným pilotem

1. Doplnit sondy na poslední konkrétní rozhodnutí, vlastníka rozpočtu a původ ukazatele.
2. U každého tvrzeného přínosu zjistit výchozí stav, období, metriku a alternativní vysvětlení.
3. Ptát se na selhání, zastavené projekty a opatření bez očekávaného přínosu.
4. Oddělit osobní názor respondenta od oficiální pozice a dostupného dokumentu.
5. Zachytit velikost, vlastnictví, sektor, pozici v hodnotovém řetězci a typ regulatorní expozice bez oslabení anonymity.
6. Po prvních dvou skutečných rozhovorech revidovat scénář; syntetické kódy nepřenášet automaticky jako definitivní codebook.
7. Empirické přepisy uložit mimo syntetický korpus a při exportu vždy uvést datový status.

## 8. Auditní stopa této demonstrace

| Fáze | Vstup | Operace | Výstup | Status |
|---|---|---|---|---|
| Konstrukce pilotu | výzkumný kontrakt | vytvoření kontrastních hypotetických profilů | `data/synthetic-pilot-interviews.md` | syntetické, ne empirické |
| Seznámení | S01–S06 | memo o napětích a kontrastech | oddíl 2A | analytická demonstrace |
| Kódování 1 | syntetické úryvky | otevřené a otázkami citlivé kódování | codebook v oddílu 2B | analytická demonstrace |
| Revize | první kódy a případy | rozdělení, zpřesnění a kontrola hranic | oddíl 2D | analytická demonstrace |
| Témata | kódy a případová matice | hledání vztahů a negativních případů | oddíl 4 | analytická demonstrace |
| Reflexe | témata + pracovní očekávání | kontrola kruhovosti a potvrzovacího zkreslení | oddíl 6 | metodická kontrola |

**Výsledek pilotu:** Scénář a analytický rámec jsou použitelné pro skutečný pilot po uvedených úpravách. Toto je rozhodnutí o procesu, nikoli empirický výsledek o ESG.
