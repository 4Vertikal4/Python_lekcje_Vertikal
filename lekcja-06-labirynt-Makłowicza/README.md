# Labirynt Makłowicza - Algorytm zachłanny w Pythonie - Lekcja 6

## Opis
Ten program to humorystyczna symulacja Roberta Makłowicza nawigującego przez labirynt własnej kuchni. Program demonstruje praktyczne zastosowanie algorytmów nawigacji, pętli while, instrukcji warunkowych if/elif oraz pracy z dwuwymiarowymi strukturami danych.

**Robert Makłowicz utknął w swojej kuchni!** Program automatycznie prowadzi go do wyjścia używając prostego algorytmu nawigacji. To świetny przykład pokazujący, jak komputery rozwiązują problemy przestrzenne krok po kroku, nawet gdy nie "widzą" całego labiryntu.

## Kod źródłowy
Znajdziesz go w pliku `lekcja-06-makłowicz-labirynt/makłowicz_maze.py`

## Czego się nauczysz

- Jak używać **pętli while** do powtarzania akcji aż do osiągnięcia celu
- Jak stosować **instrukcje warunkowe if/elif** do podejmowania decyzji
- Jak pracować z **listami** reprezentującymi przestrzeń 2D
- Jak implementować **algorytmy nawigacji** w prostych grach
- Jak używać **indeksów** do poruszania się po strukturach danych
- Jak stosować **time.sleep()** do kontroli szybkości wykonania
- Jak czyścić ekran używając **os.system()** dla lepszej wizualizacji
- Jak debugować problemy z **poruszaniem się w przestrzeni 2D**
- Jak używać **f-stringów** do dynamicznego formatowania tekstu

## Jak działa program?

1. **Definicja labiryntu** - kuchnia reprezentowana jako lista stringów
   - `#` = ściana
   - `.` = wolna przestrzeń
   - `@` = pozycja Makłowicza (wyświetlana dynamicznie)
   - `X` = wyjście z kuchni

2. **Algorytm nawigacji** - hierarchia priorytetów ruchu:
   - Najpierw próbuj iść **w dół** (bo tam jest wyjście)
   - Jeśli nie możesz, idź **w prawo**
   - Jeśli nie możesz, idź **w lewo**
   - Ostatnia opcja: idź **w górę**

3. **Wizualizacja** - czyszczenie konsoli i odświeżanie widoku po każdym kroku

4. **Komentarze Makłowicza** - humorystyczne odniesienia kulinarne przy każdym ruchu

## Algorytm - dlaczego to działa?

Program używa **algorytmu zachłannego** z preferencją kierunkową:
- Zawsze wybiera pierwszy dostępny ruch według ustalonej hierarchii
- Priorytet "w dół" sprawia, że Makłowicz dąży w kierunku wyjścia
- Brak pamięci odwiedzonych miejsc - prostota kosztem optymalności
- Działa dla tego konkretnego labiryntu dzięki jego strukturze

## Przykładowy przebieg programu

```
KUCHNIA MAKŁOWICZA

# # # # # # # # # #
# . . . . . . . . #
# . # # # # # # . #
# . . . . . . . . #
# . # # # # # # . #
# . . . . . . . . #
# # # # # # # . . #
# . . . . . . . . @
# # # # # # # # # #

Eureka! Znalazłem wyjście! Czas na aperitif!

Makłowicz dotarł do wyjścia w 14 krokach!
```

## Cytaty Makłowicza

Program zawiera charakterystyczne komentarze przy ruchach:
- **W dół**: *"Schodzę w dół, jak temperatura przy blanszowaniu!"*
- **W prawo**: *"W prawo, jak przy mieszaniu risotto!"*
- **W lewo**: *"W lewo, zawsze pod prąd!"*
- **W górę**: *"W górę, jak suflety w piekarniku!"*
- **Sukces**: *"Eureka! Znalazłem wyjście! Czas na aperitif!"*

## Zastosowania praktyczne

- **Podstawy AI w grach** - tak działają NPC w prostych grach komputerowych
- **Robotyka** - podobne algorytmy używają roboty sprzątające
- **Pathfinding** - wprowadzenie do bardziej zaawansowanych algorytmów jak A*
- **Debugowanie** - śledzenie wykonania programu krok po kroku
- **Wizualizacja algorytmów** - zrozumienie jak komputer "myśli" o przestrzeni

## Link do filmu
[Obejrzyj lekcję na YouTube](#) *(link zostanie dodany po publikacji)*

---

To jest szósta lekcja z serii "Python dla początkujących". Pokazujemy że nauka programowania może być równie satysfakcjonująca co dobry obiad przygotowany według przepisu Makłowicza!
