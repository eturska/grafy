graf1 = {'1': ['2','3','5'], '2':['1','5'], '3':['1','4'], '4':['3','5'], '5':['1','2','4', '6'],'6':['5']}
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