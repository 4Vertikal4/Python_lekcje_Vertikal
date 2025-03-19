print("Witaj w kalkulatorze zrzutki na paliwo")
koszt_paliwa = input("Podaj całkowity koszt paliwa (np. 150.00):\n")
koszt_paliwa = float(koszt_paliwa)
ilosc_osob = input("Ile osób dzieli się kosztami?\n")
ilosc_osob = int(ilosc_osob)
koszt_na_osobe = koszt_paliwa / ilosc_osob
kwota_zaokraglona = round(koszt_na_osobe, 2)
print(f"Każdy osoba powinnna zapłacić: {kwota_zaokraglona:.2f} zł.")
