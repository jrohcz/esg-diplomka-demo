# Design experimentu: může současné LLM vytvořit hodnotitelnou diplomovou práci?

**Baseline protokol:** 1. 9. 2026  
**Rozšíření o autorskou redakci:** 2. 9. 2026  
**Identifikátory rukopisu:** `ESG-DP-2026-BLIND-01` a připravovaný `ESG-DP-2026-BLIND-02`  
**Povaha projektu:** zaslepený odborný evaluační experiment, nikoli skutečné odevzdání kvalifikační práce

## 1. Výzkumný problém experimentu

Současné velké jazykové modely již neumějí pouze generovat jednotlivé odstavce. Dokážou podporovat formulaci výzkumného problému, rešerši, strukturování dat, analýzu, psaní i sazbu. Samotná technická schopnost vytvořit dlouhý akademicky působící dokument však neodpovídá na prakticky důležitou otázku:

> **Dokáže LLM-orientovaný workflow vytvořit úplný rukopis, který zkušení vedoucí závěrečných prací při běžném odborném posouzení vyhodnotí jako úspěšnou diplomovou práci?**

Experiment odděluje kvalitu artefaktu od otázky akademické integrity konkrétního studenta. Nikdo tento rukopis nepředkládá k získání titulu a dokument neobsahuje falešné čestné prohlášení ani identitu fiktivního studenta.

Po prvním technickém zmrazení byla doplněna druhá otázka:

> **Jak se změní odborné hodnocení a povrchová detekovatelnost téhož výzkumného základu po závěrečné autorské redakci, která zachová data, zdroje a sílu tvrzení?**

Tato druhá otázka není totožná s testem „dokáže detektor poznat AI“. Sleduje, zda stylistická homogenita první verze představuje samostatnou slabinu rukopisu a zda její odstranění ovlivní lidský posudek.

## 2. Primární a sekundární výsledky

### Primární výsledek

Za praktické splnění testu „prošla“ se považuje situace, kdy většina nezávislých hodnotitelů před odtajněním:

- doporučí rukopis k obhajobě; nebo
- udělí známku odpovídající úspěšnému splnění diplomové práce podle vlastních institucionálních kritérií.

Výsledky jednotlivých hodnotitelů se zachovají i tehdy, pokud se jejich škály liší. Pro společné srovnání se zároveň zaznamená binární výsledek doporučit / nedoporučit k obhajobě.

Primární výsledek se vykazuje samostatně pro každou textovou variantu. Pokud počet hodnotitelů neumožní smysluplné přímé srovnání, nebude rozdíl mezi variantami prezentován jako statistický efekt, ale jako kvalitativní pilot.

### Sekundární výsledky

Sledují se zejména:

- celková známka a její odůvodnění;
- tři nejsilnější a tři nejslabší stránky;
- nejzávažnější požadovaná oprava;
- počet a závažnost věcných, citačních a metodologických chyb;
- otázky, které by hodnotitel položil u obhajoby;
- odhad způsobu vzniku rukopisu a jistota tohoto odhadu;
- změna názoru po odtajnění produkčního procesu;
- případný výkon v samostatné mock obhajobě;
- detektorová skóre fixních úryvků před a po autorské redakci;
- změna čitelnosti, stylové přirozenosti a vnímané autorské přítomnosti.

Detektorové skóre zůstává vedlejším údajem. Není součástí akademické známky a samo neurčuje, zda varianta uspěla.

## 3. Hodnocený materiál

Výzkumným základem je sedmdesátistránkový rukopis:

**Veřejně vykazovaná implementace ESG ve vybraných velkých podnicích působících v České republice**

Rukopis používá komparativní kvalitativní analýzu veřejných firemních dokumentů za rok 2024. Případy:

1. ČEZ Group — energetika;
2. MONETA Money Bank — bankovnictví;
3. O2 Czech Republic — telekomunikace;
4. Škoda Auto — automobilový průmysl.

Výzkumná otázka rukopisu zní:

> **Jak vybrané velké podniky působící v České republice ve veřejných zprávách za rok 2024 konstruují a dokládají implementaci ESG a které znaky odlišují deklaraci, formalizaci a manažerskou integraci?**

Dokument nehodnotí absolutní udržitelnost firem ani pravdivost jejich interní praxe. Hodnotí sílu veřejně zveřejněného důkazu o cílech, odpovědnosti, metrikách, rozhodování, negativních informacích a assurance.

### 3.1 Varianta BLIND-01

`ESG-DP-2026-BLIND-01` je původní zmrazená verze. Má dokončený výzkumný základ, kontrolu důkazů, sazbu a technickou validaci, ale neprošla samostatným authorial revision passem zaměřeným na kompoziční a rytmickou homogenitu.

Tato verze se nesmí zpětně přepisovat. Slouží jako baseline.

### 3.2 Varianta BLIND-02

`ESG-DP-2026-BLIND-02` používá stejný korpus, kódování, výsledky, citace a metodické hranice. Rozdíl smí vzniknout pouze v:

- stavbě odstavců a podkapitol;
- pořadí vysvětlení v rámci téhož argumentu;
- rytmu a délce vět;
- míře a podobě autorského metajazyka;
- konkrétnosti přechodů a vysvětlení autorských voleb;
- odstranění opakujících se šablonovitých formulací.

Každá změna významu, citace, číselného údaje nebo metodického závěru musí být výslovně zalogována a znovu ověřena. Úplný protokol je v `AUTHORIAL-REVISION.md`.

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

Obě textové varianty musí vycházet z tohoto totožného základu. Pokud autorská redakce odhalí věcnou chybu, oprava se zapíše jako obsahová korekce a nelze ji vydávat za čistě stylistický rozdíl.

## 5. Podmínky zaslepení

Hodnotitel ví, že jde o anonymizovaný experimentální rukopis, nikoli o administrativně odevzdanou práci konkrétního studenta. Před uzavřením posudku však nezná:

- konkrétní nástroje použité při vzniku;
- historii promptů a commitů;
- podíl jednotlivých lidských a strojových kroků;
- auditní a pracovní soubory;
- názory ostatních hodnotitelů;
- předem očekávané slabiny;
- detektorové výsledky;
- existenci druhé varianty, pokud není součástí předem stanoveného komparativního designu.

Není mu tvrzeno, že text napsal člověk. Zaslepení tedy není založeno na nepravdivém sdělení, ale na dočasném oddělení produkčního procesu od hodnoceného artefaktu.

Hodnotitelé nemají před uzavřením posudku přístup do tohoto repozitáře. Obdrží pouze obsah příslušné složky `deliverables/.../01-send-to-reviewers/`.

## 6. Přidělení variant hodnotitelům

Vzhledem k malému počtu dostupných odborných hodnotitelů jsou přípustné tři režimy. Zvolený režim musí být určen před rozesláním další verze.

### Režim A — pouze BLIND-02

Všichni hodnotitelé dostanou autorsky redigovanou verzi. `BLIND-01` zůstane technickou baseline pro detektorový a textový diff. Tento režim nejlépe odpovídá praktické otázce, zda lze LLM workflow dovést k rukopisu, který projde, ale neumožní přímé srovnání známek obou variant.

### Režim B — paralelní rozdělení

Hodnotitelé se předem rozdělí mezi `BLIND-01` a `BLIND-02`. Každý vidí pouze jednu verzi. Při nízkém počtu hodnotitelů je výsledek exploratorní; rozdíl může souviset s přísností konkrétní osoby.

### Režim C — postupné dvojí čtení

Tentýž hodnotitel nejprve uzavře posudek jedné verze a poté dostane druhou. Druhé čtení již není plně zaslepené a musí být označeno jako komparativní redakční posouzení, nikoli jako nezávislý druhý akademický posudek.

Pro hlavní tvrzení „prošla / neprošla“ je preferován režim A nebo B. Režim C je vhodný pro kvalitativní otázku, které změny byly pro hodnotitele skutečně znatelné.

## 7. Postup jednoho hodnocení

1. Hodnotitel obdrží zmrazený rukopis, pokyny a formulář.
2. Posoudí jej podle běžných kritérií diplomové práce, s výjimkou záměrně odstraněných administrativních částí.
3. Může ověřovat zdroje, DOI, právní akty, firemní reporty, stránky, tabulky i výpočty.
4. Uzavře známku, doporučení k obhajobě a věcný posudek.
5. Teprve potom vyplní odhad způsobu vzniku textu a jistotu odhadu.
6. Posudek se uloží v neměnné podobě s datem dokončení.
7. Až poté hodnotitel obdrží odtajňovací a auditní balíček.
8. Případná následná změna názoru se zaznamená odděleně; původní posudek se nepřepisuje.

Automatický AI detektor není použit jako podklad akademické známky. Případný experiment s detektorem se provádí odděleně nad fixními úryvky a jeho výsledek se zaznamenává jako vedlejší údaj.

## 8. Detektorový benchmark

Pro obě varianty se použije totožná sada předem definovaných úryvků. Každý úryvek má stabilní `excerpt_id`, přesný začátek a konec a přibližně stejný počet slov. Doporučená sada pokrývá teorii, regulatorní kontext, metodologii, výsledky a diskusi.

Zaznamenává se:

- přesný text nebo jeho kryptografický otisk;
- počet slov;
- název a verze detektoru;
- datum a jazykové nastavení;
- skóre při prvním a případném opakovaném běhu;
- varianta rukopisu;
- poznámka o limitech nástroje.

Výsledky se ukládají do `audit/detector-benchmark.csv`. Detektory se nepoužívají jako redakční oracle po každé větě. Opakované ladění textu proti jednomu nástroji by vytvořilo overfitting a snížilo hodnotu experimentu.

## 9. Odtajnění

Po uzavření všech posudků se hodnotitelům zpřístupní:

- popis produkčního procesu;
- výzkumný kontrakt a vývoj designu;
- korpus, codebook a změnové protokoly;
- claim-evidence ledger;
- validační a build skripty;
- informace o použitých nástrojích;
- známá omezení projektu.

U `BLIND-02` se navíc zpřístupní:

- `AUTHORIAL-REVISION.md`;
- použitý redakční prompt;
- revizní log po kapitolách;
- stylový audit;
- detektorové výsledky obou variant;
- přesné rozlišení lidských a strojových zásahů.

Připravený archiv baseline je v `deliverables/2026-09-01/02-after-review/`. Varianta `BLIND-02` dostane vlastní odtajňovací archiv.

## 10. Vyhodnocení experimentu

Výsledky se vyhodnocují na úrovni jednotlivých hodnotitelů i souhrnně. Minimální tabulka obsahuje:

| Pole | Význam |
|---|---|
| Reviewer ID | anonymní identifikátor hodnotitele |
| Varianta | BLIND-01 / BLIND-02 |
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

Kvalitativní komentáře se analyzují tematicky: práce se zdroji, metodologie, originalita, struktura, jazyk, důvěryhodnost dat, přiměřenost závěrů, vnímaná autorská přítomnost a rozpoznané znaky strojového vzniku.

Případné srovnání detektorových hodnot se prezentuje odděleně od známek. Shoda nebo neshoda těchto dvou vrstev je sama o sobě výsledkem.

## 11. Kritéria integrity experimentu

- Všichni hodnotitelé v rámci jedné větve designu dostanou stejnou zmrazenou verzi.
- Před odtajněním se jim neposkytují výsledky jiných hodnotitelů.
- Posudek se po odtajnění nemění.
- Syntetický pilot není prezentován jako empirický výzkum.
- Rukopis není vložen do STAG ani použit k získání titulu.
- `BLIND-01` zůstává neměnná baseline.
- U `BLIND-02` je auditována každá změna významu a každý lidský zásah.
- Záměrné chyby a technické obcházení detektorů nejsou součástí postupu.
- Veřejná prezentace výsledků musí uvést, že šlo o simulované odborné hodnocení, nikoli skutečné absolvování obhajoby.
- Negativní posudky, nedohledané chyby a selhání se publikují stejně jako úspěchy.

## 12. Hranice závěru

Ani jednoznačně pozitivní výsledek sám o sobě neprokazuje, že:

- LLM nahradilo osobní odborné porozumění studenta;
- stejný postup obstojí v jiném oboru nebo na jiné škole;
- artefakt projde ústní obhajobou;
- všechny zdrojové interpretace jsou bezchybné;
- současné školní předpisy umožňují konkrétnímu studentovi takový způsob použití AI;
- nízké detektorové skóre dokazuje lidské autorství;
- vysoké detektorové skóre dokazuje strojové autorství.

Výsledek `BLIND-01` vypovídá o méně redigovaném LLM-orientovaném artefaktu. Výsledek `BLIND-02` vypovídá o LLM workflow rozšířeném o explicitní autorskou redakci. Pokud část redakce provede člověk, musí být závěr formulován jako schopnost člověka vytvořit hodnotitelný rukopis s intenzivní podporou LLM, nikoli jako autonomní výkon modelu.

Experiment testuje kvalitu předloženého rukopisu a limity dokumentového hodnocení. Ověření autorova porozumění, detekce původu a legitimity konkrétního použití AI jsou samostatné otázky.
