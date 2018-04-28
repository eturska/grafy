graf1 = {}
wierzcholek1 = input("Podaj wierzcholek poczatkowy: ")
ilosc_wierzcholkow = len(graf1)


def dfs(graf, wierzcholek, odwiedzone):
    if wierzcholek not in odwiedzone:
        odwiedzone.append(wierzcholek)
        for n in graf[wierzcholek]:
            dfs(graf, n, odwiedzone)
    return odwiedzone


visited = dfs(graf1, wierzcholek1, [])
print(visited)
lista_stopni_parzystych = []
if ilosc_wierzcholkow == len(visited):
    print("graf jest spojny")
    for key, value in graf1.items():
        if len(value) % 2 == 0:
            lista_stopni_parzystych.append(len(value))
    if len(lista_stopni_parzystych) == ilosc_wierzcholkow:
        print('graf jest eulerowski')
    else:
        if len(graf1) - len(lista_stopni_parzystych) == 2:
            print("graf jest poleulerowski")
        else:
            print("graf nie jest eulerowski")

else:
    print("graf nie jest spojny")
