import random


def losowana_liczba():
    x = random.randint(1000, 10000)
    return str(x)


def pobierz_od_uzytkownika():
    return input('Podaj liczbe : ')


def wylicz_krowy(wartosci_prawidłowe, wartosci_uzytkownika):
    Cows = 0
    lista = []
    for i in range(len(wartosci_prawidłowe)):
        if wartosci_uzytkownika[i] == wartosci_prawidłowe[i]:
            Cows += 1
            lista.append(i)
    return Cows, lista


def wylicz_byki(wartosci_prawidłowe, wartosci_uzytkownika, indeksy_zajeta):
    Bulls = 0
    indeksy_zajete_byki = indeksy_zajeta.copy()
    for i, wartosc in enumerate(wartosci_prawidłowe):
        if not i in indeksy_zajeta:
            for j, liczba in enumerate(wartosci_uzytkownika):
                if i != j and liczba == wartosc and j not in indeksy_zajete_byki:
                    Bulls += 1
                    indeksy_zajeta.append(i)
                    indeksy_zajete_byki.append(j)
                    break
    return Bulls


def main():
    trial = 0
    wylosowana_liczba = losowana_liczba()

    print(wylosowana_liczba)
    while True:
        liczba_uzytkownika = pobierz_od_uzytkownika()
        krowy, zajete = wylicz_krowy(liczba_uzytkownika, wylosowana_liczba)
        byki = wylicz_byki(wylosowana_liczba, liczba_uzytkownika, zajete)
        if krowy == 4:
            print(f'Wygrałes, Liczba prob {trial}')
            break
        else:
            print(f'Liczba krów: {krowy}, a byki {byki}')
            trial += 1


main()

