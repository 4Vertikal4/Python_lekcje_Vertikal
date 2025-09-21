# Szyfr GA-DE-RY-PO-LU-KI - Harcerski szyfr w Pythonie - Lekcja 8

## Opis
Ten program to implementacja klasycznego szyfru harcerskiego GA-DE-RY-PO-LU-KI, używanego od pokoleń przez polskich harcerzy podczas gier terenowych i zabaw. Program demonstruje praktyczne zastosowanie słowników (dictionary), funkcji, pracy ze stringami oraz koncepcji szyfrowania symetrycznego.

**Zaszyfruj swoje tajne wiadomości!** Ten szyfr podstawieniowy zamienia pary liter według prostego klucza ukrytego w samej nazwie. Co ciekawe, ta sama operacja służy zarówno do szyfrowania, jak i deszyfrowania - to piękno matematycznej symetrii! Świetny przykład pokazujący, jak tworzyć programy kryptograficzne i pracować ze strukturami danych.

## Kod źródłowy
Znajdziesz go w pliku `lekcja-08-gaderypoluki/gaderypoluki.py`

## Czego się nauczysz

- Jak używać **słowników (dictionary)** do mapowania znaków
- Jak stosować metodę **get()** do bezpiecznego pobierania wartości ze słownika
- Jak pracować z **iteracją przez stringi** znak po znaku
- Jak używać **join()** do efektywnego łączenia stringów
- Jak implementować **funkcje symetryczne** (ta sama funkcja szyfruje i deszyfruje)
- Jak stosować **list comprehension** do skrócenia kodu
- Jak tworzyć **czytelne menu** w konsoli
- Jak pisać **funkcje pomocnicze** i organizować kod
- Jak implementować **testy jednostkowe** dla swoich funkcji
- Jak pracować z **wielkością liter** w stringach

## Jak działa szyfr?

1. **Klucz szyfru** - nazwa GA-DE-RY-PO-LU-KI to jednocześnie klucz:
   - G zamienia się z A (i odwrotnie)
   - D zamienia się z E (i odwrotnie)
   - R zamienia się z Y (i odwrotnie)
   - P zamienia się z O (i odwrotnie)
   - L zamienia się z U (i odwrotnie)
   - K zamienia się z I (i odwrotnie)

2. **Symetria** - ten sam algorytm szyfruje i deszyfruje:
   - Jeśli A→G przy szyfrowaniu
   - To G→A przy deszyfrowaniu
   - Dlatego podwójne zaszyfrowanie daje oryginalny tekst!

3. **Litery poza kluczem** - pozostają bez zmian (np. H, B, C, itd.)

## Algorytm - jak to działa?

Program używa słownika do szybkiego mapowania liter:
```python
def gaderypoluki(tekst):
    szyfr = stworz_slownik_gaderypoluki()
    wynik = ""
    
    for litera in tekst:
        if litera in szyfr:
            wynik += szyfr[litera]
        else:
            wynik += litera
    
    return wynik
```

Przykładowy przebieg programu

```
╔════════════════════════════════════╗
║   SZYFR GA-DE-RY-PO-LU-KI         ║
║   Popularny szyfr harcerski       ║
╚════════════════════════════════════╝

--- MENU ---
1. Zaszyfruj/Odszyfruj tekst
2. Zobacz przykład
3. Informacje o szyfrze
4. Wyjście

Wybierz opcję (1-4): 2

==================================================
PRZYKŁAD DZIAŁANIA:
==================================================
Tekst oryginalny: HARCERZ
Po zaszyfrowaniu: HGYCDYZ
Po odszyfrowaniu: HARCERZ

Zauważ, że używamy tej samej funkcji do szyfrowania i deszyfrowania!
```


## Funkcje w programie

- **`stworz_slownik_gaderypoluki()`** - tworzy słownik z parami liter do zamiany
- **`gaderypoluki()`** - główna funkcja szyfrująca/deszyfrująca (wersja podstawowa)
- **`gaderypoluki_v2()`** - krótsza wersja używająca list comprehension
- **`pokaz_przyklad()`** - demonstracja działania szyfru z przykładem
- **`test_szyfru()`** - automatyczne testy poprawności implementacji
- **`main()`** - główna pętla programu z menu

## Zastosowania praktyczne

- **Kryptografia dla początkujących** - wprowadzenie do podstaw szyfrowania
- **Słowniki w praktyce** - efektywne mapowanie danych
- **Gry i zabawy edukacyjne** - tworzenie narzędzi do zabaw harcerskich
- **Przetwarzanie tekstu** - operacje na stringach znak po znaku
- **Symetria w algorytmach** - zrozumienie funkcji odwracalnych
- **Historia informatyki** - nauka o klasycznych metodach szyfrowania

## Ciekawostki

- Szyfr GA-DE-RY-PO-LU-KI jest używany w polskim harcerstwie od lat 20. XX wieku
- Istnieją inne warianty tego szyfru: PO-LI-TY-KA-RE-NU, KO-NI-EC-MA-TU-RY
- Jest to przykład szyfru monoalfabetycznego podstawieniowego
- Łatwy do zapamiętania dzięki rytmicznej nazwie

## Link do filmu
[Obejrzyj lekcję na YouTube](#) *(link zostanie dodany po publikacji)*

---

To jest ósma lekcja z serii "Python dla początkujących". Pokazuje, że programowanie może łączyć się z tradycją i historią - implementujemy szyfr używany przez pokolenia harcerzy, ucząc się przy tym koncepcji programistycznych. Czuwaj!
