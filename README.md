# ESG diplomka — experimentální hodnoticí rukopis

> **VÝZKUMNÝ ARTEFAKT, NIKOLI SKUTEČNĚ ODEVZDÁVANÁ DIPLOMOVÁ PRÁCE.**
>
> Projekt testuje, zda workflow založené převážně na současném velkém jazykovém modelu dokáže vytvořit úplný, auditovatelný a odborně hodnotitelný rukopis. Neusiluje o získání akademického titulu, neobsahuje falešné čestné prohlášení a nesmí být vydáván za práci konkrétního studenta.

## Rychlý vstup

- **Co poslat hodnotitelům:** [`deliverables/final/01-send-to-reviewers/`](deliverables/final/01-send-to-reviewers/)
- **Co předat až po uzavření posudku:** [`deliverables/final/02-after-review/`](deliverables/final/02-after-review/)
- **Úplný interní archiv:** [`deliverables/final/03-source-and-audit/`](deliverables/final/03-source-and-audit/)
- **Celý postup a mapa souborů:** [`PROCESS.md`](PROCESS.md)
- **Design zaslepeného experimentu:** [`EXPERIMENT-DESIGN.md`](EXPERIMENT-DESIGN.md)
- **Aktuální stav a omezení:** [`STATUS.md`](STATUS.md)

Hodnotitelům se neposílá přístup do repozitáře. Obsahuje produkční historii, auditní vrstvu a odtajňovací materiály, které by před uzavřením posudku ovlivnily zaslepení.

## Hodnocený rukopis

**Název:** *Veřejně vykazovaná implementace ESG ve vybraných velkých podnicích působících v České republice*  
**Identifikátor:** `ESG-DP-2026-REVIEW`

Práce používá komparativní kvalitativní analýzu oficiálních firemních reportů za rok 2024. Analyzuje ČEZ Group, MONETA Money Bank, O2 Czech Republic a Škoda Auto. Původní rozhovorový návrh byl během vývoje opuštěn; syntetický demonstrační materiál není součástí empirického korpusu ani výsledků rukopisu.

## Stav

- úplný text od českého a anglického abstraktu po závěr a seznam zdrojů;
- kompletní závěrečná autorská a jazyková redakce všech narativních kapitol;
- 45 klíčových důkazních segmentů s přesnými lokátory;
- finální kódovací slovník E0–E4;
- případová mema a mezipřípadová evidenční matice;
- kontrolní překódování přibližně deseti procent korpusu;
- druhá kontrola všech devíti položek E3/E4;
- claim-evidence ledger pro 31 hlavních tvrzení;
- pokyny a strukturovaný formulář pro nezávislé hodnotitele;
- samostatná odtajňovací zpráva;
- reprodukovatelná validace, sazba do DOCX/PDF a automatizované sestavení balíčků.

## Struktura repozitáře

| Cesta | Obsah |
|---|---|
| `deliverables/final/` | jediná kanonická sada hotových výstupů |
| `chapters/` | zdrojový rukopis po kapitolách |
| `sources/` | akademické, regulatorní a firemní zdrojové registry |
| `data/` | empirický dokumentový korpus a oddělený historický demonstrační materiál |
| `analysis/` | kódovací rámce, kontroly, případová mema a evidenční matice |
| `audit/` | claim-evidence ledger a produkční auditní podklady |
| `notes/` | výzkumný kontrakt, metodika, osnova, literatura a regulatorní poznámky |
| `reviewer-packet/` | pokyny, hodnoticí formulář a odtajnění |
| `scripts/` | validační, sazební a exportní nástroje |
| `.github/workflows/` | automatické sestavení, kontrola a publikace finálních výstupů |
| `thesis/README.md` | pořadí kapitol a způsob sestavení rukopisu |

## Hlavní metodické pravidlo

Jednotkou hodnocení není firma, ale konkrétní tvrzení. Škála rozlišuje:

- **E0:** deklaraci;
- **E1:** aktivitu nebo výstup;
- **E2:** formalizovaný proces nebo řízený výsledek;
- **E3:** vazbu na kapitál, riziko, produkt, dodavatele, odměnu nebo provoz;
- **E4:** přesně vymezený výsledek se silnou externí podporou.

Assurance je evidováno samostatně. Externě ověřená zpráva není automaticky důkazem manažerské integrace ani skutečného dopadu.

## Sestavení

```bash
python scripts/validate-manuscript.py
bash scripts/build-manuscript.sh
```

Úspěšný build vytvoří kanonický rukopis `ESG-DP-2026-REVIEW` v DOCX a PDF, hodnoticí dokumenty, balíček k prvnímu rozeslání, samostatný odtajňovací archiv a kontrolní součty. GitHub Actions uloží hotové soubory do `deliverables/final/`.

## Postup hodnocení

1. Hodnotiteli poslat pouze ZIP nebo jednotlivé soubory ze složky `01-send-to-reviewers`.
2. Nechat jej uzavřít známku, doporučení k obhajobě a věcný posudek.
3. Teprve potom zaznamenat odhad způsobu vzniku textu.
4. Původní posudek archivovat beze změny.
5. Následně předat obsah `02-after-review` a případnou změnu názoru zachytit jako samostatnou reflexi.

Podrobnosti jsou v [`PROCESS.md`](PROCESS.md) a [`reviewer-packet/README.md`](reviewer-packet/README.md).

## Kritická omezení

1. Firemní report je oficiální sebeprezentace, nikoli nezávislý audit provozu.
2. Čtyři velké podniky nejsou reprezentativním vzorkem české ekonomiky.
3. Analýza hodnotí dokumenty za rok 2024; pozdější změny se do nich nepromítají zpětně.
4. Dokumentový design neověřuje zkušenost zaměstnanců, dodavatelů, zákazníků ani komunit.
5. Vysoká třída důkazu u konkrétního segmentu není celkovým ESG ratingem firmy.
6. Schopnost konkrétního člověka rukopis ústně obhájit vyžaduje samostatný test.
7. Pozitivní známka artefaktu sama neznamená, že obdobný způsob použití generativních nástrojů dovolují pravidla konkrétní školy.