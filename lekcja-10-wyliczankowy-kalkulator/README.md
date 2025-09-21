# Kalkulator Wyliczankowy - Polski Kalkulator z Rymowankami - Lekcja 10

## Opis
Ten program to innowacyjne połączenie nauki programowania z polską kulturą dziecięcą. Kalkulator wykorzystuje tradycyjne polskie wyliczanki do wyboru operacji matematycznych oraz opcjonalnie do generowania liczb na podstawie sylab czy słów. Program demonstruje zaawansowane techniki programowania: funkcje jako wartości, słowniki funkcji, rekursję oraz interaktywne menu.

**Liczymy z wyliczankami!** Program pozwala wykonywać obliczenia matematyczne wybierając operacje poprzez polskie wyliczanki jak "Raz, dwa, trzy - baba jaga patrzy" czy "Entliczek pentliczek". To kreatywne podejście do nauki programowania, które łączy elementy kultury z praktyczną implementacją kalkulatora, pokazując że kodowanie może być zabawne i związane z lokalnymi tradycjami.

## Kod źródłowy
Znajdziesz go w pliku `lekcja-10-kalkulator-wyliczankowy/kalkulator_wyliczankowy.py`

## Czego się nauczysz

- Jak **przechowywać funkcje jako wartości** w słownikach
- Jak używać **funkcji bez nawiasów** do przekazywania referencji
- Jak implementować **rekursję** jako alternatywę dla zagnieżdżonych pętli
- Jak tworzyć **interaktywne menu** z różnymi trybami działania
- Jak używać **float()** do dokładnych obliczeń matematycznych
- Jak implementować **algorytmy liczenia sylab i słów** w tekście
- Jak stosować **moduł random** do losowania elementów
- Jak budować **funkcje pomocnicze** dla operacji matematycznych
- Jak używać **f-stringów** do formatowania wyników
- Jak łączyć **programowanie z elementami kultury**

## Jak działa kalkulator?

1. **Struktura danych** - słownik wyliczanek przechowuje:
   - Tekst wyliczanki dla każdej operacji
   - Symbol matematyczny (+, -, *, /)
   - Nazwę akcji (DODAJ, ODEJMIJ, POMNÓŻ, PODZIEL)

2. **Dwa tryby działania**:
   - **Tryb klasyczny** - użytkownik sam wprowadza liczby
   - **Tryb wyliczankowy** - liczby generowane z ilości sylab/słów w wyliczankach

3. **Mechanizm wyboru** - użytkownik wybiera operację poprzez wyliczankę:
   - System wyświetla wszystkie dostępne wyliczanki
   - Każda wyliczanka odpowiada konkretnej operacji
   - Program wykonuje obliczenia używając wybranej funkcji

## Algorytm - kluczowe funkcje

Przechowywanie funkcji w słowniku:
```python
operacje = {
    "+": dodaj,
    "-": odejmij,
    "*": pomnoz,
    "/": podziel
}
```

Liczenie sylab w tekście:

```python
def policz_sylaby(tekst):
    samogloski = "aąeęioóuyAĄEĘIOÓUY"
    sylaby = 0
    poprzednia_samogloska = False
    
    for litera in tekst:
        if litera in samogloski:
            if not poprzednia_samogloska:
                sylaby += 1
            poprzednia_samogloska = True
        else:
            poprzednia_samogloska = False
    
    return sylaby
```

Rekursja dla kontynuacji obliczeń:

```python
def kalkulator_wyliczankowy():
    # kod kalkulatora
    decyzja = input("Chcesz policzyć coś jeszcze? (T/N): ")
    if decyzja == 'T':
        kalkulator_wyliczankowy()  # Rekursja
```

Przykładowy przebieg programu

```
=========================================
   KALKULATOR WYLICZANKOWY
   Liczymy z polskimi wyliczankami!
=========================================

Witaj w Kalkulatorze Wyliczankowym!Wybierz tryb:

    Tryb klasyczny (sam wpisujesz liczby)
    Tryb wyliczankowy (liczby z wyliczanek)

Wybierz tryb (1 lub 2): 1
TRYB KLASYCZNY
Jaka jest pierwsza liczba? 10
WYBIERZ WYLICZANKĘ DLA DZIAŁANIA:

    DODAJ (+) 'Raz, dwa, trzy - baba jaga patrzy, cztery, pięć - będę dodawać chcieć!'

    ODEJMIJ (-) 'Entliczek pentliczek, czerwony stoliczek, a na tym stoliczku - odejmij z koszyczku!'

    POMNÓŻ (*) 'Siała baba mak, nie wiedziała jak, a tu przyszedł pan - pomnóż sobie sam!'

    PODZIEL (/) 'Poszła Ola do przedszkola, zapomniała parasola, a tu pada deszcz - podziel jeśli chcesz!'

Wpisz numer wyliczanki (1-4): 3Jaka jest druga liczba? 5
================================================== WYNIK: 10.0 * 5.0 = 50.0
Chcesz policzyć coś jeszcze? (T/N): N Do zobaczenia! Pamiętaj o wyliczankach!
```


## Funkcje w programie

- **`dodaj()`, `odejmij()`, `pomnoz()`, `podziel()`** - podstawowe operacje matematyczne
- **`policz_sylaby()`** - algorytm liczenia sylab w tekście polskim
- **`policz_slowa()`** - liczenie słów w wyliczance
- **`wybierz_wyliczanke()`** - interaktywny wybór operacji przez wyliczankę
- **`tryb_wyliczankowy()`** - tryb generowania liczb z wyliczanek
- **`kalkulator_wyliczankowy()`** - główna funkcja z rekursją
- **`stworz_wyliczanke_matematyczna()`** - generator wyliczanek z wynikiem
- **`tabliczka_wyliczankowa()`** - nauka tabliczki mnożenia przez wyliczanki

## Zastosowania praktyczne

- **Edukacja** - innowacyjne podejście do nauki matematyki i programowania
- **Aplikacje dla dzieci** - połączenie nauki z zabawą
- **Lokalizacja oprogramowania** - przykład adaptacji kodu do kultury lokalnej
- **Przetwarzanie języka naturalnego** - podstawy analizy tekstu (sylaby, słowa)
- **Gamifikacja** - wykorzystanie elementów zabawy w aplikacjach edukacyjnych
- **Kulturowe API** - możliwość rozbudowy o więcej elementów folkloru

## Ciekawostki

- Polskie wyliczanki mają setki lat tradycji i były przekazywane ustnie z pokolenia na pokolenie
- "Entliczek pentliczek" to najpopularniejsza polska wyliczanka, znana w całym kraju
- Liczenie sylab w języku polskim jest trudniejsze niż w angielskim ze względu na grupy spółgłoskowe
- Rekursja (funkcja wywołująca samą siebie) jest często używana w algorytmach matematycznych
- Python jest jednym z najpopularniejszych języków do nauczania programowania dzieci
- Łączenie programowania z kulturą lokalną zwiększa zaangażowanie uczniów

## Link do filmu
[Obejrzyj lekcję na YouTube](#) *(link zostanie dodany po publikacji)*

---

To jest dziesiąta lekcja z serii "Python dla początkujących". Pokazuje, jak tworzyć kreatywne aplikacje edukacyjne łączące programowanie z polską kulturą. Od klasycznego kalkulatora do innowacyjnego narzędzia wykorzystującego wyliczanki - programowanie może być zabawne i związane z naszymi tradycjami!
