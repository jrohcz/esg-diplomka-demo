# Sestavení rukopisu

## Kanonická hodnoticí verze

Identifikátor finálního rukopisu je `ESG-DP-2026-REVIEW`.

Pořadí zdrojových souborů:

1. `chapters/front-matter.md`
2. `chapters/00-introduction.md`
3. `chapters/01-theoretical-framework.md`
4. `chapters/02-regulatory-context.md`
5. `chapters/03-methodology.md`
6. `chapters/04-results.md`
7. `chapters/05-discussion.md`
8. `chapters/06-conclusion.md`
9. `chapters/references.md`

Hodnoticí dokument neobsahuje produkční audit ani informaci o konkrétním modelu. Titulní strana jej výslovně označuje jako experimentální rukopis, který není podáván k získání akademického titulu.

## Balíček pro hodnotitele

- `reviewer-packet/README.md` — instrukce před hodnocením;
- `reviewer-packet/evaluation-form.md` — posudkový formulář;
- `reviewer-packet/reveal-note.md` — předat až po uzavření původního posudku.

Hotové soubory se publikují do:

- `deliverables/final/01-send-to-reviewers/`;
- `deliverables/final/02-after-review/`;
- `deliverables/final/03-source-and-audit/`.

## Reprodukční podklady

- `sources/corporate-documents.csv` — registr empirického korpusu;
- `data/document-corpus.csv` — důkazní segmenty;
- `analysis/document-codebook-v2.csv` — finální slovník;
- `analysis/coding-revisions.csv` — změny po kontrolním kódování;
- `analysis/control-coding.csv` — kontrolní vzorek;
- `analysis/high-evidence-review.csv` — druhá kontrola E3/E4;
- `analysis/evidence-matrix.csv` — mezipřípadová matice;
- `analysis/case-memos.md` — případová mema;
- `audit/claim-evidence-ledger.csv` — vazba hlavních tvrzení na důkazy.

## Příkaz pro sestavení

```bash
bash scripts/build-manuscript.sh
```

Skript nejprve spustí datovou a strukturální validaci, následně vytvoří formátované DOCX dokumenty, aktualizuje obsah pomocí LibreOffice a exportuje PDF. GitHub workflow navíc připraví ZIP balíčky, kontrolní součty a publikuje jedinou kanonickou sadu výstupů do `deliverables/final/`.

## Pravidlo rozesílání

Hodnotitelům vždy posílejte pouze obsah `01-send-to-reviewers` se shodným identifikátorem a kontrolním součtem. Posudek musí být uzavřen před otevřením `reviewer-packet/reveal-note.md`, auditních souborů nebo historie repozitáře.