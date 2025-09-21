# Mini Ceneo - Porównywarka Cen w Pythonie - Lekcja 9

## Opis
Ten program to uproszczona wersja popularnej polskiej porównywarki cen Ceneo.pl, zbudowana w Pythonie. Program demonstruje zaawansowane użycie słowników (dictionary), w tym zagnieżdżone struktury danych, sortowanie, znajdowanie minimum/maksimum oraz praktyczne zastosowanie algorytmów porównawczych.

**Znajdź najlepszą ofertę!** Program pozwala porównywać ceny produktów w różnych sklepach, znajdować najkorzystniejsze oferty, dodawać nowe dane i obliczać potencjalne oszczędności. To świetny przykład pokazujący, jak tworzyć praktyczne aplikacje biznesowe używając struktur danych i algorytmów, które są podstawą rzeczywistych serwisów e-commerce.

## Kod źródłowy
Znajdziesz go w pliku `lekcja-09-mini-ceneo/mini_ceneo.py`

## Czego się nauczysz

- Jak używać **zagnieżdżonych słowników** do reprezentowania złożonych danych
- Jak **iterować po słownikach** używając `items()`, `keys()`, `values()`
- Jak znajdować **wartość minimalną i maksymalną** w słowniku
- Jak **sortować słowniki** według wartości używając `sorted()` i `lambda`
- Jak implementować **menu interaktywne** z wieloma opcjami
- Jak stosować **enumerate()** do numerowania elementów
- Jak używać **float('inf')** do inicjalizacji wartości minimalnej
- Jak tworzyć **funkcje pomocnicze** do obsługi danych
- Jak **aktualizować zagnieżdżone słowniki** dynamicznie
- Jak formatować **wyjście tekstowe** dla czytelności

## Jak działa porównywarka?

1. **Struktura danych** - zagnieżdżony słownik przechowuje informacje:
   - Pierwszy poziom: nazwa produktu (klucz)
   - Drugi poziom: słownik sklepów z cenami
   - Przykład: `produkty["laptop"]["MediaExpert"] = 3499`

2. **Algorytm porównywania** - przeszukuje wszystkie sklepy dla danego produktu:
   - Iteruje przez wszystkie ceny
   - Zapamiętuje najniższą wartość
   - Zwraca sklep z najlepszą ofertą

3. **Sortowanie ofert** - prezentuje ceny od najniższej do najwyższej:
   - Używa `sorted()` z funkcją `lambda`
   - Oblicza różnice cenowe
   - Oznacza najlepszą ofertę

## Algorytm - kluczowe funkcje

Znajdowanie najlepszej oferty:
```python
def znajdz_najlepsza_oferte(nazwa_produktu):
    najtanszy_sklep = ""
    najnizsza_cena = float('inf')
    
    for sklep, cena in produkty[nazwa_produktu].items():
        if cena < najnizsza_cena:
            najnizsza_cena = cena
            najtanszy_sklep = sklep
    
    return {"sklep": najtanszy_sklep, "cena": najnizsza_cena}
```

Sortowanie po cenach:

```
posortowane = sorted(ceny_produktu.items(), key=lambda x: x
```

```
Przykładowy przebieg programu

==================================================
🛍️  MINI CENEO - PORÓWNYWARKA CEN  🛍️
==================================================

📋 MENU:

    🔍 Znajdź najlepszą cenę
    📊 Porównaj wszystkie oferty
    ➕ Dodaj nową ofertę
    💵 Oblicz oszczędność
    ❌ Wyjście

Twój wybór (1-5): 2📦 Dostępne produkty:

    Laptop
    Telefon
    Słuchawki

Wpisz nazwę produktu: laptop

💰 Ceny dla: LAPTOP
✅ x-kom: 3199 zł ⭐ NAJLEPSZA CENA! Morele: 3250 zł (różnica: +51 zł) RTV Euro AGD: 3299 zł (różnica: +100 zł) MediaExpert: 3499 zł (różnica: +300 zł)⏎ Naciśnij ENTER aby kontynuować...
```

## Funkcje w programie

- **`wyswietl_logo()`** - wyświetla nagłówek programu
- **`pokaz_produkty()`** - lista dostępnych produktów
- **`znajdz_najlepsza_oferte()`** - algorytm znajdowania minimum w słowniku
- **`pokaz_wszystkie_ceny()`** - sortowanie i wyświetlanie wszystkich ofert
- **`dodaj_oferte()`** - aktualizacja bazy danych produktów
- **`oblicz_oszczednosc()`** - kalkulacja różnicy między max a min ceną
- **`clear_screen()`** - czyszczenie konsoli dla lepszej czytelności
- **`main()`** - główna pętla programu z obsługą menu

## Zastosowania praktyczne

- **E-commerce** - podstawy systemów porównywania cen
- **Analiza danych** - znajdowanie wartości ekstremalnych
- **Aplikacje biznesowe** - zarządzanie danymi produktów
- **Web scraping** - struktura danych dla pobranych cen
- **Systemy rekomendacji** - podstawy algorytmów wyboru
- **Bazy danych** - wprowadzenie do struktur relacyjnych

## Ciekawostki

- Ceneo.pl powstało w 2005 roku i jest największą polską porównywarką cen
- Codziennie porównuje miliony ofert z tysięcy sklepów
- Algorytmy porównywania cen są podstawą wielu aplikacji zakupowych
- Zagnieżdżone słowniki są często używane w REST API do reprezentacji JSON
- Python jest jednym z najpopularniejszych języków do web scrapingu i analizy cen

## Link do filmu
[Obejrzyj lekcję na YouTube](#) *(link zostanie dodany po publikacji)*

---

To jest dziewiąta lekcja z serii "Python dla początkujących". Pokazuje, jak tworzyć praktyczne aplikacje biznesowe używając słowników i algorytmów. Od prostego projektu edukacyjnego do prawdziwej aplikacji e-commerce - jeden krok!
