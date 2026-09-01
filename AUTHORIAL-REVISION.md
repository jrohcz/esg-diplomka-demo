# Autorská redakce rukopisu (humanizer pass)

**Stav:** nový závěrečný krok experimentu  
**Výchozí verze:** `ESG-DP-2026-BLIND-01`  
**Cílová verze:** `ESG-DP-2026-BLIND-02`  
**Pracovní větev:** `experiment/authorial-revision-pass`

## Proč tento krok vznikl

První zmrazený rukopis obstál v obsahové, zdrojové a technické kontrole, jeho próza je však výrazně homogenní. Předběžný test několika úryvků teoretické kapitoly v automatických detektorech je označil jako vysoce pravděpodobně generované. Srovnávací diplomová práce se zřetelně nepravidelnějším autorským stylem přitom ve stejném orientačním testu dosáhla podstatně nižších hodnot.

Tento výsledek není důkazem původu žádného textu. AI detektor měří povrchové statistické znaky a může se mýlit oběma směry. Pro experiment je však relevantní, že první verze působí stylisticky uniformně nejen na detektor, ale i při pozorném lidském čtení. Proto se zavádí samostatná autorská redakce.

V interní komunikaci lze krok označit jako „humanizer“. V metodice a veřejném popisu se používá přesnější název **autorská redakce** nebo **authorial revision pass**. Cílem není obcházet kontrolní systém, ale odstranit mechanicky působící prózu, aniž se změní data, tvrzení nebo zdroje.

## Zásadní pravidlo: baseline se nepřepisuje

Verze `BLIND-01` zůstává zachována jako původní LLM-orientovaný rukopis. Autorská redakce vytváří novou verzi `BLIND-02`. Tím lze později odděleně odpovědět na dvě otázky:

1. jak dopadne obsahově kvalitní, ale stylisticky málo redigovaný LLM výstup;
2. jak dopadne stejný výzkum po důsledné autorské redakci.

Bez této verze by nebylo možné poznat, zda výsledek zlepšil samotný výzkumný základ, sazba, nebo až poslední stylistický krok.

## Co je na první verzi stylisticky podezřelé

Nejde o jednotlivá „AI slova“, ale o souběh několika vlastností:

- mnoho krátkých podkapitol má téměř stejnou vnitřní stavbu: definice, vysvětlení, výhrada a vazba na empirii;
- argumentace je neobvykle komprimovaná a téměř každý odstavec plní přesně jednu funkci;
- často se vracejí konstrukce typu „může, ale nemusí“, „nejde o X, ale o Y“ a „pro tuto práci je proto“;
- věty i odstavce mají podobný rytmus a podobnou míru opatrnosti;
- text málo ukazuje, kde autor skutečně volí mezi dvěma možnými výklady;
- citace jsou zapojovány velmi pravidelně a přechody mezi zdroji působí až příliš hladce;
- jednotlivé části jsou dokonale provázané s metodologií, což je věcně silné, ale v součtu připomíná text sestavený podle osnovy jedním průchodem.

Srovnávací lidská práce obsahuje delší a nestejnoměrné věty, lokální návraty k předchozím pasážím, osobitější slovník, explicitní rozhodnutí autora i určitou redundanci. Obsahuje také jazykové nedokonalosti. Poslední vlastnost se **nesmí mechanicky napodobovat**. Záměrné přidávání chyb by zhoršilo práci a z experimentu by vytvořilo test klamání místo testu akademické kvality.

## Cíl autorské redakce

Cílem je, aby text působil jako práce autora, který:

- tématu rozumí a nemusí každou větu skládat podle stejné šablony;
- dokáže vysvětlit, proč určitou hranici zvolil a jinou odmítl;
- vrací se ke konkrétním problémům práce, nikoli pouze k abstraktním kategoriím;
- rozlišuje, co je převzatý poznatek, co vlastní interpretace a co metodické rozhodnutí;
- někde postupuje stručně a jinde argument rozvine podle jeho skutečné složitosti;
- připouští nejistotu konkrétně, nikoli automatickou závěrečnou větou v každém odstavci.

Výsledkem nemá být hovorový text ani imitace nedbalého studenta. Stále jde o odbornou diplomovou práci.

## Postup redakce jedné kapitoly

### 1. Zmrazení významu

Před přepisem se uloží:

- seznam hlavních tvrzení kapitoly;
- všechny použité citace;
- vazby na claim-evidence ledger;
- tabulky, číselné hodnoty a lokátory;
- tvrzení, která nesmí být rozšířena.

Tento „meaning lock“ je důležitější než původní slovosled. Humanizer nesmí zlepšit plynulost tím, že posune sílu tvrzení.

### 2. Autorské memo

Ke každé podkapitole se před přepisem stručně odpoví:

- Co je zde skutečný argument?
- Proč je pro tuto práci potřeba právě zde?
- Jaké alternativní vysvětlení nebo námitka je nejsilnější?
- Které rozhodnutí autora z textu dosud není vidět?
- K čemu se má čtenář po dočtení části vrátit v empirii?

Memo se nepřepisuje přímo do rukopisu. Slouží jako opora pro nové vystavění textu.

### 3. Přepis po významových blocích

Text se nepřepisuje větu po větě ani pomocí synonym. Celý odstavec nebo podkapitola se znovu napíše z porozumění zdrojům a autorskému memu. Původní formulace se používá pouze ke kontrole, zda něco nevypadlo.

Tento krok má odstranit zejména syntaktické stopy „parafrázování původního AI textu“. Synonymický spinner často zachová stejnou stavbu vět, stejnou argumentační symetrii a navíc poškodí terminologii.

### 4. Viditelná autorská rozhodnutí

V textu mají být přirozeně přítomny věty, které ukazují skutečnou volbu, například:

- proč se práce nezabývá celkovým ESG ratingem podniku;
- proč je assurance odděleno od rozhodovací vazby;
- proč dokumentový design neumožňuje tvrdit něco o interní praxi;
- proč byl určitý koncept ponechán pouze jako analytická čočka;
- proč je v jednom místě vhodnější konkrétní příklad než další obecná definice.

Autorský hlas neznamená opakovat „domnívám se“. Znamená zpřítomnit úsudek a jeho důvod.

### 5. Přirozenější rytmus

Redakce pracuje s rytmem podle obsahu:

- důležitá definice může stát v krátké větě;
- složitý vztah může vyžadovat delší souvětí;
- odstavce nemají mít stejný počet vět;
- ne každá podkapitola musí končit metodologickou poučkou;
- výčet se používá jen tehdy, když jde skutečně o výčet, ne jako automatický způsob organizace myšlenek;
- citace mohou stát na začátku, uprostřed i na konci argumentu podle své funkce.

Variabilita se nevyrábí náhodně. Musí vycházet z významu.

### 6. Redukce šablonovitého metajazyka

Při redakci se cíleně hledají a posuzují opakované konstrukce:

- „Pro tuto práci je...“;
- „Práce proto...“;
- „Empirická analýza...“;
- „Výsledky ukazují...“;
- „Současně však...“;
- „Může..., ale nemusí...“;
- „Nejde pouze o..., ale také o...“;
- automatické trojice a čtveřice substantiv;
- závěrečná věta, která pokaždé převádí teorii do stejného analytického pravidla.

Konstrukce nejsou zakázané. Problémem je jejich mechanické opakování.

### 7. Konkrétní kotvy

Obecný argument se tam, kde je to věcně možné, ukotví v problému rukopisu. Například materialita se nevysvětluje pouze definicí, ale otázkou, zda její výsledek ovlivnil investiční plán, úvěrové portfolio, datové centrum nebo dodavatelský řetězec. Tím se text přibližuje skutečnému uvažování nad čtyřmi případy a přestává působit jako univerzální učebnicové shrnutí.

### 8. Zdrojová kontrola po přepisu

Každý nově formulovaný odstavec se porovná s:

- původní citací;
- registrem zdrojů;
- claim-evidence ledgerem;
- metodickými hranicemi práce.

Změna stylu nesmí způsobit:

- nový kauzální závěr;
- rozšíření jednoho případu na celé odvětví;
- záměnu firemního tvrzení za ověřený fakt;
- záměnu omezeného a přiměřeného ujištění;
- záměnu výsledku, dopadu a rozhodovacího mechanismu.

### 9. Čtení nahlas a lokální editace

Kapitola se čte nahlas nebo po kratších blocích bez současného pohledu do původní verze. Sledují se zejména:

- rytmicky stejné věty za sebou;
- série odstavců začínajících stejným způsobem;
- přechody, které znějí logicky, ale nic konkrétního nespojují;
- příliš mnoho abstraktních substantiv;
- místa, kde čtenář neví, proč následuje další zdroj;
- náhlé skoky mezi popisem literatury a vlastním analytickým rámcem.

### 10. Automatizovaný stylový audit

Skript `scripts/style-audit.py` neodhaduje autorství. Pouze upozorňuje na opakované začátky vět, frekvenci šablonovitých frází, distribuci délky vět a odstavců a opakující se n-gramy. Výstup slouží editorovi, nikoli jako automatická podmínka přijetí textu.

### 11. Fixní detektorový benchmark

Teprve po zdrojové a jazykové kontrole se použijí stejné předem zmrazené úryvky ve stejných detektorech. Zaznamená se:

- přesné znění a rozsah úryvku;
- název a verze detektoru;
- datum;
- výsledek baseline `BLIND-01`;
- výsledek verze `BLIND-02`;
- případná variabilita při opakovaném testu.

Detektorové skóre je **sekundární pozorování**, nikoli důkaz autorství a nikoli jediný optimalizační cíl. Přepis, který sníží skóre, ale zhorší přesnost nebo akademickou úroveň, se odmítá.

### 12. Zmrazení nové verze

Po dokončení všech kapitol se vytvoří nový identifikátor, nový PDF/DOCX export, nové kontrolní součty a nová složka v `deliverables/`. `BLIND-01` zůstane beze změny.

## Co je výslovně zakázáno

- záměrné vkládání pravopisných nebo gramatických chyb;
- nahodilé prodlužování textu vatou;
- kopírování formulací ze srovnávací práce;
- synonymický spinning bez nového vystavění argumentu;
- neviditelné znaky, homoglyphy, překlady tam a zpět nebo jiné technické obcházení detektorů;
- změna dat, citací nebo významu jen proto, aby text působil méně strojově;
- využití veřejného „humanizeru“, který neumožňuje audit změn nebo může uchovávat vložený rukopis.

## Akceptační kritéria

Kapitola je po autorské redakci připravena, pokud:

1. všechna původní nosná tvrzení jsou zachována nebo je změna výslovně zalogována;
2. každá citace stále podporuje větu, u níž je uvedena;
3. nevzniklo žádné nové nepodložené faktické tvrzení;
4. text má variabilnější, významově motivovaný rytmus;
5. opakované šablonovité fráze byly omezeny;
6. autorova rozhodnutí a hranice jsou konkrétní, nikoli pouze deklarované;
7. kapitola prošla čtením nahlas a zdrojovou kontrolou;
8. změny jsou uvedeny v `audit/authorial-revision-log.csv`;
9. detektorový výsledek je zaznamenán odděleně a nebyl použit k ospravedlnění věcného zhoršení.

## Struktura artefaktů

- `variants/authorial-pass/chapters/` — redigované kapitoly;
- `variants/authorial-pass/README.md` — stav varianty a návod k sestavení;
- `analysis/style-benchmark.md` — stylistická diagnóza baseline;
- `audit/authorial-revision-log.csv` — audit změn;
- `audit/detector-benchmark.csv` — výsledky fixních testů;
- `prompts/authorial-revision.md` — reprodukovatelný redakční prompt;
- `scripts/style-audit.py` — pomocná povrchová diagnostika.

## Interpretace výsledku

Pokud `BLIND-02` získá lepší posudek než `BLIND-01`, nelze výsledek připsat pouze „menší detekovatelnosti“. Autorská redakce současně zlepšuje čitelnost, argumentační hierarchii a viditelnost rozhodnutí. Pokud se sníží detektorové skóre, ale odborné hodnocení se nezmění, bude to naopak užitečný důkaz, že detektor a akademická kvalita měří odlišné vlastnosti.

Nejdůležitější je v závěru přesně uvést, zda poslední redakci provedl další LLM průchod, člověk, nebo kombinace obou. Právě tato informace rozhoduje, zda výsledek dokládá schopnost samotného LLM workflow, nebo schopnost člověka vytvořit kvalitní práci s intenzivní podporou LLM.