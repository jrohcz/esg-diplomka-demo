# ESG diplomka — experimentální hodnoticí rukopis

> **VÝZKUMNÝ ARTEFAKT, NIKOLI SKUTEČNĚ ODEVZDÁVANÁ DIPLOMOVÁ PRÁCE.**
>
> Projekt testuje, zda současný velký jazykový model dokáže vytvořit úplný, auditovatelný a odborně hodnotitelný rukopis. Neusiluje o získání akademického titulu, neobsahuje falešné čestné prohlášení a nesmí být vydáván za práci konkrétního studenta.

## Název rukopisu

**Veřejně vykazovaná implementace ESG ve vybraných velkých podnicích působících v České republice**

Výzkum používá komparativní kvalitativní analýzu oficiálních firemních reportů za rok 2024. Původní syntetický rozhovorový pilot zůstává v repozitáři pouze jako historický demonstrační materiál a **není použit v empirické části finálního rukopisu**.

## Stav

- úplný text od abstraktu po závěr;
- čtyři kontrastní případy: ČEZ Group, MONETA Money Bank, O2 Czech Republic a Škoda Auto;
- 45 klíčových důkazních segmentů s přesnými lokátory;
- finální kódovací slovník E0–E4;
- případová mema a mezipřípadová evidenční matice;
- desetiprocentní kontrolní kódování;
- druhá kontrola všech devíti položek E3/E4;
- claim-evidence ledger pro hlavní tvrzení rukopisu;
- zaslepené pokyny a formulář pro nezávislé hodnotitele;
- samostatná odtajňovací zpráva o produkčním procesu;
- deterministický validační skript.

## Rukopis

Pořadí zdrojových kapitol je uvedeno v [`thesis/README.md`](thesis/README.md):

- `chapters/front-matter.md`
- `chapters/00-introduction.md`
- `chapters/01-theoretical-framework.md`
- `chapters/02-regulatory-context.md`
- `chapters/03-methodology.md`
- `chapters/04-results.md`
- `chapters/05-discussion.md`
- `chapters/06-conclusion.md`
- `chapters/references.md`

Sestavení DOCX podporuje `scripts/build-manuscript.sh`.

## Empirický a analytický audit

- `sources/corporate-documents.csv` — registr firemních dokumentů;
- `data/document-corpus.csv` — první kolo důkazních segmentů;
- `analysis/document-codebook-v2.csv` — finální slovník;
- `analysis/coding-revisions.csv` — změny po kontrole;
- `analysis/control-coding.csv` — kontrolní vzorek;
- `analysis/high-evidence-review.csv` — kontrola E3/E4;
- `analysis/evidence-matrix.csv` — mezipřípadová syntéza;
- `analysis/case-memos.md` — vnitropřípadové interpretace;
- `audit/claim-evidence-ledger.csv` — vazba tvrzení na důkazy.

## Balíček pro hodnotitele

- [`reviewer-packet/README.md`](reviewer-packet/README.md) — podmínky zaslepení;
- [`reviewer-packet/evaluation-form.md`](reviewer-packet/evaluation-form.md) — posudkový formulář;
- [`reviewer-packet/reveal-note.md`](reviewer-packet/reveal-note.md) — předat až po uzavření známky.

## Hlavní metodické pravidlo

Jednotkou hodnocení není firma, ale konkrétní tvrzení. Škála rozlišuje:

- **E0:** deklarace;
- **E1:** aktivita nebo výstup;
- **E2:** formalizovaný proces nebo řízený výsledek;
- **E3:** vazba na kapitál, riziko, produkt, dodavatele, odměnu nebo provoz;
- **E4:** přesně vymezený výsledek se silnou externí podporou.

Assurance je evidováno samostatně. Externě ověřená zpráva není automaticky důkazem manažerské integrace ani skutečného dopadu.

## Validace

```bash
python scripts/validate-manuscript.py
bash scripts/build-manuscript.sh
```

Validátor kontroluje strukturu CSV, počet a distribuci segmentů, pokrytí kontroly E3/E4, claim ledger a to, že finální empirický text necituje syntetický pilot.

## Kritická omezení

1. Firemní report je oficiální sebeprezentace, nikoli nezávislý audit provozu.
2. Čtyři velké podniky nejsou reprezentativním vzorkem české ekonomiky.
3. Analýza hodnotí reporty za rok 2024; pozdější právní a organizační změny nejsou zpětně promítány.
4. Dokumentový design neověřuje zkušenost zaměstnanců, dodavatelů, zákazníků ani komunit.
5. Vysoká třída důkazu u konkrétního segmentu není celkovým ESG ratingem firmy.
6. Skutečná schopnost autora práci obhájit vyžaduje samostatný experiment.
