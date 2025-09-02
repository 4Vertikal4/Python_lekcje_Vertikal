## Kółko i Krzyżyk w Pythonie - Lekcja 4

## Opis
Ten program to klasyczna gra w kółko i krzyżyk, w której gracz mierzy się z komputerem. Gra demonstruje praktyczne zastosowanie list, funkcji, pętli oraz instrukcji warunkowych w Pythonie. Komputer wykonuje ruchy losowo, a program automatycznie sprawdza warunki wygranej i remisu. To świetny przykład tworzenia interaktywnej gry konsolowej z pełną logiką rozgrywki.

## Kod źródłowy
Znajdziesz go w pliku lekcja-04-kolko-krzyzyk/kolko_krzyzyk.py

## Czego się nauczysz

- Jak używać list do reprezentowania struktury danych (plansza gry)
- Jak tworzyć i wywoływać funkcje do organizacji kodu
- Jak stosować pętle while do ciągłej rozgrywki
- Jak obsługiwać błędy użytkownika za pomocą try/except
- Jak używać modułu random do generowania ruchów komputera
- Jak sprawdzać złożone warunki logiczne (wygrana w poziomie, pionie, po skosie)
- Jak używać list comprehension do tworzenia list

## Jak działa program?

- Inicjalizacja planszy - program tworzy pustą planszę jako listę 9 elementów
- Wyświetlanie instrukcji - pokazuje numerację pól (1-9) dla łatwiejszej nawigacji
- Główna pętla gry:
   * **Ruch gracza** - gracz wybiera pole wpisując numer od 1 do 9
   * **Walidacja** - program sprawdza poprawność ruchu
   * **Ruch komputera** - komputer wykonuje losowy ruch na wolnym polu
   * **Sprawdzenie wygranej** - po każdym ruchu sprawdzane są warunki wygranej
- Zakończenie - gra kończy się wygraną jednego z graczy lub remisem

## Przykładowy przebieg gry

```
Witaj w grze Kółko i Krzyżyk!
Ty grasz jako 'X', komputer jako 'O'
Wybierz pozycję wpisując numer od 1 do 9

Pozycje na planszy:
 1 | 2 | 3 
---+---+---
 4 | 5 | 6 
---+---+---
 7 | 8 | 9 

Wybierz pozycję (1-9): 5

   |   |   
---+---+---
   | X |   
---+---+---
   |   |   

Komputer wykonuje ruch...

   |   | O 
---+---+---
   | X |   
---+---+---
   |   |   

Wybierz pozycję (1-9): 1

 X |   | O 
---+---+---
   | X |   
---+---+---
   |   |   

Komputer wykonuje ruch...

 X |   | O 
---+---+---
   | X |   
---+---+---
 O |   |   

Wybierz pozycję (1-9): 9

 X |   | O 
---+---+---
   | X |   
---+---+---
 O |   | X 

Gratulacje! Wygrałeś!
```

## Link do filmu
[Obejrzyj lekcję na YouTube](https://youtu.be/VVWvhv-ofvg)

... ... ... ...

To jest czwarta lekcja z serii "Python dla początkujących". W tej lekcji połączyliśmy wszystkie dotychczasowe koncepcje w funkcjonalną grę!

