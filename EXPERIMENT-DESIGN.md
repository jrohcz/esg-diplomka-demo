# Design experimentu: může současné LLM vytvořit hodnotitelnou diplomovou práci?

**Finální protokol:** 1. 9. 2026  
**Identifikátor rukopisu:** `ESG-DP-2026-BLIND-01`  
**Povaha projektu:** zaslepený odborný evaluační experiment, nikoli skutečné odevzdání kvalifikační práce

## 1. Výzkumný problém experimentu

Současné velké jazykové modely již neumějí pouze generovat jednotlivé odstavce. Dokážou podporovat formulaci výzkumného problému, rešerši, strukturování dat, analýzu, psaní i sazbu. Samotná technická schopnost vytvořit dlouhý akademicky působící dokument však neodpovídá na prakticky důležitou otázku:

> **Dokáže LLM-orientovaný workflow vytvořit úplný rukopis, který zkušení vedoucí závěrečných prací při běžném odborném posouzení vyhodnotí jako úspěšnou diplomovou práci?**

Experiment odděluje kvalitu artefaktu od otázky akademické integrity konkrétního studenta. Nikdo tento rukopis nepředkládá k získání titulu a dokument neobsahuje falešné čestné prohlášení ani identitu fiktivního studenta.

## 2. Primární a sekundární výsledky

### Primární výsledek

Za praktické splnění testu „prošla“ se považuje situace, kdy většina nezávislých hodnotitelů před odtajněním:

- doporučí rukopis k obhajobě; nebo
- udělí známku odpovídající úspěšnému splnění diplomové práce podle vlastních institucionálních kritérií.

Výsledky jednotlivých hodnotitelů se zachovají i tehdy, pokud se jejich škály liší. Pro společné srovnání se zároveň zaznamená binární výsledek doporučit / nedoporučit k obhajobě.

### Sekundární výsledky

Sledují se zejména:

- celková známka a její odůvodnění;
- tři nejsilnější a tři nejslabší stránky;
- nejzávažnější požadovaná oprava;
- počet a závažnost věcných, citačních a metodologických chyb;
- otázky, které by hodnotitel položil u obhajoby;
- odhad způsobu vzniku rukopisu a jistota tohoto odhadu;
- změna názoru po odtajnění produkčního procesu;
- případný výkon v samostatné mock obhajobě.

## 3. Hodnocený materiál

Zmrazeným materiálem je sedmdesátistránkový rukopis:

**Veřejně vykazovaná implementace ESG ve vybraných velkých podnicích působících v České republice**

Rukopis používá komparativní kvalitativní analýzu veřejných firemních dokumentů za rok 2024. Případy:

1. ČEZ Group — energetika;
2. MONETA Money Bank — bankovnictví;
3. O2 Czech Republic — telekomunikace;
4. Škoda Auto — automobilový průmysl.

Výzkumná otázka rukopisu zní:

> **Jak vybrané velké podniky působící v České republice ve veřejných zprávách za rok 2024 konstruují a dokládají implementaci ESG a které znaky odlišují deklaraci, formalizaci a manažerskou integraci?**

Dokument nehodnotí absolutní udržitelnost firem ani pravdivost jejich interní praxe. Hodnotí sílu veřejně zveřejněného důkazu o cílech, odpovědnosti, metrikách, rozhodování, negativních informacích a assurance.

## 4. Empirický a analytický základ

Finální korpus obsahuje 45 významových segmentů s dohledatelným dokumentem a lokátorem. Počty případů jsou vyrovnané: ČEZ 11, MONETA 12, O2 11 a Škoda Auto 11.

Každý segment je klasifikován na škále:

- E0 — deklarace;
- E1 — aktivita nebo výstup;
- E2 — formalizovaný proces nebo řízený výsledek;
- E3 — rozhodovací vazba;
- E4 — konkrétní výsledek se silnou externí podporou.

Finální distribuce je E0 = 1, E1 = 8, E2 = 27, E3 = 8 a E4 = 1.

Kontrolní postup zahrnuje stratifikovaný vzorek přibližně 10 % korpusu, změnový protokol, opětovné otevření všech devíti položek E3/E4 a claim-evidence ledger pro 31 hlavních tvrzení rukopisu. Podrobnosti jsou v `PROCESS.md` a příslušných složkách `data/`, `analysis/` a `audit/`.

## 5. Podmínky zaslepení

Hodnotitel ví, že jde o anonymizovaný experimentální rukopis, nikoli o administrativně odevzdanou práci konkrétního studenta. Před uzavřením posudku však nezná:

- konkrétní nástroje použité při vzniku;
- historii promptů a commitů;
- podíl jednotlivých lidských a strojových kroků;
- auditní a pracovní soubory;
- názory ostatních hodnotitelů;
- předem očekávané slabiny.

Není mu tvrzeno, že text napsal člověk. Zaslepení tedy není založeno na nepravdivém sdělení, ale na dočasném oddělení produkčního procesu od hodnoceného artefaktu.

Hodnotitelé nemají před uzavřením posudku přístup do tohoto repozitáře. Obdrží pouze obsah `deliverables/2026-09-01/01-send-to-reviewers/`.

## 6. Postup jednoho hodnocení

1. Hodnotitel obdrží zmrazený rukopis, pokyny a formulář.
2. Posoudí jej podle běžných kritérií diplomové práce, s výjimkou záměrně odstraněných administrativních částí.
3. Může ověřovat zdroje, DOI, právní akty, firemní reporty, stránky, tabulky i výpočty.
4. Uzavře známku, doporučení k obhajobě a věcný posudek.
5. Teprve potom vyplní odhad způsobu vzniku textu a jistotu odhadu.
6. Posudek se uloží v neměnné podobě s datem dokončení.
7. Až poté hodnotitel obdrží odtajňovací a auditní balíček.
8. Případná následná změna názoru se zaznamená odděleně; původní posudek se nepřepisuje.

Automatický AI detektor není použit jako podklad akademické známky. Případný experiment s detektorem se provádí až odděleně a jeho výsledek se zaznamenává jako vedlejší údaj.

## 7. Odtajnění

Po uzavření všech posudků se hodnotitelům zpřístupní:

- popis produkčního procesu;
- výzkumný kontrakt a vývoj designu;
- korpus, codebook a změnové protokoly;
- claim-evidence ledger;
- validační a build skripty;
- informace o použitých nástrojích;
- známá omezení projektu.

Připravený archiv je v `deliverables/2026-09-01/02-after-review/`.

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
| Odhad AI | kategorie a jistota |
| Otázky k obhajobě | adversariální kontrola porozumění |
| Reakce po odtajnění | samostatná následná reflexe |

Kvalitativní komentáře se analyzují tematicky: práce se zdroji, metodologie, originalita, struktura, jazyk, důvěryhodnost dat, přiměřenost závěrů a rozpoznané znaky strojového vzniku.

## 9. Kritéria integrity experimentu

- Všichni hodnotitelé dostanou stejnou zmrazenou verzi.
- Před odtajněním se jim neposkytují výsledky jiných hodnotitelů.
- Posudek se po odtajnění nemění.
- Syntetický pilot není prezentován jako empirický výzkum.
- Rukopis není vložen do STAG ani použit k získání titulu.
- Veřejná prezentace výsledků musí uvést, že šlo o simulované odborné hodnocení, nikoli skutečné absolvování obhajoby.
- Negativní posudky, nedohledané chyby a selhání se publikují stejně jako úspěchy.

## 10. Hranice závěru

Ani jednoznačně pozitivní výsledek sám o sobě neprokazuje, že:

- LLM nahradilo osobní odborné porozumění studenta;
- stejný postup obstojí v jiném oboru nebo na jiné škole;
- artefakt projde ústní obhajobou;
- všechny zdrojové interpretace jsou bezchybné;
- současné školní předpisy umožňují konkrétnímu studentovi takový způsob použití AI.

Experiment testuje kvalitu předloženého rukopisu a limity dokumentového hodnocení. Ověření autorova porozumění a legitimity konkrétního použití AI jsou samostatné otázky.
