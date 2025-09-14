# Generator Testowych Kart Kredytowych w Pythonie - Lekcja 5

## Opis
Ten program to generator **testowych** numerów kart kredytowych, stworzony wyłącznie do celów edukacyjnych i testowania aplikacji e-commerce. Program demonstruje praktyczne zastosowanie algorytmu Luhna, modułu random, funkcji oraz pracy z datami w Pythonie. Generator tworzy numery kart, które przechodzą matematyczną walidację, ale **NIE mogą być użyte do prawdziwych transakcji**. To świetny przykład zastosowania Pythona w kontekście bezpieczeństwa i walidacji danych finansowych.

## ⚠️ WAŻNE OSTRZEŻENIE
**Ten generator tworzy TYLKO testowe numery kart do celów:**
- Testowania aplikacji e-commerce
- Nauki programowania i algorytmów
- Zrozumienia działania walidacji kart kredytowych

**Numery te NIE MOGĄ być użyte do prawdziwych transakcji!**

## Kod źródłowy
Znajdziesz go w pliku `lekcja-05-generator-kart/generator_kart.py`

## Czego się nauczysz

- Jak implementować **algorytm Luhna** do walidacji numerów kart
- Jak używać modułu **random** do generowania losowych danych
- Jak pracować z **datami** używając datetime i timedelta
- Jak tworzyć **funkcje** do organizacji kodu
- Jak używać **słowników** do przechowywania danych konfiguracyjnych
- Jak formatować **stringi** i używać f-stringów
- Jak stosować **pętle for** z range() do generowania ciągów cyfr
- Jak używać **list comprehension** do formatowania danych
- Jak implementować **walidację danych** w aplikacjach finansowych

## Jak działa program?

1. **Wybór typu karty** - użytkownik wybiera między Visa, Mastercard lub American Express
2. **Generowanie numeru**:
   - Program dobiera odpowiedni prefiks (4 dla Visa, 5 dla Mastercard, 37 dla Amex)
   - Generuje losowe cyfry środkowej części numeru
   - Oblicza cyfrę kontrolną używając algorytmu Luhna
3. **Generowanie daty ważności** - losowa data między 1 a 5 lat w przyszłości
4. **Generowanie CVV/CVC** - 3 cyfry dla Visa/MC, 4 cyfry dla Amex
5. **Generowanie danych właściciela** - losowe imię i nazwisko z predefiniowanych list
6. **Formatowanie i wyświetlanie** - prezentacja danych w czytelny sposób

## Algorytm Luhna - serce programu

Algorytm Luhna to matematyczna metoda walidacji numerów kart kredytowych:
- Przechodzimy przez cyfry numeru od prawej do lewej
- Co drugą cyfrę mnożymy przez 2
- Jeśli wynik > 9, odejmujemy 9
- Sumujemy wszystkie cyfry
- Cyfra kontrolna to wartość, która sprawia, że suma jest podzielna przez 10

## Przykładowy przebieg programu

================================================== GENERATOR TESTOWYCH KART KREDYTOWYCH

UWAGA: To są numery TYLKO do testów! NIE używaj ich do prawdziwych transakcji!

Wybierz typ karty: 1 - Visa 2 - Mastercard 3 - American Express

Twój wybór (1-3): 1

================================================== WYGENEROWANA KARTA TESTOWA:

Numer karty: 4539 1488 0343 6467 

Data ważności: 08/27 

CVV/CVC: 342 

Właściciel: Anna Kowalski 

Typ: VISA

================================================== Pamiętaj: To jest karta TESTOWA! Używaj tylko do testowania aplikacji!


## Zastosowania praktyczne

- **Testowanie sklepów internetowych** - sprawdzanie formularzy płatności
- **Nauka programowania** - zrozumienie algorytmów walidacyjnych
- **Projekty edukacyjne** - demonstracja bezpieczeństwa w aplikacjach
- **Rozwój aplikacji** - testowanie integracji z systemami płatności

## Link do filmu
[Obejrzyj lekcję na YouTube](#) *(link zostanie dodany po publikacji)*

---

To jest piąta lekcja z serii "Python dla początkujących". W tej lekcji łączymy wiedzę o funkcjach, pętlach i algorytmach w praktyczny generator danych testowych, jednocześnie ucząc się o bezpieczeństwie w aplikacjach!

