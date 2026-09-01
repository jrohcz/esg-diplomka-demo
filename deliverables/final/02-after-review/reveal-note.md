# Odtajnění produkčního procesu

> Tento dokument předat hodnotiteli až po uzavření známky, doporučení a původního odhadu autorství.

## Co bylo testováno

Experiment testoval, zda současný velký jazykový model dokáže pod lidským zadáním vytvořit kompletní a formálně hodnotitelný rukopis diplomové práce, který:

- vymezuje výzkumný problém a otázky;
- pracuje s dohledatelnou akademickou a regulatorní literaturou;
- používá skutečný, veřejně ověřitelný empirický korpus;
- provádí transparentní kvalitativní analýzu;
- odděluje firemní tvrzení, metriku, interpretaci a omezení;
- vytváří výsledky, diskusi a závěr;
- umožňuje nezávislou kontrolu každého klíčového tvrzení.

Nešlo o test, zda lze podvodně odevzdat práci za konkrétního studenta. Rukopis nebyl a nebude použit k získání titulu, neobsahuje falešné čestné prohlášení a v titulní části je označen jako experimentální artefakt pro odborné hodnocení.

## Způsob vzniku

Obsahová produkce rukopisu, návrh metodiky, kódovacího rámce, extrakce důkazních segmentů, syntéza, formulace kapitol a kontrolní dokumentace byly provedeny prostřednictvím velkého jazykového modelu **GPT-5.6 Pro** v rozhraní ChatGPT dne 1. září 2026.

Lidský iniciátor experimentu:

- formuloval výzkumný cíl;
- poskytl původní demonstrační repozitář;
- rozhodl o účelu nezávislého hodnocení;
- zajistil hodnotitele;
- nenahrazoval v průběhu této verze autora odborných pasáží ani analytika jednotlivých segmentů.

Model měl přístup k soukromému GitHub repozitáři prostřednictvím konektoru a k veřejnému webu. Produkce probíhala po souborech na samostatné větvi `experiment/complete-document-analysis`.

## Proč nebyly použity původní rozhovory

Výchozí demonstrační projekt obsahoval syntetické rozhovory. Ty byly výrazně označeny jako neempirické a sloužily pouze k testu workflow. Pro hodnotitelný rukopis nebyly použity jako výzkumná data.

Model změnil design na komparativní analýzu veřejných firemních dokumentů za rok 2024. Tím vznikl reálný a reprodukovatelný korpus bez fingovaného sběru dat. Analyzovány byly oficiální reporty ČEZ Group, MONETA Money Bank, O2 Czech Republic a Škoda Auto.

## Zdrojová a analytická kontrola

Korpus obsahuje 45 klíčových segmentů. U každého je uloženo:

- ID případu a dokumentu;
- přesný lokátor;
- neutrální parafráze;
- tematické kódy;
- evidenční třída E0–E4;
- status tvrzení;
- zamýšlené analytické použití;
- omezení nebo alternativní výklad.

Každé hlavní tvrzení rukopisu je napojeno na `audit/claim-evidence-ledger.csv`. Devět položek třídy E3/E4 prošlo samostatnou kontrolou hranice a originálního lokátoru. Desetiprocentní kontrolní vzorek byl znovu klasifikován bez původního hodnocení; jedna položka byla snížena z E3 na E2. Důvodem bylo zjištění, že omezené assurance nad celou zprávou samo o sobě nepředstavuje rozhodovací vazbu.

## Co kontrola zahrnovala

- ověření DOI a bibliografických metadat;
- práci s oficiálními firemními dokumenty;
- práci s primárními právními prameny EUR-Lex a českou legislativou;
- přesné stránkové nebo sekční lokátory;
- negativní případy a proti-důkazy;
- oddělení output, outcome a impact claimu;
- oddělení assurance od hloubky manažerské integrace;
- technickou kontrolu struktury, citací, tabulek a exportu.

## Co kontrola nezahrnovala

- přečtení všech citovaných akademických článků lidským odborníkem v plném textu;
- nezávislé opakování kódování druhým lidským analytikem;
- rozhovory se zaměstnanci, managementem, dodavateli nebo komunitami;
- ověření interních investičních dokumentů a skutečné praxe v provozu;
- skutečnou ústní obhajobu autorem-studentem;
- posouzení práce oficiální komisí nebo její podání do STAG.

Tato omezení jsou podstatná. Experiment dokládá schopnost modelu vytvořit auditovatelný akademický artefakt, nikoli nezávisle prokazuje pravdivost všech firemních tvrzení ani schopnost fiktivního studenta práci obhájit.

## Jak číst výsledek posudku

Vysoké hodnocení by ukazovalo, že samotný dokument může dosáhnout kvality, kterou zkušený hodnotitel považuje za obhajitelnou. Neprokazovalo by, že je přijatelné nahradit studentskou práci modelem nebo zatajit jeho použití.

Nízké hodnocení je třeba rozdělit podle příčin:

- nedostatek teorie nebo zdrojů;
- slabý či nevhodný design;
- malý nebo selektivní korpus;
- nedostatečná analýza;
- stylistická uniformita či opakování;
- chyby ve zdrojích;
- absence skutečné obhajoby;
- indicie strojového původu.

Největší vzdělávací hodnotu má konkrétní popis, které části obstály a které selhaly bez ohledu na původ textu.

## Otázky pro reflexi hodnotitele

1. Které části posudku by byly stejné, kdyby text napsal známý student?
2. Které indicie vedly k odhadu původu a byly skutečně spolehlivé?
3. Změnila informace o původu hodnocení odborné správnosti, nebo spíše hodnocení autorství a integrity?
4. Které kompetence lze ověřit pouze při průběžném vedení, práci se zdrojem nebo ústní obhajobě?
5. Co by měl vedoucí vyžadovat jako procesní důkaz vedle výsledného PDF?

## Hlavní pedagogická teze experimentu

Hotový text již nelze považovat za dostatečný důkaz toho, kdo vykonal intelektuální práci a čemu autor rozumí. To neznamená rezignovat na kvalifikační práce. Znamená to posílit průběžnou práci s rozhodnutími, zdrojovou stopou, verzemi, nečekanými daty a obhajobou.
