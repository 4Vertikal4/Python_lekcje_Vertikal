print("Witaj, Geralt! Zostałeś wezwany do wioski Podgórze. Mieszkańcy są "
      "terroryzowani przez potwora.")
print("Sołtys prosi Cię o pomoc. Co robisz?")

wybor = input("1. Przyjmujesz zlecenie. 2. Odmawiasz.\n")

if wybor == "1":
    print("Wyruszasz do lasu w poszukiwaniu potwora.")
    print("Nagle słyszysz szelest w krzakach. Co robisz?")
    wybor2 = input("1. Atakujesz. 2. Czekasz.\n")
    if wybor2 == "1":
        print("Z krzaków wyskakuje Leszy! Rozpoczyna się walka!")
        print("Leszy atakuje Cię swoimi korzeniami!")
        wybor_walki = input("1. Bronisz się znakiem Quen. 2. Kontratakujesz mieczem.\n")
        if wybor_walki == "1":
            print("Znak Quen chroni Cię przed atakiem. Masz chwilę na kontratak!")
            print("Zadajesz Leszemu poważny cios!")
            print("Leszy wycofuje się głębiej w las.")
            print("Czy chcesz go ścigać?")
            wybor_poscig = input("1. Ścigasz Leszego. 2. Wracasz do wioski.\n")
            if wybor_poscig == "1":
                print("Ścigasz Leszego, ale wpadasz w jego pułapkę! Koniec Gry.")
            elif wybor_poscig == "2":
                print("Wracasz do wioski po pomoc. Mieszkańcy są Ci wdzięczni.")
                print("Razem planujecie zasadzkę na Leszego. Udaje się go pokonać! "
                      "Wygrałeś!")
        elif wybor_walki == "2":
            print("Próbujesz kontratakować, ale Leszy jest zbyt szybki.")
            print("Korzenie oplątują Cię i unieruchamiają!")
            print("Leszy wysysa z Ciebie życie. Koniec Gry.")
        else:
            print("Nie rozumiesz polecenia. Leszy Cię atakuje! Koniec Gry.")
            print(r"""
  .------..
     -          -
   /              \
 /                   \
/    .--._    .---.   |
|  /      -__-     \   |
| |                 |  |
 ||     ._   _.      ||
 ||      o   o       ||
 ||      _  |_      ||
 C|     (o\_/o)     |O
  \      _____      /      
    \ ( /#####\ ) /       
     \  `====='  /
      \  -___-  /
       |       |
       /-_____-\
     /           \
   /               \
  /__|  SOŁTYS  |__\
  | ||           |\ \
""")
    elif wybor2 == "2":
        print("Z krzaków wychodzi przestraszony wieśniak. Opowiada Ci o "
              "legowisku potwora.")
        print("Mówi, że potwór ukrywa się w starej, opuszczonej kapliczce na wzgórzu.")
        print("Wieśniak ostrzega, że kapliczka jest nawiedzona i straszy tam.")
        wybor_kapliczka = input("1. Idziesz do kapliczki. 2. Wracasz do wioski po pomoc.\n")
        if wybor_kapliczka == "1":
            print("Wchodzisz do kapliczki. Jest ciemno i czuć stęchlizną.")
            print("Nagle słyszysz szelest i widzisz czerwone oczy w ciemności!")
            wybor_walki_kapliczka = input("1. Atakujesz potwora. "
                                          "2. Używasz znaku Igni, żeby go przepłoszyć.\n")
            if wybor_walki_kapliczka == "1":
                print("Rzucasz się na potwora z mieczem!")
                print("Okazuje się, że to tylko stary, zagubiony pies. "
                      "Wracasz do wioski ze wstydem. Koniec Gry.")
            elif wybor_walki_kapliczka == "2":
                print("Używasz znaku Igni! Potwór wyje z bólu i ucieka!")
                print("Znajdujesz w kapliczce skarb ukryty przez potwora!")
                print("Wracasz do wioski jako bohater! Wygrałeś!")
            else:
                print("Nie rozumiesz polecenia. Potwór Cię atakuje! Koniec Gry.")
                print(r"""
  .------..
     -          -
   /              \
 /                   \
/    .--._    .---.   |
|  /      -__-     \   |
| |                 |  |
 ||     ._   _.      ||
 ||      o   o       ||
 ||      _  |_      ||
 C|     (o\_/o)     |O
  \      _____      /      
    \ ( /#####\ ) /       
     \  `====='  /
      \  -___-  /
       |       |
       /-_____-\
     /           \
   /               \
  /__|  SOŁTYS  |__\
  | ||           |\ \
""")
        elif wybor_kapliczka == "2":
            print("Wracasz do wioski po pomoc. Mieszkańcy są przerażeni, "
                  "ale zgadzają się pomóc.")
            print("Razem organizujecie wyprawę do kapliczki.")
            print("W kapliczce okazuje się, że potworem był tylko przestraszony "
                  "wieśniak przebrany za upiora. Wygrałeś, rozwiązując problem pokojowo!")
        else:
            print("Nie rozumiesz polecenia. Wieśniak ucieka, a Ty zostajesz "
                  "sam w lesie. Koniec Gry.")
            print(r"""
  .------..
     -          -
   /              \
 /                   \
/    .--._    .---.   |
|  /      -__-     \   |
| |                 |  |
 ||     ._   _.      ||
 ||      o   o       ||
 ||      _  |_      ||
 C|     (o\_/o)     |O
  \      _____      /      
    \ ( /#####\ ) /       
     \  `====='  /
      \  -___-  /
       |       |
       /-_____-\
     /           \
   /               \
  /__|  SOŁTYS  |__\
  | ||           |\ \
""")
    else:
        print("Nie rozumiesz polecenia. Marnujesz czas. Leszy Cię atakuje! Koniec Gry.")
        print(r"""
  .------..
     -          -
   /              \
 /                   \
/    .--._    .---.   |
|  /      -__-     \   |
| |                 |  |
 ||     ._   _.      ||
 ||      o   o       ||
 ||      _  |_      ||
 C|     (o\_/o)     |O
  \      _____      /      
    \ ( /#####\ ) /       
     \  `====='  /
      \  -___-  /
       |       |
       /-_____-\
     /           \
   /               \
  /__|  SOŁTYS  |__\
  | ||           |\ \
""")
elif wybor == "2":
    print("Odmawiasz pomocy. Wioska zostaje zniszczona. Koniec Gry.")
else:
    print("Nie rozumiesz polecenia. Sołtys jest wściekły i wygania Cię z wioski. "
          "Koniec Gry.")
    print(r"""
  .------..
     -          -
   /              \
 /                   \
/    .--._    .---.   |
|  /      -__-     \   |
| |                 |  |
 ||     ._   _.      ||
 ||      o   o       ||
 ||      _  |_      ||
 C|     (o\_/o)     |O
  \      _____      /      
    \ ( /#####\ ) /       
     \  `====='  /
      \  -___-  /
       |       |
       /-_____-\
     /           \
   /               \
  /__|  SOŁTYS  |__\
  | ||           |\ \
""")
