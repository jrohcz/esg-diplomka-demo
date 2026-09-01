# STATUS — final merge audit

**Stav:** dokončeno 1. 9. 2026
**Větev:** `main`
**Cílové artefakty:** 19/19

## Ověření

- **CSV:** 7/7 souborů načteno Python `csv.reader(..., strict=True)`; všechny řádky mají stabilní počet sloupců.
- **Akademické zdroje:** 17/17 DOI v `sources/academic-sources.csv` znovu vyřešeno přes Crossref; všech 17 DOI uvedených v Markdown artefaktech je obsaženo v registru. Neplatný, necitovaný DOI z pracovní verze byl odstraněn.
- **Regulace:** statusy 2025/794, 2026/470, 2024/1760 a 2025/1416 ověřeny proti autentickému znění EUR-Lex. Přehled rozlišuje platnost aktu EU, jeho použitelnost, transpozici a návrhy. Registry doplněny o citované SFDR a ESPR.
- **Syntetická data:** varování je v README, na začátku datového i analytického souboru, u každého syntetického profilu a v každém řádku codebooku.
- **Konzistence:** osnova opravena na diplomovou práci; hlavní otázka a rozsah 12–16 rozhovorů sjednoceny s výzkumným kontraktem a metodologií.
- **Whitespace:** `git diff --cached --check` bez nálezu.

## Omezení / blocker

Žádný technický blocker pro merge a push. Před skutečným náborem respondentů zůstává věcně nutné potvrzení vedoucím/UJEP: finální zadání, etický a GDPR režim, citační styl a pravidla přiznání AI. Nejde o blocker tohoto demonstračního repozitáře.
