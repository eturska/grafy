ilosc_wierzcholkow = int(input('Podaj liczbe wierzcholkow: '))
macierz_sasiedztwa = [[0 for i in range(ilosc_wierzcholkow)] for j in range(ilosc_wierzcholkow)]
ilosc_krawedzi = int(input('Podaj ilosc krawedzi: '))
for i in range(ilosc_krawedzi):
    poczatek = int(input('Podaj poczatek krawedzi nr {}: '.format(i)))
    koniec = int(input('Podaj koniec krawedzi nr {}: '.format(i)))
    if poczatek == koniec:
        print('Poczatek i koniec krawedzi nie moze byc tym samym wierzcholkiem')
    macierz_sasiedztwa[poczatek][koniec] = 1
    macierz_sasiedztwa[koniec][poczatek] = 1
print('Macierz sasiedztwa wyglada nastepujaco: {}'.format(macierz_sasiedztwa))

lista_stopni = []
stopien_grafu = 0
for i in range(ilosc_wierzcholkow):
    stopien_wierzcholka = 0;
    for j in range(ilosc_wierzcholkow):
        stopien_wierzcholka += macierz_sasiedztwa[i][j]
        if stopien_grafu < stopien_wierzcholka:
            stopien_grafu = stopien_wierzcholka
    lista_stopni.append(stopien_wierzcholka)
    print('Stopien wierzcholka nr {} wynosi {}'.format(i, stopien_wierzcholka))
print('Stopien grafu wynosi {}'.format(stopien_grafu))
print(lista_stopni)
