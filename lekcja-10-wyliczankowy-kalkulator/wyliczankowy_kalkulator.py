import random

# Logo kalkulatora wyliczankowego
logo = """
=========================================
   KALKULATOR WYLICZANKOWY
   Liczymy z polskimi wyliczankami!
=========================================
"""

# Słownik z polskimi wyliczankami
wyliczanki = {
    "dodawanie": {
        "tekst": "Raz, dwa, trzy - baba jaga patrzy, cztery, pięć - będę dodawać chcieć!",
        "symbol": "+",
        "akcja": "DODAJ"
    },
    "odejmowanie": {
        "tekst": "Entliczek pentliczek, czerwony stoliczek, a na tym stoliczku - odejmij z koszyczku!",
        "symbol": "-", 
        "akcja": "ODEJMIJ"
    },
    "mnożenie": {
        "tekst": "Siała baba mak, nie wiedziała jak, a tu przyszedł pan - pomnóż sobie sam!",
        "symbol": "*",
        "akcja": "POMNÓŻ"
    },
    "dzielenie": {
        "tekst": "Poszła Ola do przedszkola, zapomniała parasola, a tu pada deszcz - podziel jeśli chcesz!",
        "symbol": "/",
        "akcja": "PODZIEL"
    }
}

# Funkcje matematyczne
def dodaj(n1, n2):
    return n1 + n2

def odejmij(n1, n2):
    return n1 - n2

def pomnoz(n1, n2):
    return n1 * n2

def podziel(n1, n2):
    if n2 != 0:
        return n1 / n2
    else:
        return "Nie można dzielić przez zero!"

# Słownik operacji
operacje = {
    "+": dodaj,
    "-": odejmij,
    "*": pomnoz,
    "/": podziel
}

def policz_sylaby(tekst):
    """Liczy przybliżoną liczbę sylab w tekście"""
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

def policz_slowa(tekst):
    """Liczy liczbę słów w tekście"""
    return len(tekst.split())

def wybierz_wyliczanke():
    """Pozwala użytkownikowi wybrać wyliczankę"""
    print("\nWYBIERZ WYLICZANKĘ DLA DZIAŁANIA:")
    print("=" * 50)
    
    # Wyświetl wszystkie wyliczanki
    opcje = list(wyliczanki.keys())
    for i, nazwa in enumerate(opcje, 1):
        wyliczanka = wyliczanki[nazwa]
        print(f"\n{i}. {wyliczanka['akcja']} ({wyliczanka['symbol']})")
        print(f"   '{wyliczanka['tekst']}'")
    
    while True:
        try:
            wybor = int(input("\nWpisz numer wyliczanki (1-4): "))
            if 1 <= wybor <= 4:
                wybrana = opcje[wybor - 1]
                return wyliczanki[wybrana]['symbol']
            else:
                print("Wybierz numer od 1 do 4!")
        except ValueError:
            print("Wpisz poprawny numer!")

def tryb_wyliczankowy():
    """Tryb gdzie liczby są generowane na podstawie wyliczanek"""
    print("\nTRYB WYLICZANKOWY - liczby z wyliczanek!")
    print("=" * 50)
    
    # Wybierz losową wyliczankę dla pierwszej liczby
    wyliczanka1 = random.choice([
        "Ene due rike fake, torba borba ósme smake",
        "Jeden, dwa, trzy, cztery, pięć, sześć, siedem, osiem",
        "Idzie kominiarz po drabinie, fiku miku na drabinie"
    ])
    
    print(f"\nPierwsza wyliczanka: '{wyliczanka1}'")
    
    wybor_liczby = input("Chcesz policzyć [S]ylaby czy [W] słowa? (S/W): ").upper()
    
    if wybor_liczby == 'S':
        num1 = float(policz_sylaby(wyliczanka1))
        print(f"Liczba sylab: {int(num1)}")
    else:
        num1 = float(policz_slowa(wyliczanka1))
        print(f"Liczba słów: {int(num1)}")
    
    # Wybierz operację
    symbol = wybierz_wyliczanke()
    
    # Wybierz drugą wyliczankę
    wyliczanka2 = random.choice([
        "Kosi kosi łapci, nie masz mleka",
        "Sroczka kaszkę warzyła, dzieci karmiła",
        "Raz i dwa, raz i dwa, będzie wojna niedługo"
    ])
    
    print(f"\nDruga wyliczanka: '{wyliczanka2}'")
    
    if wybor_liczby == 'S':
        num2 = float(policz_sylaby(wyliczanka2))
        print(f"Liczba sylab: {int(num2)}")
    else:
        num2 = float(policz_slowa(wyliczanka2))
        print(f"Liczba słów: {int(num2)}")
    
    # Wykonaj obliczenie
    funkcja_obliczeniowa = operacje[symbol]
    wynik = funkcja_obliczeniowa(num1, num2)
    
    print("\n" + "=" * 50)
    print(f"WYNIK: {num1} {symbol} {num2} = {wynik}")
    print("=" * 50)
    
    return wynik

def kalkulator_wyliczankowy():
    """Główna funkcja kalkulatora"""
    print(logo)
    
    print("Witaj w Kalkulatorze Wyliczankowym!")
    print("\nWybierz tryb:")
    print("1. Tryb klasyczny (sam wpisujesz liczby)")
    print("2. Tryb wyliczankowy (liczby z wyliczanek)")
    
    tryb = input("\nWybierz tryb (1 lub 2): ")
    
    if tryb == "2":
        wynik = tryb_wyliczankowy()
    else:
        # Tryb klasyczny
        print("\nTRYB KLASYCZNY")
        print("=" * 50)
        
        num1 = float(input("\nJaka jest pierwsza liczba? "))
        
        # Pokaż wyliczanki i pozwól wybrać operację
        symbol = wybierz_wyliczanke()
        
        num2 = float(input("\nJaka jest druga liczba? "))
        
        # Wykonaj obliczenie
        funkcja_obliczeniowa = operacje[symbol]
        wynik = funkcja_obliczeniowa(num1, num2)
        
        print("\n" + "=" * 50)
        print(f"WYNIK: {num1} {symbol} {num2} = {wynik}")
        print("=" * 50)
    
    # Zapytaj czy kontynuować
    kontynuuj = True
    while kontynuuj:
        decyzja = input("\nChcesz policzyć coś jeszcze? (T/N): ").upper()
        if decyzja == 'T':
            print("\n" * 2)
            kalkulator_wyliczankowy()  # Rekursja
            kontynuuj = False
        elif decyzja == 'N':
            print("\nDo zobaczenia! Pamiętaj o wyliczankach!")
            kontynuuj = False
        else:
            print("Wpisz T lub N")

# Dodatkowa funkcja - generator wyliczanek matematycznych
def stworz_wyliczanke_matematyczna(wynik):
    """Tworzy prostą wyliczankę z wynikiem"""
    wyliczanki_koncowe = [
        f"Raz, dwa, trzy - wynik patrzy: {wynik} już czy!",
        f"Hop siup, wynik to {wynik}, brawo Ty!",
        f"Entliczek pentliczek, {wynik} w koszyku leży sobie cichutko!",
        f"Siała baba mak, wynik wyszedł tak: {wynik}, i to fakt!"
    ]
    return random.choice(wyliczanki_koncowe)

# Funkcja edukacyjna - nauka tabliczki mnożenia przez wyliczanki
def tabliczka_wyliczankowa():
    """Nauka tabliczki mnożenia przez wyliczanki"""
    print("\nTABLICZKA MNOŻENIA Z WYLICZANKAMI")
    print("=" * 50)
    
    liczba = int(input("Którą tabliczkę chcesz ćwiczyć? (1-10): "))
    
    for i in range(1, 11):
        wynik = liczba * i
        if i <= 5:
            print(f"\n'{liczba} razy {i} - wynik leci!' = {wynik}")
        else:
            print(f"\n'{liczba} razy {i} - już wiesz czy?' = {wynik}")
    
    print(f"\n{stworz_wyliczanke_matematyczna('Brawo!')}")

# Uruchom program
if __name__ == "__main__":
    print("=" * 60)
    print("MENU GŁÓWNE:")
    print("1. Kalkulator Wyliczankowy")
    print("2. Tabliczka Mnożenia z Wyliczankami")
    print("=" * 60)
    
    wybor = input("\nCo chcesz zrobić? (1 lub 2): ")
    
    if wybor == "2":
        tabliczka_wyliczankowa()
    else:
        kalkulator_wyliczankowy()
