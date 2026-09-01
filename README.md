# ESG diplomka — demonstrační projekt

> **DEMONSTRAČNÍ PROJEKT, NIKOLI HOTOVÁ DIPLOMOVÁ PRÁCE.** Soubory v `data/` a `analysis/` označené jako syntetické obsahují výhradně uměle vytvořená data. Neproběhl žádný rozhovor a syntetický pilot nesmí být prezentován jako empirický výsledek.

Demonstrační výzkumný projekt k tématu:

> **Implementace ESG principů v českých podnicích: motivace, bariéry a vnímané přínosy v období regulatorní změny**

FSE UJEP · Ekonomika a management veřejného sektoru.

Projekt ukazuje transparentní proces: výzkumný kontrakt, ověřené akademické a regulatorní zdroje, metodologii rozhovorů, šablony evidence, syntetický pilot, analýzu a audit využití AI. Není určen k odevzdání jako studentská práce; školní, etické, GDPR a citační požadavky musí před empirickou fází potvrdit vedoucí a UJEP.

## Stav k 1. 9. 2026

- všech **19 cílových artefaktů** existuje;
- akademický registr obsahuje **17/17 DOI ověřených přes Crossref**;
- regulatorní přehled rozlišuje účinné právo EU, transpozici, delegovaný akt a návrh;
- všech 7 CSV souborů prochází striktním Python `csv` parserem se stabilním počtem sloupců;
- syntetická data a syntetická analýza jsou výrazně označeny a odděleny od budoucího empirického korpusu;
- úplný merge audit je v [`STATUS.md`](STATUS.md).

## Artefakty

### Návrh a metodologie

- `notes/research-contract.md`
- `notes/thesis-outline.md`
- `notes/methodology.md`
- `notes/literature-map.md`
- `notes/esg-regulatory-czech-2026.md`
- `notes/ujep-requirements.md`
- `notes/ai-workflow-and-audit.md`

### Zdroje

- `sources/academic-sources.csv`
- `sources/regulatory-sources.csv`
- `sources/ujep-sources.csv`

### Výzkumné šablony

- `templates/interview-guide.md`
- `templates/consent-and-information-sheet.md`
- `templates/respondent-matrix.csv`
- `templates/evidence-ledger.csv`
- `audit/ai-use-log-template.csv`

### Demonstrační kapitola a syntetický pilot

- `chapters/01-theoretical-framework-demo.md`
- `data/synthetic-pilot-interviews.md` — **SYNTHETICKÁ / NE EMPIRICKÁ DATA**
- `analysis/codebook-v1.csv` — **KÓDOVÁNÍ SYNTHETICKÉHO PILOTU**
- `analysis/synthetic-pilot-analysis.md` — **SYNTHETICKÁ / NE EMPIRICKÁ ANALÝZA**

## Kritická omezení

1. Metadata a DOI nenahrazují četbu plných textů a kontrolu konkrétních tvrzení proti stranám originálu.
2. Právní závěr pro konkrétní českou firmu vyžaduje aktuální konsolidované právo, českou transpozici a individuální posouzení.
3. Šablony souhlasu a GDPR jsou pracovní; před náborem je musí potvrdit správce údajů / UJEP.
4. Syntetický pilot testuje proces, nikoli realitu českých podniků.
