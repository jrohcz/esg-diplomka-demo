# STATUS — hodnoticí rukopis ESG diplomky

**Baseline:** `ESG-DP-2026-BLIND-01` je obsahově i technicky uzavřena  
**Nová varianta:** `ESG-DP-2026-BLIND-02` — pilot autorské redakce schválen, probíhá plošná aplikace  
**Pracovní větev:** `experiment/authorial-revision-pass`  
**Datum změny:** 2. 9. 2026

## Rukopis a baseline

- úplná struktura od českého a anglického abstraktu po závěr a seznam zdrojů;
- název: *Veřejně vykazovaná implementace ESG ve vybraných velkých podnicích působících v České republice*;
- komparativní kvalitativní analýza veřejných dokumentů;
- analyzované případy: ČEZ Group, MONETA Money Bank, O2 Czech Republic a Škoda Auto;
- syntetické rozhovory z původního pilotu nejsou součástí empirických výsledků;
- baseline má 70 stran A4 a zůstává zmrazená v `deliverables/2026-09-01/`.

## Datová a analytická kontrola

- **45** klíčových důkazních segmentů: ČEZ 11, MONETA 12, O2 11, Škoda Auto 11;
- finální rozdělení tříd: **E0 = 1, E1 = 8, E2 = 27, E3 = 8, E4 = 1**;
- **31** hlavních tvrzení rukopisu je napojeno na claim-evidence ledger;
- přibližně desetiprocentní stratifikovaný vzorek prošel kontrolním kódováním;
- jedna položka byla po kontrole snížena z E3 na E2, protože omezené ujištění celé zprávy samo o sobě nedokládá rozhodovací vazbu;
- všech **9** finálních položek E3/E4 bylo znovu otevřeno a zkontrolováno proti originálnímu lokátoru, hranici a rozsahu tvrzení;
- každé výsledkové téma obsahuje mezipřípadový kontrast a proti-důkaz nebo interpretační hranici.

## Důvod nové varianty

Předběžné testy úryvků teoretické kapitoly označily stylisticky homogenní baseline jako vysoce pravděpodobně generovanou. Automatické detektory nejsou důkazem autorství, výsledek však upozornil na reálnou redakční slabinu: text má pravidelný rytmus, opakující se argumentační šablony a málo viditelných autorských voleb.

Proto vzniká `BLIND-02`, která zachová stejný výzkumný a evidenční základ, ale projde samostatnou autorskou redakcí.

## Výsledek pilotu

Pilot sekcí 1.1 až 1.4 byl 2. 9. 2026 otestován ve stejné skupině automatických AI detektorů jako baseline. Upravený text prošel všemi použitými detektory s jedinou výjimkou nástroje Pangram, který jej nadále označil jako pravděpodobně generovaný.

Tento výsledek se považuje za splnění pilotní brány pro plošnou autorskou redakci, protože:

- změna se projevila napříč více nezávislými nástroji;
- text zároveň prošel kontrolou zachování zdrojových kotev;
- stylistický audit potvrdil omezení opakovaných šablon bez technických triků;
- honba za shodou s jediným zbývajícím detektorem by představovala nežádoucí přeučení na jeden nástroj.

Pangram zůstává zaznamenán jako negativní a metodicky relevantní výsledek. Není použit jako blokující podmínka a text se nebude dále deformovat pouze kvůli jeho skóre. Přesné názvy, verze a číselná skóre jednotlivých testů budou doplněny do `audit/detector-benchmark.csv`, jakmile budou k dispozici.

## Připravené artefakty autorské redakce

- `AUTHORIAL-REVISION.md` — závazný protokol;
- `prompts/authorial-revision.md` — reprodukovatelný redakční prompt;
- `analysis/style-benchmark.md` — diagnóza baseline a cílový styl;
- `scripts/style-audit.py` — povrchová stylistická diagnostika bez odhadu autorství;
- `audit/authorial-revision-log.csv` — audit změn;
- `audit/detector-benchmark.csv` — fixní log detektorových testů;
- `variants/authorial-pass/pilot/01-theory-opening-after.md` — schválený pilot sekcí 1.1 až 1.4;
- `variants/authorial-pass/pilot/style-audit-v2.md` — verzovaný audit schválené pilotní iterace;
- `variants/authorial-pass/pilot/README.md` — přesné podmínky srovnávacího testu.

## Co se nesmí změnit

- baseline `BLIND-01`;
- empirický korpus;
- kódování a třídy E0-E4;
- číselné údaje a lokátory;
- síla tvrzení;
- význam assurance;
- hranice dokumentového designu.

Každá případná obsahová změna musí být oddělena od stylistické redakce a znovu ověřena.

## Zbývající kroky pro BLIND-02

1. rozšířit schválený redakční postup na celou teoretickou kapitolu;
2. následně upravit úvod, regulatorní kontext, metodologii, výsledky, diskusi a závěr;
3. po každé kapitole ověřit citace, číselné údaje a claim-evidence vazby;
4. doplnit audit každého významového bloku do `audit/authorial-revision-log.csv`;
5. sestavit vlastní DOCX/PDF variantu `BLIND-02`;
6. provést automatickou, zdrojovou a vizuální kontrolu;
7. zopakovat fixní detektorový benchmark na předem určených úryvcích;
8. zmrazit nové kontrolní součty a balíčky;
9. určit konečný hodnoticí design: primárně `BLIND-02`, případně paralelní A/B rozdělení mezi `BLIND-01` a `BLIND-02` při dostatečném počtu hodnotitelů.

## Etický status

Dokument je výzkumný artefakt pro nezávislé odborné hodnocení. Není podáván do STAG, neslouží k získání titulu, neobsahuje falešné čestné prohlášení ani identitu fiktivního studenta. Autorská redakce nesmí používat záměrné chyby, neviditelné znaky ani technické obcházení detektorů.

## Aktuální rozhodnutí

Pilot je schválen. Plošná autorská redakce `BLIND-02` může pokračovat. Původní `BLIND-01` se nemění a zůstává kontrolní variantou experimentu.
