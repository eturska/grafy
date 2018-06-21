ilosc_wierzcholkow = int(input('Podaj liczbe wierzcholkow: '))
macierz_sasiedztwa = [[0 for i in range(ilosc_wierzcholkow)] for j in range(ilosc_wierzcholkow)]
ilosc_krawedzi = int(input('Podaj ilosc krawedzi: '))
for i in range(ilosc_krawedzi):
    poczatek = int(input('Podaj poczatek krawedzi nr {}: '.format(i)))
    koniec = int(input('Podaj koniec krawedzi nr {}: '.format(i)))
    macierz_sasiedztwa[poczatek][koniec] = 1
    macierz_sasiedztwa[koniec][poczatek] = 1

loops = 0
for i in range(ilosc_wierzcholkow):
    if macierz_sasiedztwa[i][i] == 1:
        loops = loops + 1

if loops == 0:
    print('Graf nie ma pętli')
else:
    print('Graf ma pętle')
