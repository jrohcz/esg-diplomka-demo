# Metodologie — komparativní kvalitativní analýza firemních ESG reportů

**Verze:** 2026-09-01  
**Navazuje na:** `notes/research-contract.md`  
**Metodický status:** uzavřený protokol před hlavním kódováním

## 1. Výzkumný design

Práce používá kvalitativní, průřezový a komparativní design založený na analýze veřejných firemních dokumentů. Dokumentová analýza je systematický postup, při němž jsou dokumenty vyhledány, posouzeny, segmentovány, kódovány a interpretovány s ohledem na podmínky jejich vzniku (Bowen, 2009). Nejde tedy o „čtení reportů a shrnutí zajímavostí“, ale o transparentní výzkumný proces s předem stanovenými jednotkami analýzy, kódovacím rámcem a evidenční stopou.

Jádrem je **řízená kvalitativní obsahová analýza** (directed qualitative content analysis). Počáteční kategorie vycházejí z teoretického rámce a výzkumných otázek: institucionální tlaky, legitimita, materialita, organizační odpovědnost, manažerská integrace, metriky, zveřejňování negativních dopadů a externí ověření. Řízený přístup je vhodný, když existující teorie poskytuje výchozí pojmy, ale analýza musí umožnit jejich upřesnění či doplnění kategoriemi vzniklými z dat (Hsieh & Shannon, 2005). Kódovací rámec proto není uzavřeným checklistem. Při pilotu i hlavním kódování lze přidat induktivní kód, pokud zachycuje významný jev, který stávající rámec nezahrnuje.

Design neslouží k měření „ESG výkonnosti“ firem ani k sestavení pořadí. Zkoumá kvalitu a povahu zveřejněných dokladů o implementaci. Firemní reporty jsou zároveň informačními dokumenty a nástroji legitimizace. Jejich obsah je proto analyzován jako organizací vytvořená reprezentace vlastní praxe, nikoli jako nezávislé potvrzení skutečného dopadu.

## 2. Výzkumné otázky

### Hlavní výzkumná otázka

**Jak vybrané velké podniky působící v České republice ve veřejných zprávách za rok 2024 konstruují a dokládají implementaci ESG a které znaky odlišují deklaraci, formalizaci a manažerskou integraci?**

### Dílčí výzkumné otázky

1. Jak podniky vymezují materiální ESG témata a jak vysvětlují jejich vazbu na strategii a podnikatelský model?
2. Jaké struktury odpovědnosti, dohledu a interní koordinace v reportech uvádějí?
3. Kde je doložena vazba ESG na investice, řízení rizik, odměňování, produkty, nákup nebo provozní rozhodování?
4. Jakou evidenční sílu mají zveřejněné cíle a ukazatele: rozlišují vstupy, aktivity, výstupy, výsledky a dopady?
5. Jak podniky komunikují nesplněné cíle, trade-offy, nejistoty a negativní dopady?
6. Jak se způsoby dokládání implementace liší mezi energetikou, bankovnictvím, telekomunikacemi a automobilovým průmyslem?

## 3. Výběr případů a dokumentů

### 3.1 Strategie výběru

Použit je účelový výběr kontrastních případů. Do korpusu byly zařazeny čtyři velké podniky nebo skupiny s významnou činností a rozhodovací či výrobní základnou v České republice:

| Případ | Sektor | Institucionální charakteristika | Hlavní zdroj |
|---|---|---|---|
| ČEZ Group | energetika | kapitálově náročná transformace, regulace, významný podíl státu | integrovaná výroční finanční zpráva a zpráva o udržitelnosti 2024 |
| MONETA Money Bank | bankovnictví | burzovně obchodovaná banka, finanční dohled, dopady úvěrového portfolia | Sustainability at MONETA 2024 a příslušná část výroční zprávy |
| O2 Czech Republic | telekomunikace | soukromá skupina, energeticky náročná infrastruktura, digitální bezpečnost | ESG Report 2024 |
| Škoda Auto | automobilový průmysl | nadnárodní skupina, produktová transformace a rozsáhlý dodavatelský řetězec | Annual Report / Sustainability Report 2024 a oficiální online report |

Případy nejsou reprezentativním vzorkem české ekonomiky. Záměrem je analytické srovnání odlišných mechanismů: investiční transformace, finanční zprostředkování, provoz digitální infrastruktury a průmyslová výroba. Všechny organizace mají značnou reportovací kapacitu; výzkum proto nevypovídá o běžné praxi malých a středních podniků.

### 3.2 Kritéria zařazení dokumentu

Dokument musel splnit všechna následující kritéria:

1. byl zveřejněn samotnou analyzovanou organizací nebo její skupinou;
2. pokrýval účetní či reportovací období od 1. ledna do 31. prosince 2024;
3. obsahoval informace o strategii, správě, cílech, metrikách nebo konkrétních ESG opatřeních;
4. byl dostupný v úplné podobě v PDF nebo na stabilní oficiální webové stránce;
5. bylo možné určit přesný lokátor — stránku, oddíl nebo stabilní webovou sekci.

Mediální články, žebříčky, poradenské komentáře a firemní tiskové zprávy nebyly kódovány jako primární data. Mohou být použity pouze ke kontrole bibliografického kontextu. K ověření faktu, který report sám pouze tvrdí, by bylo třeba nezávislého zdroje; taková triangulace není automaticky součástí tohoto designu.

### 3.3 Uzavření korpusu

Korpus byl uzavřen před hlavní analýzou a evidován v `sources/corporate-documents.csv`. Každý dokument má stabilní identifikátor, název, vydavatele, období, rozsah, URL, datum přístupu a roli v analýze. Případné změny online dokumentu po datu přístupu nejsou do zmrazeného korpusu zpětně promítány bez záznamu v changelogu.

## 4. Jednotky analýzy a segmentace

Schreier (2012) rozlišuje jednotku analýzy, jednotku kódování a kontextovou jednotku. V této práci jsou definovány následovně:

- **Jednotka analýzy:** jeden podnik jako případ a jeho uzavřený soubor dokumentů za rok 2024.
- **Jednotka kódování:** významově ucelený úsek — věta, odstavec, položka tabulky nebo související skupina položek — obsahující tvrzení o cíli, procesu, odpovědnosti, rozhodnutí, metrice, výsledku, negativním dopadu, omezení nebo ověření.
- **Kontextová jednotka:** celý oddíl dokumentu, případně navazující tabulka a metodická poznámka. Smysl úryvku se neurčuje izolovaně od názvu ukazatele, hranice měření a vysvětlivky.

Segment nesmí být vytvořen jen proto, že obsahuje slovo „ESG“ nebo „udržitelnost“. Naopak může být zařazen i bez těchto slov, pokud popisuje relevantní řídicí mechanismus, například kapitálový plán, pravidlo nákupu, řízení klimatického rizika, pracovní podmínky nebo ochranu zákazníků.

Jeden segment může nést více kódů, pokud zachycuje různé analytické dimenze. Například tvrzení, že představenstvo schválilo investiční plán navázaný na dekarbonizační cíl, může nést kódy `governance-board`, `decision-capex`, `target-timebound` a `evidence-E3`.

## 5. Kódovací rámec

Úplný datový slovník je uložen v `analysis/document-codebook.csv`. Hlavní rodiny kódů jsou:

1. **Tlak a motivace** — regulace, investor, zákazník, mateřská skupina, provozní úspora, řízení rizik, legitimita.
2. **Materialita a strategie** — proces dvojí materiality, vazba na podnikatelský model, sektorové priority, stakeholder engagement.
3. **Governance** — odpovědný orgán, vlastník tématu, výbor, pravidelné reportování, interní kontrola, dovednosti a externí expertiza.
4. **Manažerská integrace** — kapitálové výdaje, provozní rozpočet, úvěrování, produktové portfolio, nákup a dodavatelé, odměňování, řízení rizik.
5. **Metriky a výsledky** — základní rok, cílový rok, hranice, metodika, časová řada, přepočet dat, splněný či nesplněný cíl.
6. **Negativní informace a nejistota** — negativní dopad, růst nepříznivého ukazatele, trade-off, omezení dat, změna metodiky, zrušení či reset cíle.
7. **Ověření a hranice tvrzení** — externí ujištění, omezené ujištění, neověřený report, firemní atribuce, nejasná kauzalita.
8. **Evidenční síla** — E0 až E4.

### 5.1 Škála evidenční síly

Každému relevantnímu tvrzení je přiřazena nejvyšší obhajitelná třída:

| Třída | Definice | Minimální znak | Typický příklad |
|---|---|---|---|
| E0 | deklarace | hodnotový nebo strategický závazek bez mechanismu | „Udržitelnost je prioritou.“ |
| E1 | aktivita | konkrétní provedené opatření nebo objem činnosti | počet proškolených osob, zapojených dodavatelů nebo realizovaný projekt |
| E2 | řízený výsledek | vlastník či proces, měřitelný cíl a sledovaný vývoj | cíl s výchozím rokem, termínem a časovou řadou |
| E3 | rozhodovací vazba | prokazatelná vazba na alokaci zdrojů, riziko, produkt, nákup nebo odměnu | investiční plán v souladu s přechodovým plánem; ESG KPI ve variabilní odměně |
| E4 | ověřitelný dopad | jasná hranice, metodika, časová řada a nezávislé ověření nebo přesvědčivá triangulace | externě ověřená metrika s doloženým výsledkem; nikoli automaticky kauzální společenský dopad |

E4 se používá restriktivně. Externí ujištění nad reportem samo o sobě nepovyšuje všechna tvrzení na E4. Rozhoduje rozsah ujištění a kvalita konkrétní metriky. Omezené ujištění také není ekvivalentem rozumného ujištění ani auditu účinnosti řízení.

## 6. Postup analýzy

### 6.1 Příprava a seznámení s korpusem

1. Ověření, že dokument pochází z oficiální domény a pokrývá rok 2024.
2. Uložení bibliografických údajů a kontrolního součtu lokální kopie, je-li technicky dostupná.
3. První čtení bez kódování se zaměřením na strukturu dokumentu, rozsah, reportingový standard a vztah k výroční zprávě.
4. Případové memo: podnikatelský model, hlavní dopady, deklarované priority a předběžná rizika interpretačního zkreslení.

### 6.2 Pilotní kódování

Pilot zahrnuje nejméně dva kontrastní oddíly z každého případu: jeden o strategii či správě a jeden s výkonnostními údaji. Cílem je prověřit:

- zda se kódy vzájemně nepřekrývají bez analytického přínosu;
- zda lze konzistentně odlišit aktivitu od výsledku a rozhodovací vazby;
- zda lokátor umožňuje nezávisle dohledat segment;
- zda rámec nezvýhodňuje některý sektor;
- zda chybí induktivní kategorie.

Po pilotu se provede jednorázová revize definic. Změny jsou zaznamenány v codebooku a changelogu. Již zakódované segmenty jsou následně znovu posouzeny podle finálních definic.

### 6.3 Hlavní kódování

Kódování probíhá po případech a následně napříč případy:

1. označení segmentu a jeho přesného lokátoru;
2. neutrální parafráze toho, co dokument skutečně sděluje;
3. přiřazení tematických kódů;
4. přiřazení třídy E0–E4 s krátkým odůvodněním;
5. označení statusu tvrzení: `corporate_claim`, `metric`, `interpretation`, `limitation`;
6. záznam alternativního výkladu nebo chybějícího důkazu;
7. přenos vybraných segmentů do evidenční matice.

Po dokončení každého případu vznikne memo, které obsahuje podporující i rozporné důkazy. Teprve poté se vytvářejí témata napříč případy. Tím se omezuje riziko, že dominantní struktura jednoho reportu určí interpretaci všech ostatních.

### 6.4 Kontrolní kódování

Protože hlavní analýzu provádí jeden výzkumník, není předstírána interkodérská reliabilita. Důvěryhodnost je posílena dvěma kontrolami:

- po časovém odstupu je znovu zakódován nejméně desetiprocentní stratifikovaný vzorek segmentů ze všech případů;
- všechny segmenty označené E3 nebo E4 jsou znovu otevřeny v originálu a kontrolovány proti definici třídy a rozsahu tvrzení.

Neshoda se neřeší mechanickým procentem shody, ale revizí definice, zúžením interpretace nebo snížením evidenční třídy. Výsledek kontroly je popsán v metodologické kapitole a auditním logu.

## 7. Syntéza a tvorba témat

Výsledková témata musí splnit čtyři podmínky:

1. jsou podložena více než jedním segmentem nebo přesvědčivým kritickým případem;
2. obsahují minimálně jeden kontrast mezi podniky;
3. rozlišují firemní tvrzení od interpretace autora;
4. uvádějí hranici, negativní případ nebo vysvětlení, co korpus neumožňuje tvrdit.

Počty kódů jsou používány pouze jako orientační mapa pozornosti, nikoli jako statistický důkaz významnosti. Dlouhý report přirozeně vytváří více segmentů než stručný report; četnosti proto nejsou bez normalizace srovnatelným měřítkem kvality.

Výsledná syntéza postupuje ve třech úrovních:

- **vnitropřípadová:** jak je implementace konstruována v jednom podniku;
- **mezipřípadová:** podobnosti a rozdíly v témže mechanismu;
- **teoretická:** vztah zjištění k institucionalismu, legitimitě, materialitě a debatě o symbolickém versus substantivním reportingu.

## 8. Důvěryhodnost a auditovatelnost

### 8.1 Dohledatelnost tvrzení

Každé klíčové zjištění ve výsledcích je spojeno s položkou v `analysis/evidence-matrix.csv` nebo `audit/claim-evidence-ledger.csv`. Položka obsahuje případ, dokument, lokátor, parafrázi, kódy, evidenční třídu, interpretaci a omezení.

### 8.2 Negativní případy

Analýza aktivně vyhledává informace, které narušují jednoduchý pozitivní příběh: růst emisí či spotřeby, nesplněný ukazatel, změnu hranice, zrušený cíl, chybějící KPI, nepokrytou oblast nebo výslovné upozornění na nejistotu. Přítomnost negativní informace není automaticky známkou horší implementace; může naopak zvyšovat informační vyváženost reportu.

### 8.3 Reflexivita

Výchozí očekávání autora jsou zaznamenána před analýzou. Autor počítá s tím, že standardizace ESRS zvýší srovnatelnost struktury a že sektorově materiální témata budou častěji spojena s rozhodováním. Tato očekávání mohou vést k přeceňování formálních vazeb nebo k hledání předem známé typologie. Případová mema proto obsahují sekci „co nesedí na pracovní očekávání“.

### 8.4 Reprodukovatelnost

Repozitář uchovává:

- registr dokumentů;
- uzavřený kódovací rámec a jeho verze;
- korpus segmentů s lokátory;
- evidenční matici;
- případová mema;
- claim ledger;
- log významných AI interakcí a lidských kontrol;
- zmrazenou verzi rukopisu poskytnutou hodnotitelům.

Reprodukovatelnost zde neznamená, že jiný výzkumník musí dojít ke stejným tématům. Znamená, že může dohledat vstupy, porozumět rozhodnutím a věcně napadnout konkrétní interpretační krok.

## 9. Etické a právní aspekty

Výzkum pracuje s veřejnými dokumenty právnických osob a neprovádí nábor ani zpracování neveřejných osobních údajů. Citováni mohou být veřejně uvedení členové vedení pouze tehdy, je-li jejich funkce významná pro interpretaci dokumentu. Přímé citace jsou omezeny a vždy doplněny lokátorem; převládá přesná parafráze.

Analýza se vyhýbá tvrzením o úmyslu. Z dokumentu nelze spolehlivě určit, zda byla určitá formulace vytvořena primárně pro legitimitu, splnění regulace nebo skutečné řízení. Lze pouze identifikovat znaky, které jsou konzistentní se symbolickým či substantivním pojetím, a uvést alternativní vysvětlení.

## 10. Limity metodiky

1. **Sebeprezentační povaha zdrojů:** podnik určuje, co zveřejní, jak stanoví hranice a jak výsledky interpretuje.
2. **Nerovný rozsah dokumentů:** počet dostupných tvrzení odráží reportovací kapacitu a povinnosti, nikoli nutně kvalitu praxe.
3. **Sektorová nesouměřitelnost:** emise energetiky, financované emise banky, digitální bezpečnost telekomunikace a životní cyklus automobilu nelze redukovat na jedinou škálu.
4. **Skupinové hranice:** u nadnárodní skupiny nemusí být vždy možné oddělit rozhodnutí české společnosti od skupinové politiky.
5. **Časový řez:** rok 2024 nezachycuje implementaci jako dlouhodobý proces a následné regulatorní změny let 2025–2026 jsou pouze kontextem.
6. **Bez ověření reality provozu:** analýza neposuzuje závody, smlouvy, interní systémy ani zkušenost zaměstnanců a komunit.
7. **Jediný analytik:** opakované kontrolní kódování zvyšuje konzistenci, ale neodstraňuje interpretační perspektivu autora.
8. **AI v procesu:** jazykový model může urychlit extrakci a navrhovat interpretace, avšak může také produkovat přesvědčivé, ale nepodložené vazby. Každé použité tvrzení proto musí projít kontrolou originálu a být připsáno zdroji.

## 11. Kritérium dokončení analýzy

Analýza je považována za dokončenou, když:

- všechny čtyři případy mají úplné případové memo;
- každý dílčí výzkumný dotaz má podporující i omezující důkazy;
- všechny E3 a E4 položky byly znovu ověřeny v originálu;
- výsledková témata obsahují mezipřípadový kontrast a negativní případ;
- klíčová tvrzení rukopisu jsou napojena na evidenční ledger;
- žádný syntetický materiál není použit jako empirický výsledek.
