def stworz_slownik_gaderypoluki():
    """
    Tworzy słownik z parami liter do zamiany.
    Każda litera mapuje się na swoją parę.
    """
    szyfr = {
        'G': 'A', 'A': 'G',
        'D': 'E', 'E': 'D',
        'R': 'Y', 'Y': 'R',
        'P': 'O', 'O': 'P',
        'L': 'U', 'U': 'L',
        'K': 'I', 'I': 'K',
        # Dodajemy też małe litery dla wygody
        'g': 'a', 'a': 'g',
        'd': 'e', 'e': 'd',
        'r': 'y', 'y': 'r',
        'p': 'o', 'o': 'p',
        'l': 'u', 'u': 'l',
        'k': 'i', 'i': 'k'
    }
    return szyfr

def gaderypoluki(tekst):
    """
    Szyfruje lub deszyfruje tekst używając szyfru GA-DE-RY-PO-LU-KI.
    Ta sama funkcja służy do szyfrowania i deszyfrowania!
    """
    szyfr = stworz_slownik_gaderypoluki()
    wynik = ""
    
    for litera in tekst:
        # Jeśli litera jest w szyfrze, zamieniamy ją
        if litera in szyfr:
            wynik += szyfr[litera]
        else:
            # Jeśli nie ma jej w szyfrze, zostawiamy bez zmian
            wynik += litera
    
    return wynik

def gaderypoluki_v2(tekst):
    """
    Wersja krótsza używająca metody get()
    """
    szyfr = stworz_slownik_gaderypoluki()
    return ''.join(szyfr.get(litera, litera) for litera in tekst)

def pokaz_przyklad():
    """
    Pokazuje przykład działania szyfru
    """
    print("\n" + "="*50)
    print("PRZYKŁAD DZIAŁANIA:")
    print("="*50)
    
    przykladowy_tekst = "HARCERZ"
    print(f"Tekst oryginalny: {przykladowy_tekst}")
    
    zaszyfrowany = gaderypoluki(przykladowy_tekst)
    print(f"Po zaszyfrowaniu: {zaszyfrowany}")
    
    odszyfrowany = gaderypoluki(zaszyfrowany)
    print(f"Po odszyfrowaniu: {odszyfrowany}")
    
    print("\nZauważ, że używamy tej samej funkcji do szyfrowania i deszyfrowania!")
    print("="*50)

def main():
    """
    Główna funkcja programu z menu
    """
    print("╔════════════════════════════════════╗")
    print("║   SZYFR GA-DE-RY-PO-LU-KI         ║")
    print("║   Popularny szyfr harcerski       ║")
    print("╚════════════════════════════════════╝")
    
    while True:
        print("\n--- MENU ---")
        print("1. Zaszyfruj/Odszyfruj tekst")
        print("2. Zobacz przykład")
        print("3. Informacje o szyfrze")
        print("4. Wyjście")
        
        wybor = input("\nWybierz opcję (1-4): ")
        
        if wybor == "1":
            print("\n[Pamiętaj: ta sama operacja szyfruje i deszyfruje!]")
            tekst = input("Podaj tekst: ")
            
            if tekst:
                wynik = gaderypoluki(tekst)
                print(f"\n>>> WYNIK: {wynik}")
                
                # Pokazujemy że to działa w obie strony
                print(f"\nSprawdzenie (powtórne użycie szyfru):")
                print(f">>> {gaderypoluki(wynik)}")
            else:
                print("Nie podano tekstu!")
                
        elif wybor == "2":
            pokaz_przyklad()
            
        elif wybor == "3":
            print("\n" + "="*50)
            print("INFORMACJE O SZYFRZE GA-DE-RY-PO-LU-KI:")
            print("="*50)
            print("• Jest to szyfr podstawieniowy")
            print("• Zamienia pary liter według klucza:")
            print("  G↔A, D↔E, R↔Y, P↔O, L↔U, K↔I")
            print("• Litery spoza klucza pozostają bez zmian")
            print("• Ta sama operacja szyfruje i deszyfruje")
            print("• Używany od pokoleń przez harcerzy")
            print("="*50)
            
        elif wybor == "4":
            print("\nDo zobaczenia! Czuwaj!")
            break
            
        else:
            print("Nieprawidłowy wybór! Spróbuj ponownie.")

# Dodatkowa funkcja pomocnicza do testowania
def test_szyfru():
    """
    Funkcja testująca poprawność działania szyfru
    """
    print("\n--- TESTY AUTOMATYCZNE ---")
    
    testy = [
        ("HARCERZ", "HGYCDYZ"),
        ("PYTHON", "ORTHPN"),
        ("GADERYPOLUKI", "AGEDZROPULKI"),
        ("123", "123"),  # Cyfry bez zmian
        ("Ala ma kota", "Gug mg iptg")  # Ze spacjami
    ]
    
    for tekst, oczekiwany in testy:
        wynik = gaderypoluki(tekst)
        status = "✓" if wynik == oczekiwany else "✗"
        print(f"{status} '{tekst}' -> '{wynik}' (oczekiwano: '{oczekiwany}')")

# Uruchomienie programu
if __name__ == "__main__":
    # Możesz odkomentować linię poniżej żeby zobaczyć testy
    # test_szyfru()
    
    main()
