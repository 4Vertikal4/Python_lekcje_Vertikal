## Kalkulator Zrzutki na Paliwo w Pythonie - Lekcja 2

Ten program w Pythonie oblicza, ile każda osoba powinna zapłacić, gdy dzielą się wspólnym kosztem paliwa. Użytkownik wprowadza całkowity koszt paliwa i liczbę osób, a program oblicza kwotę na osobę.

## Czego się nauczysz

- Jak pobierać dane od użytkownika za pomocą funkcji `input()`
- Jak konwertować dane tekstowe na liczby za pomocą funkcji `int()` i `float()`
- Jak wykonywać podstawowe operacje matematyczne w Pythonie
- Jak zaokrąglać liczby do określonego miejsca po przecinku za pomocą funkcji `round()`
- Jak używać f-string do formatowania tekstu z danymi liczbowymi

## Kod źródłowy
```python
print("Witaj w kalkulatorze zrzutki na paliwo")
koszt_paliwa = input("Podaj całkowity koszt paliwa (np. 150.00):\n")
koszt_paliwa = float(koszt_paliwa)
ilosc_osob = input("Ile osób dzieli się kosztami?\n")
ilosc_osob = int(ilosc_osob)
koszt_na_osobe = koszt_paliwa / ilosc_osob
kwota_zaokraglona = round(koszt_na_osobe, 2)
print(f"Każda osoba powinna zapłacić: {kwota_zaokraglona} zł")
```

## Jak działa program?

1. Program wita użytkownika i prosi o podanie całkowitego kosztu paliwa.
2. Pobiera liczbę osób dzielących się kosztami.
3. Oblicza koszt na osobę dzieląc całkowity koszt przez liczbę osób.
4. Zaokrągla wynik do dwóch miejsc po przecinku.
5. Wyświetla końcowy wynik.

## Przykładowy wynik

**Witaj w kalkulatorze zrzutki na paliwo**

**Podaj całkowity koszt paliwa (np. 150.00):**
*200*

**Ile osób dzieli się kosztami?**
*4*

**Każda osoba powinna zapłacić: 50.0 zł**

## Link do filmu
[Obejrzyj lekcję na YouTube](https://youtu.be/zNJlTxCnIh0)

Zadania dodatkowe

1. Dodaj walidację danych: Sprawdź, czy użytkownik nie wprowadza wartości ujemnych lub zerowych dla liczby osób.
2. Popraw formatowanie wyniku: Zapewnij, że kwota jest zawsze wyświetlana z dwoma miejscami po przecinku.
3. Rozszerz program: Dodaj możliwość zapisania wyników do pliku tekstowego.
4. Ulepsz interfejs: Dodaj więcej informacji o tym, jak program oblicza wynik.

... ... ... ...

To jest druga lekcja z serii "Python dla początkujących". Kolejne lekcje będą wprowadzać bardziej zaawansowane koncepcje programowania.

