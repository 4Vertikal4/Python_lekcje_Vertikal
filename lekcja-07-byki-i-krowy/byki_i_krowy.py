import random

def generuj_tajny_numer():
    """
    Generuje 4-cyfrową liczbę z unikalnymi cyframi.
    Pierwsza cyfra nie może być 0.
    """
    cyfry = list(range(10))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    # Wybieramy pierwszą cyfrę (nie może być 0)
    pierwsza_cyfra = random.choice(cyfry[1:])  # cyfry od 1 do 9
    tajny_numer = [pierwsza_cyfra]
    cyfry.remove(pierwsza_cyfra)
    
    # Wybieramy pozostałe 3 cyfry
    for _ in range(3):
        wybrana_cyfra = random.choice(cyfry)
        tajny_numer.append(wybrana_cyfra)
        cyfry.remove(wybrana_cyfra)
    
    return ''.join(map(str, tajny_numer))

def sprawdz_format(odgadniecie):
    """
    Sprawdza czy wprowadzona liczba ma poprawny format:
    - 4 cyfry
    - wszystkie cyfry są unikalne
    - nie zaczyna się od 0
    """
    # Sprawdzamy długość
    if len(odgadniecie) != 4:
        return False, "Liczba musi mieć dokładnie 4 cyfry!"
    
    # Sprawdzamy czy to są cyfry
    if not odgadniecie.isdigit():
        return False, "Wprowadź tylko cyfry!"
    
    # Sprawdzamy czy nie zaczyna się od 0
    if odgadniecie[0] == '0':
        return False, "Liczba nie może zaczynać się od 0!"
    
    # Sprawdzamy czy cyfry są unikalne
    if len(set(odgadniecie)) != 4:
        return False, "Wszystkie cyfry muszą być różne!"
    
    return True, "OK"

def policz_byki_krowy(tajny_numer, odgadniecie):
    """
    Porównuje odgadniecie z tajnym numerem.
    Zwraca liczbę byków i krów.
    """
    byki = 0
    krowy = 0
    
    for i in range(4):
        if odgadniecie[i] == tajny_numer[i]:
            byki += 1
        elif odgadniecie[i] in tajny_numer:
            krowy += 1
    
    return byki, krowy

def wyswietl_wynik(byki, krowy):
    """
    Wyświetla wynik w czytelny sposób
    """
    byki_tekst = "byk" if byki == 1 else "byki" if byki in [2,3,4] else "byków"
    krowy_tekst = "krowa" if krowy == 1 else "krowy" if krowy in [2,3,4] else "krów"
    
    print(f"Wynik: {byki} {byki_tekst}, {krowy} {krowy_tekst}")

def wyswietl_instrukcje():
    """
    Wyświetla instrukcje gry
    """
    print("=" * 50)
    print("        GRA: BYKI I KROWY")
    print("=" * 50)
    print("\nZASADY:")
    print("  * Odgadnij 4-cyfrową liczbę")
    print("  * Wszystkie cyfry muszą być różne")
    print("  * Liczba nie może zaczynać się od 0")
    print("\nWYNIKI:")
    print("  * BYK = cyfra na właściwym miejscu")
    print("  * KROWA = cyfra jest, ale na złym miejscu")
    print("\nPowodzenia!\n")
    print("-" * 50)

def wyswietl_historie(historia_gry):
    """
    Wyświetla historię dotychczasowych prób
    """
    print("\nTwoje dotychczasowe próby:")
    print("-" * 35)
    print("Nr | Liczba | Byki | Krowy")
    print("-" * 35)
    for i, (num, b, k) in enumerate(historia_gry, 1):
        print(f"{i:2d} | {num}   |  {b}   |   {k}")
    print("-" * 35)

def main():
    """
    Główna funkcja gry
    """
    wyswietl_instrukcje()
    
    # Generujemy tajny numer
    tajny_numer = generuj_tajny_numer()
    
    liczba_prob = 0
    max_prob = 10
    historia_gry = []
    
    print(f"\nMasz {max_prob} prób na odgadnięcie liczby.\n")
    
    while liczba_prob < max_prob:
        liczba_prob += 1
        
        # Pobieramy odgadniecie od gracza
        print(f"\n[Próba {liczba_prob}/{max_prob}]")
        odgadniecie = input("Podaj 4-cyfrową liczbę: ").strip()
        
        # Sprawdzamy format
        format_ok, komunikat = sprawdz_format(odgadniecie)
        if not format_ok:
            print(f"[BŁĄD] {komunikat}")
            liczba_prob -= 1  # Nie liczymy błędnej próby
            continue
        
        # Obliczamy byki i krowy
        byki, krowy = policz_byki_krowy(tajny_numer, odgadniecie)
        
        # Zapisujemy do historii
        historia_gry.append((odgadniecie, byki, krowy))
        
        # Wyświetlamy wynik
        wyswietl_wynik(byki, krowy)
        
        # Sprawdzamy czy gracz wygrał
        if byki == 4:
            print("\n" + "=" * 50)
            print("        GRATULACJE! WYGRAŁEŚ!")
            print("=" * 50)
            print(f"Odgadłeś liczbę {tajny_numer} w {liczba_prob} próbach!")
            print("=" * 50)
            break
        
        # Wyświetlamy historię po kilku próbach
        if liczba_prob >= 3 and liczba_prob < max_prob:
            wyswietl_historie(historia_gry)
        
    else:
        # Gracz przegrał (wyczerpał próby)
        print("\n" + "=" * 50)
        print("        KONIEC GRY - PRZEGRANA")
        print("=" * 50)
        print(f"Tajny numer to: {tajny_numer}")
        print("Spróbuj jeszcze raz!")
    
    # Pytanie o kolejną grę
    print("\n" + "=" * 50)
    nowa_gra = input("Chcesz zagrać jeszcze raz? (tak/nie): ").lower()
    if nowa_gra in ['tak', 't', 'yes', 'y']:
        print("\n" * 3)  # Czyścimy trochę ekran
        main()  # Rekurencyjnie uruchamiamy grę
    else:
        print("\nDziękuję za grę! Do zobaczenia!")

# Uruchomienie gry
if __name__ == "__main__":
    main()
