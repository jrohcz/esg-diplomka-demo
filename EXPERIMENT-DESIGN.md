# Experiment: může současné LLM vytvořit hodnotitelnou diplomovou práci?

**Stav:** pracovní protokol, 1. 9. 2026  
**Větev:** `experiment/complete-document-analysis`  
**Účel:** vytvořit úplný rukopis založený na ověřitelných veřejných datech a následně jej nechat zaslepeně oznámkovat zkušenými vedoucími závěrečných prací.

## 1. Co experiment testuje

Experiment netestuje, zda lze podvodně vydávat syntetická data za skutečný výzkum. Testuje, zda současný LLM-orientovaný workflow dokáže:

1. formulovat obhajitelný výzkumný problém;
2. dohledat a správně použít odborné a regulatorní zdroje;
3. sestavit skutečný, veřejně auditovatelný datový korpus;
4. provést transparentní kvalitativní analýzu;
5. vytvořit úplný rukopis v rozsahu a struktuře diplomové práce;
6. obstát v nezávislém posudku a následné adversariální obhajobě.

## 2. Změna oproti syntetickému pilotu

Původní projekt připravoval polostrukturované rozhovory a obsahoval šest výrazně označených syntetických pilotních profilů. Ty zůstávají pouze jako test analytického workflow.

Hodnotitelný rukopis nebude syntetické rozhovory vydávat za empirii. Empirickou část nahradí **kvalitativní komparativní analýza veřejných podnikových dokumentů**. Každé tvrzení o analyzovaném podniku musí být dohledatelné k veřejnému primárnímu dokumentu a konkrétnímu lokátoru.

## 3. Pracovní název rukopisu

> **Proměna ESG reportingu vybraných českých podniků v období zavádění CSRD: kvalitativní komparativní analýza veřejných dokumentů**

## 4. Výzkumná otázka

**Jak se v období přechodu od dobrovolného nefinančního reportingu k režimu CSRD/ESRS změnil způsob, kterým vybrané české podniky veřejně popisují, řídí a dokládají svou ESG agendu?**

Dílčí otázky:

1. Jak se změnila struktura, rozsah a jazyk reportingu?
2. Jak podniky vymezují materialitu, stakeholdery a odpovědnost za ESG?
3. Nakolik propojují cíle s výchozí hodnotou, termínem, vlastníkem, metrikou a výsledkem?
4. Jak oddělují regulatorní povinnost od provozní, strategické nebo reputační motivace?
5. Jaké rozdíly se objevují mezi sektory a mezi dobrovolným a ESRS/CSRD reportem?
6. Kde zůstává mezera mezi tvrzením, metrikou a doloženou změnou rozhodování?

## 5. Empirický korpus

Cíl je **šest podnikových případů a dvanáct primárních dokumentů**. U každého případu bude zahrnut jeden dokument před přechodem na ESRS/CSRD nebo z jeho počáteční fáze a jeden nejnovější srovnatelný dokument dostupný k datu uzávěrky.

Pracovní případy:

| Případ | Sektor | Zamýšlené dokumenty |
|---|---|---|
| Skupina ČEZ | energetika | zpráva před ESRS + integrovaná zpráva podle ESRS/CSRD |
| MONETA Money Bank | bankovnictví | Sustainability at MONETA 2024 + 2025 / příslušné CSRD statements |
| Škoda Auto | automobilový průmysl | Sustainability Report 2023 + Annual/Sustainability Report 2024/2025 |
| Kofola ČeskoSlovensko | nápoje a spotřební zboží | nefinanční report 2023 + zpráva o udržitelnosti ve výroční zprávě 2024/2025 |
| O2 Czech Republic | telekomunikace | ESG report 2023 + ESG report 2024 nebo první CSRD statement |
| šestý kontrastní případ | průmysl / služby | vybrán podle dostupnosti dvou plných, ověřitelných a srovnatelných dokumentů |

Výběr je záměrný, nikoli reprezentativní. Kritérii jsou české působení, veřejná dostupnost plného textu, dostatečná informační bohatost, sektorová variace a možnost časového porovnání.

## 6. Analytická jednotka a metoda

Analytickou jednotkou není „skutečná kvalita ESG podniku“, ale **způsob veřejné reprezentace ESG implementace v konkrétním dokumentu**.

Použita bude kvalitativní obsahová analýza s kombinací deduktivních a induktivních kódů. Výchozí kódovací oblasti:

- motivace a typ tlaku;
- materialita a stakeholder engagement;
- governance, vlastník a rozhodovací pravomoc;
- cíl, baseline, termín, metrika a dosažený výsledek;
- provozní integrace a finanční vazba;
- náklady, bariéry a nejistota dat;
- assurance a dohledatelnost;
- rétorika legitimity, ocenění a ratingů;
- přiznané limity a negativní informace;
- změny mezi starším a novějším dokumentem.

Po prvním cyklu bude codebook revidován. Kvantifikace výskytu slouží pouze k orientaci; závěry budou stát na vztazích, kontrastech, negativních případech a dohledatelných ukázkách.

## 7. Auditní stopa

Pro každý dokument vznikne:

- bibliografický záznam a archivní URL;
- kontrolní součet lokální kopie, pokud to licence dovolí;
- dokumentové memo;
- tabulka kódovaných úryvků s lokátorem;
- případová syntéza;
- změnové memo mezi dvěma obdobími;
- vazba mezi výsledkovým tvrzením a konkrétní evidencí.

Syntetický pilot zůstane fyzicky i významově oddělen od empirického korpusu.

## 8. Výstupy

1. úplný rukopis v Markdownu;
2. sazebně čistý DOCX;
3. PDF pro zaslepené hodnocení;
4. příloha s metodikou, korpusem a auditní stopou;
5. samostatný balíček pro odtajnění experimentu;
6. hodnoticí formulář a scénář adversariální obhajoby.

## 9. Zaslepené hodnocení

Hodnotitel obdrží rukopis označený pouze jako anonymizovaný text k akademickému posouzení. Nebude mu tvrzeno, že text napsal člověk. Předem bude požádán, aby práci hodnotil podle běžných kritérií diplomové práce a původ textu neposuzoval před odevzdáním známky a komentáře.

Před odtajněním se zaznamená:

- navržená známka;
- doporučení / nedoporučení k obhajobě;
- hlavní silné a slabé stránky;
- podezření na použití AI a jeho důvody;
- otázky k obhajobě;
- odhad míry lidského porozumění autora.

## 10. Kritérium „prošla“

Primární kritérium je, zda většina hodnotitelů nezávisle doporučí rukopis k obhajobě nebo jej ohodnotí známkou odpovídající úspěšnému splnění.

Sekundární kritéria:

- závažnost identifikovaných věcných chyb;
- počet nedohledatelných či zdrojem nepodpořených tvrzení;
- kvalita metodologické kritiky;
- úspěch v mock obhajobě;
- rozdíl mezi hodnocením před a po odtajnění původu.

## 11. Etická hranice

Rukopis nebude předložen jako skutečná kvalifikační práce konkrétního studenta ani použit k získání akademického titulu. Hodnotitelé budou účastníky evaluačního experimentu. Veřejná prezentace výsledků musí přesně uvést, že šlo o simulaci hodnocení, nikoli o skutečné odevzdání a obhajobu.
