"""
GENERATOR TESTOWYCH KART KREDYTOWYCH
=====================================
UWAGA: Ten kod generuje TYLKO testowe numery kart do celów:
- Testowania aplikacji e-commerce
- Nauki programowania
- Zrozumienia działania walidacji kart

Te numery NIE MOGĄ być użyte do prawdziwych transakcji!
"""

import random
from datetime import datetime, timedelta

def algorytm_luhna(numer):
    """
    Sprawdza czy numer karty jest poprawny według algorytmu Luhna
    """
    cyfry = [int(d) for d in str(numer)]
    suma_kontrolna = 0
    
    # Przechodzimy od prawej do lewej
    for i, cyfra in enumerate(reversed(cyfry[:-1])):
        if i % 2 == 0:  # Co druga cyfra
            cyfra *= 2
            if cyfra > 9:
                cyfra -= 9
        suma_kontrolna += cyfra
    
    # Obliczamy cyfrę kontrolną
    return (10 - (suma_kontrolna % 10)) % 10

def generuj_numer_karty(typ_karty="visa"):
    """
    Generuje testowy numer karty kredytowej
    """
    # Prefiksy dla różnych typów kart (testowe)
    prefiksy = {
        "visa": "4",
        "mastercard": "5",
        "amex": "37"
    }
    
    # Rozpoczynamy od prefiksu
    numer = prefiksy.get(typ_karty, "4")
    
    # Dodajemy kolejne cyfry (łącznie ma być 16 cyfr dla Visa/MC, 15 dla Amex)
    dlugosc = 15 if typ_karty == "amex" else 16
    
    # Generujemy losowe cyfry (bez ostatniej - cyfry kontrolnej)
    for _ in range(dlugosc - len(numer) - 1):
        numer += str(random.randint(0, 9))
    
    # Obliczamy i dodajemy cyfrę kontrolną według algorytmu Luhna
    cyfra_kontrolna = algorytm_luhna(numer + "0")
    numer += str(cyfra_kontrolna)
    
    return numer

def generuj_date_waznosci():
    """
    Generuje losową datę ważności karty (w przyszłości)
    """
    # Data między 1 a 5 lat w przyszłości
    dni_w_przyszlosci = random.randint(365, 365 * 5)
    data_waznosci = datetime.now() + timedelta(days=dni_w_przyszlosci)
    
    miesiac = str(data_waznosci.month).zfill(2)
    rok = str(data_waznosci.year)[-2:]
    
    return f"{miesiac}/{rok}"

def generuj_cvv(typ_karty="visa"):
    """
    Generuje kod CVV/CVC
    """
    # Amex ma 4-cyfrowy CVV, pozostałe 3-cyfrowy
    cyfry = 4 if typ_karty == "amex" else 3
    cvv = ""
    for _ in range(cyfry):
        cvv += str(random.randint(0, 9))
    return cvv

def sformatuj_numer_karty(numer):
    """
    Formatuje numer karty dodając spacje co 4 cyfry
    """
    return ' '.join([numer[i:i+4] for i in range(0, len(numer), 4)])

def generuj_imie_nazwisko():
    """
    Generuje losowe imię i nazwisko dla karty testowej
    """
    imiona = ["Jan", "Anna", "Piotr", "Maria", "Tomasz", "Katarzyna", "Michał", "Agnieszka"]
    nazwiska = ["Kowalski", "Nowak", "Wiśniewski", "Wójcik", "Kowalczyk", "Kamiński"]
    
    return f"{random.choice(imiona)} {random.choice(nazwiska)}"

def main():
    """
    Główna funkcja programu
    """
    print("=" * 50)
    print("GENERATOR TESTOWYCH KART KREDYTOWYCH")
    print("=" * 50)
    print("UWAGA: To są numery TYLKO do testów!")
    print("NIE używaj ich do prawdziwych transakcji!")
    print("=" * 50)
    print()
    
    # Pytamy użytkownika o typ karty
    print("Wybierz typ karty:")
    print("1 - Visa")
    print("2 - Mastercard")
    print("3 - American Express")
    
    wybor = input("\nTwój wybór (1-3): ")
    
    typy = {"1": "visa", "2": "mastercard", "3": "amex"}
    typ_karty = typy.get(wybor, "visa")
    
    # Generujemy dane karty
    print("\n" + "=" * 50)
    print("WYGENEROWANA KARTA TESTOWA:")
    print("=" * 50)
    
    numer = generuj_numer_karty(typ_karty)
    print(f"Numer karty: {sformatuj_numer_karty(numer)}")
    print(f"Data ważności: {generuj_date_waznosci()}")
    print(f"CVV/CVC: {generuj_cvv(typ_karty)}")
    print(f"Właściciel: {generuj_imie_nazwisko()}")
    print(f"Typ: {typ_karty.upper()}")
    
    print("\n" + "=" * 50)
    print("Pamiętaj: To jest karta TESTOWA!")
    print("Używaj tylko do testowania aplikacji!")
    print("=" * 50)

if __name__ == "__main__":
    main()

