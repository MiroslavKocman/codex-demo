# Úlohy pro Codex Cloud

Zadávej postupně, každou v novém cloudovém úkolu nad větví `main`.
Po změně si prohlédni diff, testy a případně vytvoř pull request.

## 1. Orientace bez změny kódu

> Projdi AGENTS.md a repozitář, spusť `python3 scripts/check.py` a ukázkovou aplikaci. Vysvětli mi česky strukturu a výsledky. Neměň kód.

Hotovo, když: Codex popíše aplikaci, najde původní hello.py a uvede skutečný výsledek testů.

## 2. Nová funkce: unikátní slova

> Přidej do výsledku analýzy `unique_words`: počet různých slov bez ohledu na velikost písmen pomocí `casefold()`. Zachovej současné rozdělení podle bílých znaků a interpunkci. Pro `Ahoj ahoj světe` očekávám 2, pro prázdný text 0. Aktualizuj testy CLI i funkce a README. Spusť celý testovací příkaz a připrav změny k revizi.

Hotovo, když: funkce i CLI vrací nový údaj, česká diakritika funguje a všechny testy procházejí.

## 3. Nová volba příkazového řádku

> Přidej přepínač `--pretty`, který vypíše JSON s odsazením dvěma mezerami. Výchozí výstup musí zůstat na jednom řádku. Přidej testy obou režimů, aktualizuj README a spusť testy.

Hotovo, když: oba výstupy obsahují stejná data a výchozí použití se nezměnilo.

## 4. Úprava původní ukázky

> Uprav hello.py tak, aby šel importovat bez čekání na vstup. Vytvoř funkci greet(name), ořízni okolní mezery a pro prázdné jméno použij World. Zachovej interaktivní spuštění. Přidej testy importu bez vedlejších účinků, prázdného jména a běžného jména; spusť všechny testy.

Hotovo, když: import nic nevypisuje ani nečeká na vstup a původní spuštění stále funguje.
