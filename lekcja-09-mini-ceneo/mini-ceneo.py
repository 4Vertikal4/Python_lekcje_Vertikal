# Mini Ceneo - Porównywarka Cen
import os

def clear_screen():
    """Czyści ekran konsoli"""
    print("\n" * 50)

def wyswietl_logo():
    """Wyświetla logo programu"""
    print("="*50)
    print("🛍️  MINI CENEO - PORÓWNYWARKA CEN  🛍️")
    print("="*50)

# Baza produktów - słownik słowników
produkty = {
    "laptop": {
        "MediaExpert": 3499,
        "RTV Euro AGD": 3299,
        "x-kom": 3199,
        "Morele": 3250
    },
    "telefon": {
        "MediaExpert": 2799,
        "RTV Euro AGD": 2899,
        "x-kom": 2699,
        "Allegro": 2650
    },
    "słuchawki": {
        "MediaExpert": 299,
        "RTV Euro AGD": 279,
        "x-kom": 289,
        "Morele": 275
    }
}

def pokaz_produkty():
    """Wyświetla dostępne produkty"""
    print("\n📦 Dostępne produkty:")
    for nr, produkt in enumerate(produkty.keys(), 1):
        print(f"{nr}. {produkt.capitalize()}")

def znajdz_najlepsza_oferte(nazwa_produktu):
    """Znajduje najtańszy sklep dla danego produktu"""
    if nazwa_produktu not in produkty:
        return None
    
    ceny_produktu = produkty[nazwa_produktu]
    
    # Znajdowanie minimum
    najtanszy_sklep = ""
    najnizsza_cena = float('inf')
    
    for sklep, cena in ceny_produktu.items():
        if cena < najnizsza_cena:
            najnizsza_cena = cena
            najtanszy_sklep = sklep
    
    return {
        "sklep": najtanszy_sklep,
        "cena": najnizsza_cena
    }

def pokaz_wszystkie_ceny(nazwa_produktu):
    """Pokazuje wszystkie ceny dla produktu"""
    if nazwa_produktu not in produkty:
        print("❌ Nie znaleziono produktu!")
        return
    
    print(f"\n💰 Ceny dla: {nazwa_produktu.upper()}")
    print("-" * 30)
    
    ceny_produktu = produkty[nazwa_produktu]
    
    # Sortowanie po cenie
    posortowane = sorted(ceny_produktu.items(), key=lambda x: x[1])
    
    for sklep, cena in posortowane:
        if cena == posortowane[0][1]:
            print(f"✅ {sklep}: {cena} zł ⭐ NAJLEPSZA CENA!")
        else:
            roznica = cena - posortowane[0][1]
            print(f"   {sklep}: {cena} zł (różnica: +{roznica} zł)")

def dodaj_oferte():
    """Dodaje nową ofertę do bazy"""
    print("\n➕ DODAWANIE NOWEJ OFERTY")
    
    pokaz_produkty()
    produkt = input("\nPodaj nazwę produktu: ").lower()
    
    if produkt not in produkty:
        print("❌ Nieznany produkt!")
        return
    
    sklep = input("Podaj nazwę sklepu: ")
    cena = int(input("Podaj cenę (zł): "))
    
    # Aktualizacja słownika
    produkty[produkt][sklep] = cena
    print(f"✅ Dodano ofertę: {produkt} w {sklep} za {cena} zł")

def oblicz_oszczednosc(nazwa_produktu):
    """Oblicza ile można zaoszczędzić"""
    if nazwa_produktu not in produkty:
        return None
    
    ceny = list(produkty[nazwa_produktu].values())
    oszczednosc = max(ceny) - min(ceny)
    return oszczednosc

# GŁÓWNA PĘTLA PROGRAMU
def main():
    kontynuuj = True
    
    while kontynuuj:
        clear_screen()
        wyswietl_logo()
        
        print("\n📋 MENU:")
        print("1. 🔍 Znajdź najlepszą cenę")
        print("2. 📊 Porównaj wszystkie oferty")
        print("3. ➕ Dodaj nową ofertę")
        print("4. 💵 Oblicz oszczędność")
        print("5. ❌ Wyjście")
        
        wybor = input("\nTwój wybór (1-5): ")
        
        if wybor == "1":
            pokaz_produkty()
            produkt = input("\nWpisz nazwę produktu: ").lower()
            
            najlepsza = znajdz_najlepsza_oferte(produkt)
            if najlepsza:
                print(f"\n🏆 NAJLEPSZA OFERTA:")
                print(f"Sklep: {najlepsza['sklep']}")
                print(f"Cena: {najlepsza['cena']} zł")
            else:
                print("❌ Nie znaleziono produktu!")
                
        elif wybor == "2":
            pokaz_produkty()
            produkt = input("\nWpisz nazwę produktu: ").lower()
            pokaz_wszystkie_ceny(produkt)
            
        elif wybor == "3":
            dodaj_oferte()
            
        elif wybor == "4":
            pokaz_produkty()
            produkt = input("\nWpisz nazwę produktu: ").lower()
            oszczednosc = oblicz_oszczednosc(produkt)
            if oszczednosc:
                print(f"\n💰 Możesz zaoszczędzić: {oszczednosc} zł")
                print(f"   kupując w najtańszym sklepie!")
            else:
                print("❌ Nie znaleziono produktu!")
                
        elif wybor == "5":
            print("\n👋 Dziękujemy za korzystanie z Mini Ceneo!")
            kontynuuj = False
        else:
            print("❌ Nieprawidłowy wybór!")
        
        if kontynuuj and wybor in ["1", "2", "3", "4"]:
            input("\n⏎ Naciśnij ENTER aby kontynuować...")

# Uruchomienie programu
if __name__ == "__main__":
    main()
