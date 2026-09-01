# Pilotní test autorské redakce

## Účel

Než se přepíše celý rukopis, otestuje se jeden stabilní úsek teoretické kapitoly. Cílem je ověřit tři věci současně:

1. zda nový text zachoval význam a citace;
2. zda je při lidském čtení méně šablonovitý;
3. zda se změní orientační výsledek automatických detektorů.

Detektorový výsledek není jediným akceptačním kritériem.

## Baseline

Zdroj: `chapters/01-theoretical-framework.md` v baseline commitu začleněném do `main`.

Rozsah:

- začátek: nadpis `## 1.1 Od společenské odpovědnosti k ESG`;
- konec: poslední odstavec sekce `## 1.4 Legitimita a firemní zveřejnění`, končící slovy `...odlišný účel dokumentu.`

## Redigovaná verze

Soubor:

`variants/authorial-pass/pilot/01-theory-opening-after.md`

Při vložení do detektoru se vynechá úvodní H1, citace v blockquote a tento README. Testuje se pouze text od `## 1.1` do konce sekce `## 1.4`.

## Postup benchmarku

1. Z baseline i redigované verze vytvořit úryvek se stejnými tematickými hranicemi.
2. Zaznamenat počet slov obou variant.
3. Každý úryvek vložit do stejného detektoru za stejných podmínek.
4. U nestabilních nástrojů test jednou zopakovat.
5. Zapsat výsledek do `audit/detector-benchmark.csv`.
6. Neprovádět mikroeditace po každém skóre. Nejprve vyhodnotit zdrojovou přesnost a lidskou čitelnost.

## Kontrolní otázky pro lidské čtení

- Je zřetelnější, proč práce rozlišuje jazyk, praxi, formalizaci a rozhodovací integraci?
- Působí autorská omezení přirozeně, nebo pouze jako nový druh šablony?
- Neztratila se některá metodická opatrnost?
- Nevzniklo nové tvrzení, které citovaný zdroj nepodporuje?
- Nezvýšila se délka jen přidáním vaty?
- Je text stále dostatečně akademický?

## Rozhodnutí po pilotu

Možné výsledky:

- **přijmout styl:** text je lepší odborně i stylisticky a benchmark se změnil žádoucím směrem;
- **upravit styl:** čitelnost se zlepšila, ale některé pasáže jsou příliš rozvláčné nebo příliš osobní;
- **odmítnout styl:** význam se posunul, přibyla vata nebo se zhoršila odborná přesnost;
- **ignorovat detektorový rozdíl:** lidské čtení je lepší, ale automatický nástroj zůstal beze změny;
- **zastavit optimalizaci:** detektor se zlepšil, ale text je horší.
