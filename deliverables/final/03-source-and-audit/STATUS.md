# STATUS — hodnoticí rukopis ESG diplomky

**Kanonický rukopis:** `ESG-DP-2026-REVIEW`  
**Stav:** dokončeno a připraveno k nezávislému hodnocení  
**Datum uzávěrky:** 2. 9. 2026

## Rukopis

- úplná struktura od českého a anglického abstraktu po závěr a seznam zdrojů;
- název: *Veřejně vykazovaná implementace ESG ve vybraných velkých podnicích působících v České republice*;
- komparativní kvalitativní analýza veřejných dokumentů;
- analyzované případy: ČEZ Group, MONETA Money Bank, O2 Czech Republic a Škoda Auto;
- historický syntetický pilot není součástí empirických výsledků;
- všechny narativní kapitoly prošly úplnou autorskou a jazykovou redakcí při zachování zdrojů, dat a metodických hranic;
- aktuální struktura obsahuje jediný kanonický rukopis, nikoli paralelní textové varianty.

## Datová a analytická kontrola

- **45** klíčových důkazních segmentů: ČEZ 11, MONETA 12, O2 11 a Škoda Auto 11;
- rozdělení tříd: **E0 = 1, E1 = 8, E2 = 27, E3 = 8, E4 = 1**;
- **31** hlavních tvrzení je napojeno na claim-evidence ledger;
- přibližně desetiprocentní stratifikovaný vzorek prošel kontrolním překódováním;
- jedna položka byla po kontrole snížena z E3 na E2, protože omezené ujištění celé zprávy samo nedokládalo rozhodovací vazbu;
- všech devět položek E3/E4 bylo znovu otevřeno a ověřeno proti originálnímu lokátoru, hranici a rozsahu tvrzení;
- každé výsledkové téma obsahuje mezipřípadový kontrast a proti-důkaz nebo interpretační hranici.

## Závěrečná redakce

První úplné sestavení bylo věcně soudržné, ale stylisticky příliš pravidelné. Proto byly úvod, teoretická a regulatorní část, metodologie, výsledky, diskuse, závěr i oba abstrakty znovu vystavěny po významových blocích.

Při redakci zůstaly uzamčeny výzkumné otázky, zdrojové kotvy a citace, číselné údaje, firemní lokátory, význam evidenčních tříd, rozsah assurance a hranice dokumentového designu.

Nebyla použita záměrná chybovost, synonymické přepisování, neviditelné znaky ani jiné technické zásahy. Pracovní redakční soubory a paralelní označení nejsou součástí aktuální struktury.

## Sestavení a technická kontrola

GitHub Actions úspěšně provedly datovou validaci, sestavení DOCX a PDF, aktualizaci obsahu, kontrolu klíčových částí a vytvoření všech archivů.

Kanonický rukopis má **71 stran A4**. Byla provedena vizuální kontrola všech stran finálního PDF i samostatného renderu DOCX. Kontrola zahrnovala titulní části, obsah, nadpisy, tabulky, zalomení, číslování, poznámky, seznam zdrojů a okraje. Nebyly nalezeny překryvy, useknutý text, rozpadlé znaky ani rozdělené řádky tabulek, které by bránily čtení.

Hodnoticí dokumenty používají jednotný identifikátor `ESG-DP-2026-REVIEW`. Finální PDF neobsahuje pracovní označení, názvy meziverzí ani produkční poznámky.

## Připravené výstupy

Kanonická struktura je `deliverables/final/`:

- `01-send-to-reviewers/` — rukopis v PDF a DOCX, pokyny, formulář, kontrolní součty a `ESG-DP-2026-REVIEW-PACKAGE.zip`;
- `02-after-review/` — odtajňovací zpráva a auditní archiv;
- `03-source-and-audit/` — úplný interní archiv sestavení, procesní dokumentace a zdrojový commit.

## Poslední organizační podmínka

Před rozesláním je nutné nastavit repozitář jako neveřejný a hodnotitelům neposílat jeho adresu. Hodnotitelé mají dostat pouze obsah `deliverables/final/01-send-to-reviewers/`.

## Etický status

Dokument je výzkumný artefakt pro nezávislé odborné hodnocení. Není podáván do STAG, neslouží k získání titulu a neobsahuje falešné čestné prohlášení ani identitu fiktivního studenta. Produkční proces bude hodnotitelům odtajněn až po uzavření původní známky a posudku.