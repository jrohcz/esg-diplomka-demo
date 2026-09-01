# Sestavení rukopisu

## Zaslepená hodnoticí verze

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

Zaslepená verze neobsahuje produkční audit ani informaci o konkrétním modelu. Titulní strana ji výslovně označuje jako experimentální rukopis, který není podáván k získání akademického titulu.

## Balíček pro hodnotitele

- `reviewer-packet/README.md` — instrukce před hodnocením;
- `reviewer-packet/evaluation-form.md` — posudkový formulář;
- `reviewer-packet/reveal-note.md` — předat až po uzamčení posudku.

## Reprodukční podklady

- `sources/corporate-documents.csv` — registr empirického korpusu;
- `data/document-corpus.csv` — první kolo důkazních segmentů;
- `analysis/document-codebook-v2.csv` — finální slovník;
- `analysis/coding-revisions.csv` — změny po kontrolním kódování;
- `analysis/control-coding.csv` — desetiprocentní kontrolní vzorek;
- `analysis/high-evidence-review.csv` — druhá kontrola E3/E4;
- `analysis/evidence-matrix.csv` — mezipřípadová matice;
- `analysis/case-memos.md` — případová mema;
- `audit/claim-evidence-ledger.csv` — vazba hlavních tvrzení na důkazy.

## Příkaz pro sestavení

Skript `scripts/build-manuscript.sh` používá Pandoc. Výsledné DOCX je vhodné následně otevřít v kancelářském editoru, aktualizovat obsah a zkontrolovat zalomení tabulek. PDF se vytváří z finálního DOCX, aby obě hodnoticí verze měly shodnou sazbu.

## Verze

Hodnotitelům vždy posílejte soubory se stejným identifikátorem verze. Posudek musí být uzavřen před otevřením `reviewer-packet/reveal-note.md` nebo historie repozitáře.
