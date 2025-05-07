import random

# Plansza jako lista 9 elementów (indeksy 0-8)
plansza = [" " for _ in range(9)]


def wyswietl_plansze_pomocnicza():
    print("\nPozycje na planszy:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")
    print()


def wyswietl_plansze():
    print(f"\n {plansza[0]} | {plansza[1]} | {plansza[2]} ")
    print("---+---+---")
    print(f" {plansza[3]} | {plansza[4]} | {plansza[5]} ")
    print("---+---+---")
    print(f" {plansza[6]} | {plansza[7]} | {plansza[8]} ")
    print()


def ruch_gracza():
    while True:
        try:
            pozycja = int(input("Wybierz pozycję (1-9): ")) - 1
            if pozycja < 0 or pozycja > 8:
                print("Podaj liczbę od 1 do 9!")
                continue
            if plansza[pozycja] != " ":
                print("To pole jest już zajęte!")
                continue
            return pozycja
        except ValueError:
            print("Podaj poprawną liczbę!")


def ruch_komputera():
    # Lista dostępnych pozycji
    wolne_pola = [i for i, pole in enumerate(plansza) if pole == " "]
    return random.choice(wolne_pola)


def sprawdz_wygrana(symbol):
    # Sprawdzenie poziomów
    if (plansza[0] == plansza[1] == plansza[2] == symbol or
            plansza[3] == plansza[4] == plansza[5] == symbol or
            plansza[6] == plansza[7] == plansza[8] == symbol or
            # Sprawdzenie pionów
            plansza[0] == plansza[3] == plansza[6] == symbol or
            plansza[1] == plansza[4] == plansza[7] == symbol or
            plansza[2] == plansza[5] == plansza[8] == symbol or
            # Sprawdzenie przekątnych
            plansza[0] == plansza[4] == plansza[8] == symbol or
            plansza[2] == plansza[4] == plansza[6] == symbol):
        return True
    return False


def gra():
    print("Witaj w grze Kółko i Krzyżyk!")
    print("Ty grasz jako 'X', komputer jako 'O'")
    print("Wybierz pozycję wpisując numer od 1 do 9")

    wyswietl_plansze_pomocnicza()

    while True:
        # Ruch gracza
        pozycja = ruch_gracza()
        plansza[pozycja] = "X"
        wyswietl_plansze()

        # Sprawdź czy gracz wygrał
        if sprawdz_wygrana("X"):
            print("Gratulacje! Wygrałeś!")
            break

        # Sprawdź remis
        if " " not in plansza:
            print("Remis!")
            break

        # Ruch komputera
        print("Komputer wykonuje ruch...")
        pozycja = ruch_komputera()
        plansza[pozycja] = "O"
        wyswietl_plansze()

        # Sprawdź czy komputer wygrał
        if sprawdz_wygrana("O"):
            print("Komputer wygrywa! Przegrałeś.")
            break


# Rozpoczęcie gry
gra()
