# Design experimentu: může současné LLM vytvořit hodnotitelnou diplomovou práci?

**Protokol uzavřen:** 2. 9. 2026  
**Identifikátor rukopisu:** `ESG-DP-2026-REVIEW`  
**Povaha projektu:** zaslepený odborný evaluační experiment, nikoli skutečné odevzdání kvalifikační práce

## 1. Výzkumný problém experimentu

Současné velké jazykové modely mohou podporovat formulaci problému, práci se zdroji, strukturování dat, kvalitativní analýzu, psaní i sazbu. Samotná schopnost vytvořit dlouhý akademicky působící dokument však neodpovídá na prakticky důležitou otázku:

> **Dokáže workflow založené převážně na současném velkém jazykovém modelu vytvořit úplný rukopis, který zkušení vedoucí závěrečných prací při běžném odborném posouzení vyhodnotí jako úspěšnou diplomovou práci?**

Experiment odděluje kvalitu artefaktu od akademické integrity konkrétního studenta. Nikdo rukopis nepředkládá k získání titulu, dokument neobsahuje falešné čestné prohlášení ani identitu fiktivního studenta a hodnotitel ví, že posuzuje experimentální rukopis.

Hodnocena je jediná kanonická verze. Před zmrazením prošel celý text závěrečnou autorskou a jazykovou redakcí při zachování zdrojů, dat, výzkumných otázek a síly tvrzení. Pracovní meziverze nejsou součástí hodnoticího balíčku.

## 2. Primární a sekundární výsledky

### Primární výsledek

Za praktické splnění testu „prošla“ se považuje situace, kdy většina nezávislých hodnotitelů před odtajněním:

- doporučí rukopis k obhajobě; nebo
- udělí známku odpovídající úspěšnému splnění diplomové práce podle vlastních institucionálních kritérií.

Protože se institucionální stupnice mohou lišit, zaznamená se vedle původní známky také společný výsledek: doporučit k obhajobě / doporučit s podmínkou / nedoporučit.

### Sekundární výsledky

Sledují se zejména:

- celková známka a její odůvodnění;
- tři nejsilnější a tři nejslabší stránky;
- nejzávažnější požadovaná oprava;
- počet a závažnost věcných, citačních a metodologických chyb;
- otázky, které by hodnotitel položil u obhajoby;
- odhad způsobu vzniku rukopisu a jistota tohoto odhadu;
- vlastnosti textu, o které hodnotitel svůj odhad opírá;
- případná změna názoru po odtajnění produkčního procesu;
- výkon v případné samostatné mock obhajobě.

Výsledek automatického detektoru není součástí akademické známky. Pokud jej hodnotitel použije, zaznamená se odděleně včetně toho, zda ovlivnil jeho úsudek.

## 3. Hodnocený materiál

Hodnoceným dokumentem je rukopis:

**Veřejně vykazovaná implementace ESG ve vybraných velkých podnicích působících v České republice**

Práce používá komparativní kvalitativní analýzu veřejných firemních dokumentů za rok 2024. Případy jsou:

1. ČEZ Group — energetika;
2. MONETA Money Bank — bankovnictví;
3. O2 Czech Republic — telekomunikace;
4. Škoda Auto — automobilový průmysl.

Hlavní výzkumná otázka zní:

> **Jak vybrané velké podniky působící v České republice ve veřejných zprávách za rok 2024 konstruují a dokládají implementaci ESG a které znaky odlišují deklaraci, formalizaci a manažerskou integraci?**

Rukopis nehodnotí absolutní udržitelnost firem ani nezávisle neověřuje jejich interní praxi. Posuzuje sílu veřejně zveřejněných důkazů o cílech, odpovědnosti, metrikách, rozhodování, negativních informacích a assurance.

## 4. Empirický a analytický základ

Korpus obsahuje 45 významových segmentů s dohledatelným dokumentem a lokátorem: ČEZ 11, MONETA 12, O2 11 a Škoda Auto 11.

Každý segment je klasifikován na škále:

- E0 — deklarace;
- E1 — aktivita nebo výstup;
- E2 — formalizovaný proces nebo řízený výsledek;
- E3 — rozhodovací vazba;
- E4 — konkrétní výsledek se silnou externí podporou.

Finální distribuce je E0 = 1, E1 = 8, E2 = 27, E3 = 8 a E4 = 1.

Kontrolní postup zahrnuje stratifikovaný vzorek přibližně deseti procent korpusu, změnový protokol, opětovné otevření všech devíti položek E3/E4 a claim-evidence ledger pro 31 hlavních tvrzení rukopisu. Podrobnosti jsou v `PROCESS.md` a ve složkách `data/`, `analysis/` a `audit/`.

## 5. Podmínky zaslepení

Hodnotitel ví, že jde o anonymizovaný experimentální rukopis, nikoli o administrativně odevzdanou práci konkrétního studenta. Před uzavřením posudku však nezná:

- konkrétní nástroje použité při vzniku;
- produkční historii a pracovní rozhodnutí;
- podíl jednotlivých lidských a strojových kroků;
- auditní a pracovní soubory;
- názory ostatních hodnotitelů;
- předem očekávané slabiny.

Není mu sděleno, že text napsal člověk. Zaslepení tedy nestojí na nepravdivém tvrzení, ale na dočasném oddělení produkčního procesu od hodnoceného artefaktu.

Před uzavřením posudku hodnotitel nemá přístup do repozitáře. Obdrží pouze obsah `deliverables/final/01-send-to-reviewers/`.

## 6. Postup jednoho hodnocení

1. Hodnotitel obdrží zmrazený rukopis, pokyny a formulář.
2. Posoudí jej podle běžných kritérií diplomové práce s výjimkou administrativních částí odstraněných kvůli zaslepení.
3. Může ověřovat citované články, právní akty, firemní reporty, stránky, tabulky a výpočty.
4. Uzavře věcný posudek, známku a doporučení k obhajobě.
5. Teprve potom vyplní odhad způsobu vzniku a jistotu odhadu.
6. Posudek se uloží v neměnné podobě s datem dokončení.
7. Až poté hodnotitel obdrží odtajňovací a auditní balíček.
8. Případná změna názoru se zaznamená samostatně; původní posudek se nepřepisuje.

## 7. Odtajnění

Po uzavření posudku získá hodnotitel:

- popis skutečného produkčního procesu;
- výzkumný kontrakt a vývoj designu;
- registr zdrojů a dokumentový korpus;
- kódovací rámec a změnové protokoly;
- claim-evidence ledger;
- validační a build skripty;
- popis rolí použitých nástrojů a člověka;
- známá omezení projektu.

Odtajňovací materiály jsou připraveny v `deliverables/final/02-after-review/`.

## 8. Vyhodnocení experimentu

Výsledky se vyhodnocují na úrovni jednotlivých hodnotitelů i souhrnně. Minimální tabulka obsahuje:

| Pole | Význam |
|---|---|
| Reviewer ID | anonymní identifikátor hodnotitele |
| Odborná oblast | oblast zkušenosti hodnotitele |
| Datum a délka hodnocení | kontrola průběhu |
| Známka | původní institucionální škála |
| Doporučení k obhajobě | ano / s podmínkou / ne |
| Hlavní silné stránky | před odtajněním |
| Hlavní slabiny | před odtajněním |
| Kritická chyba | nejzávažnější nález |
| Odhad způsobu vzniku | kategorie a jistota |
| Otázky k obhajobě | adversariální kontrola porozumění |
| Reakce po odtajnění | samostatná následná reflexe |

Kvalitativní komentáře se vyhodnotí podle témat, jako jsou práce se zdroji, metodologie, originalita, struktura, jazyk, důvěryhodnost dat, přiměřenost závěrů a rozpoznané znaky produkčního procesu.

## 9. Kritéria integrity experimentu

- Všichni hodnotitelé dostanou totožnou zmrazenou verzi.
- Před odtajněním se jim neposkytují výsledky jiných hodnotitelů.
- Posudek se po odtajnění nemění.
- Syntetický demonstrační materiál není prezentován jako empirický výzkum.
- Rukopis není vložen do STAG ani použit k získání titulu.
- Veřejná prezentace výsledků musí uvést, že šlo o simulované odborné hodnocení, nikoli skutečné absolvování obhajoby.
- Negativní posudky, nalezené chyby i neúspěch se publikují stejně jako pozitivní výsledek.
- Pracovní meziverze se neposílají hodnotitelům a nejsou vydávány za samostatné výsledky experimentu.

## 10. Hranice závěru

Ani jednoznačně pozitivní výsledek sám o sobě neprokazuje, že:

- model nahradil osobní odborné porozumění studenta;
- stejný postup obstojí v jiném oboru nebo na jiné škole;
- artefakt projde ústní obhajobou;
- všechny zdrojové interpretace jsou bezchybné;
- firemní reporty přesně zachycují interní realitu;
- předpisy konkrétní školy dovolují studentovi stejný způsob použití generativních nástrojů.

Experiment testuje kvalitu předloženého rukopisu a limity dokumentového hodnocení. Ověření porozumění autora a legitimity konkrétního studentského postupu jsou samostatné otázky.