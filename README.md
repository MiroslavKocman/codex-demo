# Codex demo — hřiště pro Codex Cloud

Malý projekt na vyzkoušení práce s repozitářem: čtení kódu, změny, testy a pull requesty.
Stačí Python **3.10+**, žádné balíčky, API klíče ani externí služby nejsou potřeba.
Repozitář je veřejný; používej pouze ukázková data.

## Rychlé spuštění

```bash
python3 scripts/check.py
printf 'Ahoj světe' | python3 text_stats.py
python3 text_stats.py --file samples/example.txt
```

Ve Windows můžeš místo `python3` použít `python`.
Výstup prvního příkladu je `{"characters": 10, "words": 2, "lines": 1}`.

## Co aplikace dělá

`text_stats.py` přečte standardní vstup nebo UTF-8 soubor a vrátí JSON:

- `characters`: počet znaků Unicode v načteném textu, včetně mezer a konců řádků;
- `words`: počet částí oddělených bílými znaky; interpunkce zůstává součástí slova;
- `lines`: počet řádků podle `str.splitlines()`. Prázdný text má nula řádků a závěrečný konec řádku nepřidává další řádek.

Při čtení souboru Python normalizuje CRLF na LF; počty znaků se vztahují k načtenému textu.
Chyba čtení vrací kód 1 a zprávu na stderr.
Původní interaktivní ukázka `hello.py` je zachována.

## Připojení ke Codex Cloud

Repozitář je připravený; samotné cloudové prostředí se vytváří v účtu ChatGPT/Codex.

1. V novém úkolu zvol **Work in → Cloud → Select environment → Create environment**.
   Alternativně otevři **Settings → Codex Cloud → Environments → Create environment**.
2. Vyber repozitář **MiroslavKocman/codex-demo** a klikni **Get started**.
3. Pro nastavení vlož:

   > Připrav toto prostředí pro Python 3.12. Projekt používá pouze standardní knihovnu. Spusť `python3 scripts/check.py` a ověř `python3 text_stats.py --file samples/example.txt`. Není potřeba instalovat závislosti ani nastavovat secrets nebo spouštět server. Prostředí pojmenuj codex-demo.

4. Zkontroluj výsledek a zvol **Publish**. Poté **Start a new task**.

Pokud používáš starší rozhraní se setup skriptem, nastav Python 3.12 a jako setup použij `python3 scripts/check.py`. Maintenance script není potřeba. Kód i testy fungují bez přístupu k internetu.

Postup odpovídá [oficiální dokumentaci cloudových prostředí](https://learn.chatgpt.com/docs/environments/cloud-environments).

## První úkol

> Projdi repozitář a AGENTS.md, spusť testy a česky mi vysvětli strukturu projektu a výsledky. Zatím neměň kód.

Potom si vyber úlohu v [EXERCISES.md](EXERCISES.md). Každou změnu řeš v samostatném úkolu a před sloučením zkontroluj diff a testy.

## Struktura

| Soubor | Účel |
| --- | --- |
| `text_stats.py` | Ukázková aplikace a CLI |
| `tests/test_text_stats.py` | Jednotkové a integrační testy |
| `scripts/check.py` | Jediný příkaz pro kontrolu projektu |
| `AGENTS.md` | Pokyny pro Codex |
| `EXERCISES.md` | Hotová zadání k vyzkoušení |
| `.github/workflows/tests.yml` | Testy na GitHubu při pushi a pull requestu |
