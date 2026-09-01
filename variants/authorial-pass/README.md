# Varianta ESG-DP-2026-BLIND-02 — autorská redakce

Tato složka obsahuje připravovanou variantu rukopisu po závěrečném authorial revision passu. Původní `ESG-DP-2026-BLIND-01` zůstává zmrazený v `deliverables/2026-09-01/` a nesmí být přepsán.

## Stav

- [x] protokol autorské redakce;
- [x] redakční prompt;
- [x] stylová diagnóza baseline;
- [x] auditní logy;
- [ ] pilotní přepis fixního úryvku teorie;
- [ ] opakovaný detektorový benchmark;
- [ ] rozhodnutí o cílovém stylu;
- [ ] redakce všech kapitol;
- [ ] úplná zdrojová kontrola;
- [ ] build DOCX/PDF;
- [ ] vizuální kontrola;
- [ ] zmrazení `BLIND-02`.

## Adresářová logika

- `chapters/` — redigované kapitoly, které po dokončení nahradí pouze zdroj vstupující do buildu varianty BLIND-02;
- `pilot/` — krátké iterace pro porovnání stejného úryvku před a po redakci;
- kořenový `AUTHORIAL-REVISION.md` — závazný proces;
- `audit/authorial-revision-log.csv` — co, kým a proč bylo změněno;
- `audit/detector-benchmark.csv` — vedlejší výsledky fixních testů.

## Build

Dokud nejsou redigovány všechny kapitoly, standardní build stále sestavuje BLIND-01. Po dokončení varianty vznikne explicitní parametr nebo samostatný build skript; nesmí dojít k tichému přesměrování stávajícího workflow.

## Terminologie

V interní zkratce lze mluvit o „humanizeru“. Ve veřejném popisu se používá **autorská redakce**. Nejde o vložení chyb ani o technické obcházení detektorů, ale o opětovné vystavění argumentu při zachování dat a důkazů.
