# Deliverables

Tato složka obsahuje jedinou kanonickou sadu hotových výstupů experimentu:

[`final/`](final/)

Její podadresáře oddělují:

1. `01-send-to-reviewers/` — rukopis, pokyny, hodnoticí formulář a společný ZIP k prvnímu rozeslání;
2. `02-after-review/` — odtajňovací a auditní balíček, který se předává až po uzavření posudku;
3. `03-source-and-audit/` — úplný interní archiv sestavení a procesní dokumentace.

Obsah `final/` generuje a kontroluje `.github/workflows/build-review-package.yml`. Binární soubory se neupravují ručně; správný postup je změnit zdrojové kapitoly nebo skripty a znovu spustit build.

Starší pracovní výstupy a paralelní označení rukopisu nejsou součástí aktuální struktury.