# Byki i Krowy - Gra logiczna w Pythonie - Lekcja 7

## Opis
Ten program to implementacja klasycznej gry logicznej "Byki i Krowy" (Bulls and Cows), znanej również jako prekursor gry Mastermind. Program demonstruje praktyczne zastosowanie funkcji, pętli while, instrukcji warunkowych, walidacji danych oraz pracy z listami i stringami.

**Komputer wymyślił tajną liczbę!** Twoim zadaniem jest odgadnąć 4-cyfrową liczbę z unikalnymi cyframi w maksymalnie 10 próbach. Po każdej próbie otrzymujesz wskazówki w postaci byków i krów. To świetny przykład pokazujący, jak tworzyć interaktywne gry z logiką walidacji i systemem podpowiedzi.

## Kod źródłowy
Znajdziesz go w pliku `lekcja-07-byki-krowy/byki_i_krowy.py`

## Czego się nauczysz

- Jak używać **modułu random** do generowania losowych liczb
- Jak tworzyć **funkcje z parametrami** i wartościami zwracanymi
- Jak implementować **walidację danych** wprowadzanych przez użytkownika
- Jak używać **len()** do sprawdzania długości stringów i list
- Jak używać **append()** do dodawania elementów do listy
- Jak pracować z **set()** do sprawdzania unikalności elementów
- Jak stosować **pętle for** do iteracji przez stringi
- Jak używać **krotek (tuple)** do przechowywania wielu wartości
- Jak implementować **historię gry** i wyświetlać poprzednie próby
- Jak używać **rekurencji** do restartu gry

## Jak działa program?

1. **Generowanie tajnej liczby** - losowanie 4-cyfrowej liczby z unikalnymi cyframi
   - Pierwsza cyfra nie może być zerem
   - Wszystkie cyfry muszą być różne
   - Używamy `random.choice()` i usuwamy wybrane cyfry z puli

2. **Walidacja wprowadzonych danych** - sprawdzanie poprawności:
   - Dokładnie 4 cyfry
   - Tylko cyfry (bez liter)
   - Nie zaczyna się od zera
   - Wszystkie cyfry unikalne

3. **System podpowiedzi**:
   - **Byk** = cyfra jest i znajduje się na właściwej pozycji
   - **Krowa** = cyfra jest w liczbie, ale na złej pozycji

4. **Historia gry** - zapisywanie wszystkich prób gracza do wyświetlenia

## Algorytm - jak to działa?

Program używa prostego algorytmu porównania pozycyjnego:
```python
for i in range(4):
    if odgadniecie[i] == tajny_numer[i]:
        byki += 1
    elif odgadniecie[i] in tajny_numer:
        krowy += 1
```

- Iterujemy przez każdą pozycję
- Sprawdzamy dokładne dopasowanie (byk)
- Jeśli nie, sprawdzamy czy cyfra jest gdziekolwiek w liczbie (krowa)
- System ten daje graczowi precyzyjne wskazówki bez ujawniania rozwiązania

## Przykładowy przebieg programu

```
==================================================
        GRA: BYKI I KROWY
==================================================

ZASADY:
  * Odgadnij 4-cyfrową liczbę
  * Wszystkie cyfry muszą być różne
  * Liczba nie może zaczynać się od 0

WYNIKI:
  * BYK = cyfra na właściwym miejscu
  * KROWA = cyfra jest, ale na złym miejscu

Powodzenia!

--------------------------------------------------

Masz 10 prób na odgadnięcie liczby.


[Próba 1/10]
Podaj 4-cyfrową liczbę: 4
[BŁĄD] Liczba musi mieć dokładnie 4 cyfry!

[Próba 1/10]
Podaj 4-cyfrową liczbę: 4123
Wynik: 0 byków, 1 krowa

[Próba 2/10]
Podaj 4-cyfrową liczbę: 4444
[BŁĄD] Wszystkie cyfry muszą być różne!

[Próba 2/10]
Podaj 4-cyfrową liczbę: 4125
Wynik: 1 byk, 1 krowa

[Próba 3/10]
Podaj 4-cyfrową liczbę: 1275
Wynik: 3 byki, 0 krów

Twoje dotychczasowe próby:
-----------------------------------
Nr | Liczba | Byki | Krowy
-----------------------------------
 1 | 4123   |  0   |   1
 2 | 4125   |  1   |   1
 3 | 1275   |  3   |   0
-----------------------------------

[Próba 4/10]
Podaj 4-cyfrową liczbę: 1285
Wynik: 2 byki, 0 krów

Twoje dotychczasowe próby:
-----------------------------------
Nr | Liczba | Byki | Krowy
-----------------------------------
 1 | 4123   |  0   |   1
 2 | 4125   |  1   |   1
 3 | 1275   |  3   |   0
 4 | 1285   |  2   |   0
-----------------------------------

[Próba 5/10]
Podaj 4-cyfrową liczbę: 1675
Wynik: 4 byki, 0 krów

==================================================
        GRATULACJE! WYGRAŁEŚ!
==================================================
Odgadłeś liczbę 1675 w 5 próbach!
==================================================

==================================================
Chcesz zagrać jeszcze raz? (tak/nie): nie

Dziękuję za grę! Do zobaczenia!

```


## Funkcje w programie

- **`generuj_tajny_numer()`** - losuje 4-cyfrową liczbę z unikalnymi cyframi
- **`sprawdz_format()`** - waliduje wprowadzone dane od gracza
- **`policz_byki_krowy()`** - porównuje odgadnięcie z tajną liczbą
- **`wyswietl_wynik()`** - formatuje i wyświetla wynik z odmianą słów
- **`wyswietl_instrukcje()`** - pokazuje zasady gry
- **`wyswietl_historie()`** - wyświetla tabelę z poprzednimi próbami
- **`main()`** - główna pętla gry

## Zastosowania praktyczne

- **Logika gier** - podstawy tworzenia gier z systemem podpowiedzi
- **Walidacja danych** - zabezpieczanie programu przed błędnymi danymi
- **Algorytmy porównawcze** - jak porównywać dane według różnych kryteriów
- **Historia akcji** - przechowywanie i wyświetlanie historii działań użytkownika
- **UI w konsoli** - tworzenie czytelnego interfejsu tekstowego

## Link do filmu
[Obejrzyj lekcję na YouTube](https://youtu.be/S7Rd_QNgzPQ)

---

To jest siódma lekcja z serii "Python dla początkujących". Pokazuje, że tworzenie gier logicznych to świetny sposób na naukę programowania - każda linia kodu przybliża nas do rozwiązania, jak każda próba przybliża gracza do odgadnięcia tajnej liczby!


