import collections

ilosc_wierzcholkow = int(input('Podaj liczbe wierzcholkow: '))
macierz_sasiedztwa = [[0 for i in range(ilosc_wierzcholkow)] for j in range(ilosc_wierzcholkow)]
ilosc_krawedzi = int(input('Podaj ilosc krawedzi: '))

# # grafy skierowane
#
# lista_początków = []
# lista_końców = []
# for i in range(ilosc_krawedzi):
#     poczatek = int(input('Podaj poczatek krawedzi nr {}: '.format(i)))
#     lista_początków.append(poczatek)
#     koniec = int(input('Podaj koniec krawedzi nr {}: '.format(i)))
#     lista_końców.append(koniec)
#     if poczatek == koniec:
#         print('Poczatek i koniec krawedzi nie moze byc tym samym wierzcholkiem')
#     macierz_sasiedztwa[poczatek][koniec] = 1
#     macierz_sasiedztwa[koniec][poczatek] = 1
#
# stopien_wchodzacy = []
# stopien_wychodzacy = []
# counter = collections.Counter(lista_początków)
# counter1 = collections.Counter(lista_końców)
# stopien_wychodzacy = list(counter.values())
# stopien_wchodzacy = list(counter1.values())
# print(sum(stopien_wychodzacy)/ilosc_wierzcholkow)
# print(sum(stopien_wchodzacy)/ilosc_wierzcholkow)

# grafy nieskierowane
lista_stopni = []
for i in range(ilosc_krawedzi):
    poczatek = int(input('Podaj poczatek krawedzi nr {}: '.format(i)))
    koniec = int(input('Podaj koniec krawedzi nr {}: '.format(i)))
    if poczatek == koniec:
        print('Poczatek i koniec krawedzi nie moze byc tym samym wierzcholkiem')
    macierz_sasiedztwa[poczatek][koniec] = 1
    macierz_sasiedztwa[koniec][poczatek] = 1

for i in range(ilosc_wierzcholkow):
    stopien_wierzcholka = 0
    for j in range(ilosc_wierzcholkow):
        stopien_wierzcholka += macierz_sasiedztwa[i][j]
    lista_stopni.append(stopien_wierzcholka)
średni_stopień_grafu = sum(lista_stopni)/len(lista_stopni)
print('Sredni stopień wierzchołka to {}' .format(średni_stopień_grafu))
