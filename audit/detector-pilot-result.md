# Výsledek detektorového pilotu autorské redakce

**Datum hlášení:** 2. 9. 2026  
**Varianta:** `ESG-DP-2026-BLIND-02`  
**Úryvek:** teoretická kapitola, sekce 1.1 až 1.4  
**Zdroj výsledku:** manuální test operátora ve skupině veřejně dostupných AI detektorů

## Hlášený výsledek

Upravený pilotní úryvek prošel všemi použitými AI detektory s jedinou výjimkou nástroje **Pangram**, který jej nadále označil jako pravděpodobně generovaný.

Přesné názvy ostatních nástrojů, jejich verze, číselná skóre a případné opakované běhy nebyly při prvním zápisu dodány. Po jejich doplnění budou jednotlivé výsledky vloženy do `audit/detector-benchmark.csv`. Tento dokument proto zachycuje pouze kvalitativní rozhodovací bod, nikoli úplný benchmark.

## Rozhodnutí

Pilotní brána se považuje za splněnou a schválený redakční postup lze aplikovat na celý rukopis `BLIND-02`.

Pangram je ponechán jako negativní výsledek a metodicky důležitá výjimka. Není blokující podmínkou, protože:

1. změna se projevila napříč více dalšími nástroji;
2. pilot zachoval požadované zdrojové kotvy;
3. automatický stylový audit neukázal použití technických triků ani mechanického synonymického přepisu;
4. další optimalizace výhradně vůči jednomu detektoru by zvyšovala riziko přeučení na konkrétní proprietární klasifikátor a mohla by zhoršit akademickou kvalitu textu.

## Omezení interpretace

Výsledek neprokazuje lidské autorství ani spolehlivost jednotlivých detektorů. Ukazuje pouze to, že závěrečná autorská redakce významně změnila povrchový styl textu způsobem, který většina použitých nástrojů vyhodnotila odlišně od baseline.

Detektorový benchmark zůstává sekundární metrikou. Primárními podmínkami přijetí `BLIND-02` jsou zachování významu, citací, dat, evidenčních hranic a odborné čitelnosti.
