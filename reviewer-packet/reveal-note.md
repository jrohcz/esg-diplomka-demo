# Odtajnění produkčního procesu

> Tento dokument předat hodnotiteli až po uzavření známky, doporučení k obhajobě a původního odhadu způsobu vzniku.

## Co bylo testováno

Experiment ověřuje, zda workflow založené převážně na současném velkém jazykovém modelu dokáže pod lidským zadáním vytvořit kompletní a odborně hodnotitelný rukopis diplomové práce, který:

- vymezuje výzkumný problém a otázky;
- pracuje s dohledatelnou akademickou a regulatorní literaturou;
- používá skutečný, veřejně ověřitelný empirický korpus;
- provádí transparentní kvalitativní analýzu;
- odděluje firemní tvrzení, metriku, interpretaci a omezení;
- vytváří výsledky, diskusi a závěr;
- umožňuje kontrolovat hlavní tvrzení proti evidenčnímu základu;
- po úplné redakci působí jako soudržný akademický text, nikoli jako soubor izolovaných modelových výstupů.

Nešlo o pokus získat akademický titul nebo vydávat rukopis za práci konkrétního studenta. Dokument nebyl vložen do STAG, neobsahuje falešné čestné prohlášení a na titulní straně je označen jako experimentální artefakt pro odborné hodnocení.

## Způsob vzniku

Hlavní produkční práci provedl model **GPT-5.6 Pro** v rozhraní ChatGPT během 1. a 2. září 2026. Model se podílel na:

- zpřesnění výzkumného problému;
- změně výzkumného designu;
- rešerši a registraci zdrojů;
- konstrukci dokumentového korpusu;
- návrhu kódovacího rámce;
- klasifikaci a syntéze důkazních segmentů;
- formulaci kapitol;
- tvorbě kontrolních a auditních souborů;
- programování validačního a sazebního workflow;
- závěrečné autorské a jazykové redakci celého rukopisu.

Lidský iniciátor experimentu:

- určil praktický cíl testu;
- poskytl původní projekt a průběžnou zpětnou vazbu;
- rozhodl, že práce bude posuzována nezávislými vedoucími závěrečných prací;
- odmítl použití fingovaných rozhovorů jako empirických dat;
- porovnal styl prvního úplného sestavení s reálnou diplomovou prací;
- provedl orientační test vybraného úryvku v několika automatických detektorech;
- schválil závěrečnou redakci a zajistil hodnotitele.

Model pracoval s repozitářem prostřednictvím GitHub konektoru a s veřejnými zdroji prostřednictvím webového vyhledávání. Pracovní historie je zachována v systému verzování, zatímco hodnotitelé dostali pouze jeden kanonický rukopis `ESG-DP-2026-REVIEW`.

## Změna proti původnímu návrhu

Výchozí demonstrační projekt počítal s rozhovorovým výzkumem a obsahoval výrazně označený syntetický pilot. Takový materiál nebyl použit jako empirický výsledek. Design byl změněn na komparativní analýzu veřejných firemních dokumentů za rok 2024, čímž vznikl reálný a znovu dohledatelný korpus bez fingovaného sběru dat.

Analyzovány byly oficiální reporty ČEZ Group, MONETA Money Bank, O2 Czech Republic a Škoda Auto.

## Závěrečná redakce

První úplné sestavení bylo obsahově soudržné, ale vykazovalo příliš pravidelný rytmus, opakované argumentační šablony a málo viditelných autorských voleb. Tento problém byl patrný při lidském čtení a projevil se také v orientačním testu automatických detektorů.

Proto byly všechny narativní kapitoly znovu vystavěny po významových blocích. Nešlo o synonymický spinner ani o mechanické nahrazování slov. Před redakcí byly uzamčeny:

- výzkumné otázky;
- nosná tvrzení a jejich síla;
- citace a zdrojové kotvy;
- číselné údaje a lokátory;
- význam evidenčních tříd;
- hranice assurance a dokumentového designu.

Redakce změnila kompozici odstavců, rytmus, přechody a způsob vysvětlení autorských rozhodnutí. Nebyly přidávány pravopisné chyby, neviditelné znaky, překlady tam a zpět ani jiné technické prostředky. Výsledek detektorů nebyl použit jako akademické kritérium a jeden z testovaných nástrojů nadále označoval pilotní úryvek jako pravděpodobně generovaný.

Po redakci byly kapitoly znovu kontrolovány proti zdrojům, datům a claim-evidence ledgeru. Hodnoticí balíček neobsahoval pracovní meziverze ani jejich označení.

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

Hlavní tvrzení rukopisu jsou napojena na `audit/claim-evidence-ledger.csv`. Všech devět položek E3/E4 prošlo samostatnou kontrolou originálního lokátoru a hranice tvrzení. Přibližně desetiprocentní kontrolní vzorek byl znovu klasifikován bez původního hodnocení; jedna položka byla snížena z E3 na E2, protože omezené ujištění nad celou zprávou samo nepředstavovalo rozhodovací vazbu.

## Co kontrola zahrnovala

- ověření DOI a bibliografických metadat;
- práci s oficiálními firemními dokumenty;
- práci s primárními právními prameny EUR-Lex a českou legislativou;
- přesné stránkové nebo sekční lokátory;
- negativní případy a proti-důkazy;
- oddělení output, outcome a impact claimu;
- oddělení assurance od hloubky manažerské integrace;
- kontrolní překódování a druhou kontrolu nejsilnějších položek;
- technickou kontrolu struktury, tabulek a exportu;
- úplnou redakci narativních kapitol se zachováním evidenčního základu.

## Co kontrola nezahrnovala

- přečtení všech citovaných akademických článků druhým lidským odborníkem v plném textu;
- nezávislé opakování kódování druhým lidským analytikem;
- rozhovory se zaměstnanci, managementem, dodavateli nebo komunitami;
- ověření interních investičních dokumentů a skutečné provozní praxe;
- skutečnou ústní obhajobu autorem-studentem;
- posouzení oficiální komisí nebo podání do studijního systému.

Experiment tedy dokládá schopnost vytvořit auditovatelný akademický artefakt. Neprokazuje nezávisle pravdivost všech firemních tvrzení ani schopnost konkrétního studenta práci obhájit.

## Jak číst výsledek posudku

Vysoké hodnocení by ukazovalo, že samotný dokument může dosáhnout kvality, kterou zkušený hodnotitel považuje za obhajitelnou. Neznamenalo by, že je přijatelné nahradit studentskou práci modelem nebo zatajit jeho použití.

Nízké hodnocení je vhodné rozdělit podle konkrétních příčin: nedostatek teorie, nevhodný design, malý či selektivní korpus, slabá analýza, chyby ve zdrojích, nepřiměřené závěry, stylistické problémy nebo absence možnosti ověřit porozumění při obhajobě.

Největší vzdělávací hodnotu má přesný popis toho, které části obstály a které selhaly bez ohledu na produkční původ textu.

## Otázky pro reflexi hodnotitele

1. Které části posudku by byly stejné, kdyby text napsal známý student?
2. Které indicie vedly k odhadu způsobu vzniku a byly skutečně spolehlivé?
3. Změnila informace o procesu hodnocení odborné správnosti, nebo spíše úsudek o autorství a integritě?
4. Které kompetence lze ověřit pouze při průběžném vedení, práci se zdrojem nebo ústní obhajobě?
5. Co by měl vedoucí vyžadovat jako procesní důkaz vedle výsledného PDF?

## Hlavní pedagogická teze experimentu

Hotový text už nelze považovat za dostatečný důkaz toho, kdo vykonal intelektuální práci a čemu autor rozumí. To není důvod rezignovat na kvalifikační práce. Je to důvod posílit průběžnou práci s rozhodnutími, zdrojovou stopou, verzemi, nečekanými daty a obhajobou.