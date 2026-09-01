# ESG diplomka — experimentální hodnoticí rukopis

> **VÝZKUMNÝ ARTEFAKT, NIKOLI SKUTEČNĚ ODEVZDÁVANÁ DIPLOMOVÁ PRÁCE.**
>
> Projekt testuje, zda současný LLM-orientovaný workflow dokáže vytvořit úplný, auditovatelný a odborně hodnotitelný rukopis. Neusiluje o získání akademického titulu, neobsahuje falešné čestné prohlášení a nesmí být vydáván za práci konkrétního studenta.

## Rychlý vstup

- **Co poslat hodnotitelům:** [`deliverables/2026-09-01/01-send-to-reviewers/`](deliverables/2026-09-01/01-send-to-reviewers/)
- **Co předat až po uzavření posudku:** [`deliverables/2026-09-01/02-after-review/`](deliverables/2026-09-01/02-after-review/)
- **Úplný archiv verze:** [`deliverables/2026-09-01/03-complete-build/`](deliverables/2026-09-01/03-complete-build/)
- **Celý postup a mapa souborů:** [`PROCESS.md`](PROCESS.md)
- **Design zaslepeného experimentu:** [`EXPERIMENT-DESIGN.md`](EXPERIMENT-DESIGN.md)
- **Aktuální stav a omezení:** [`STATUS.md`](STATUS.md)

GitHub je soukromý pracovní archiv. Hodnotitelům se neposílá přístup do repozitáře, protože obsahuje i odtajňovací a auditní vrstvu.

## Název rukopisu

**Veřejně vykazovaná implementace ESG ve vybraných velkých podnicích působících v České republice**

Výzkum používá komparativní kvalitativní analýzu oficiálních firemních reportů za rok 2024. Původní syntetický rozhovorový pilot zůstává v repozitáři pouze jako historický demonstrační materiál a **není použit v empirické části finálního rukopisu**.

## Stav finální verze

- úplný rukopis od českého a anglického abstraktu po závěr;
- 70 stran A4 v hodnoticí verzi;
- čtyři kontrastní případy: ČEZ Group, MONETA Money Bank, O2 Czech Republic a Škoda Auto;
- 45 klíčových důkazních segmentů s přesnými lokátory;
- finální kódovací slovník E0–E4;
- případová mema a mezipřípadová evidenční matice;
- desetiprocentní kontrolní kódování;
- druhá kontrola všech devíti položek E3/E4;
- claim-evidence ledger pro 31 hlavních tvrzení rukopisu;
- zaslepené pokyny a strukturovaný formulář pro nezávislé hodnotitele;
- samostatná odtajňovací zpráva;
- reprodukovatelná validace, sazba do DOCX/PDF a automatizovaný release.

## Struktura repozitáře

| Cesta | Obsah |
|---|---|
| `deliverables/2026-09-01/` | zmrazené soubory připravené k použití |
| `chapters/` | zdrojový rukopis po kapitolách |
| `sources/` | akademické, regulatorní a firemní zdrojové registry |
| `data/` | empirický dokumentový korpus a historický syntetický pilot |
| `analysis/` | codebooky, kontroly, případová mema a evidenční matice |
| `audit/` | vazba hlavních tvrzení na důkazy a AI auditní šablona |
| `notes/` | výzkumný kontrakt, metodika, osnova, literatura a regulatorní poznámky |
| `reviewer-packet/` | zdrojové pokyny, hodnoticí formulář a odtajnění |
| `scripts/` | validační, build a exportní nástroje |
| `.github/workflows/` | automatické sestavení, kontrola a publikace zmrazených výstupů |
| `thesis/README.md` | pořadí kapitol a sestavení rukopisu |

## Hlavní metodické pravidlo

Jednotkou hodnocení není firma, ale konkrétní tvrzení. Škála rozlišuje:

- **E0:** deklarace;
- **E1:** aktivita nebo výstup;
- **E2:** formalizovaný proces nebo řízený výsledek;
- **E3:** vazba na kapitál, riziko, produkt, dodavatele, odměnu nebo provoz;
- **E4:** přesně vymezený výsledek se silnou externí podporou.

Assurance je evidováno samostatně. Externě ověřená zpráva není automaticky důkazem manažerské integrace ani skutečného dopadu.

## Reprodukce

```bash
python scripts/validate-manuscript.py
bash scripts/build-manuscript.sh
```

GitHub Actions po úspěšné validaci vytvoří DOCX, PDF, předhodnoticí ZIP, odtajňovací ZIP, kontrolní součty a uloží zmrazené výstupy do `deliverables/2026-09-01/`.

## Jak provést hodnocení

1. Hodnotiteli poslat pouze obsah `01-send-to-reviewers` nebo ZIP v této složce.
2. Nechat jej uzavřít známku, doporučení k obhajobě a věcný posudek.
3. Teprve potom vyžádat odhad způsobu vzniku textu.
4. Zachovat původní posudek beze změny.
5. Následně předat obsah `02-after-review` a zaznamenat oddělenou reflexi po odtajnění.

Podrobnosti jsou v [`PROCESS.md`](PROCESS.md) a [`reviewer-packet/README.md`](reviewer-packet/README.md).

## Kritická omezení

1. Firemní report je oficiální sebeprezentace, nikoli nezávislý audit provozu.
2. Čtyři velké podniky nejsou reprezentativním vzorkem české ekonomiky.
3. Analýza hodnotí reporty za rok 2024; pozdější změny nejsou zpětně promítány.
4. Dokumentový design neověřuje zkušenost zaměstnanců, dodavatelů, zákazníků ani komunit.
5. Vysoká třída důkazu u konkrétního segmentu není celkovým ESG ratingem firmy.
6. Skutečná schopnost člověka rukopis obhájit vyžaduje samostatný experiment.
7. Pozitivní známka neznamená, že konkrétní použití AI studentem dovolují pravidla jeho školy.
