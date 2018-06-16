import networkx as nx

G = nx.Graph()

for a in range(8):
    G.add_node(a)
print(G.nodes())

G.add_edge(6, 2)
G.add_edge(2, 1)
G.add_edge(2, 3,)
G.add_edge(3, 1)
G.add_edge(3, 4)
G.add_edge(1, 7)
G.add_edge(1, 0)
G.add_edge(1, 4)
G.add_edge(4, 7)
G.add_edge(4, 5)
G.add_edge(4, 0)
G.add_edge(7, 0)
G.add_edge(7, 5)
G.add_edge(0, 5)

for a in range(8):
    print("Stopień wierzchołka {} wynosi {}".format(a, G.degree(a)))

print("Graf ma {} krawędzi" .format(G.number_of_edges()))
print("Graf ma {} wierzchołków" .format(G.number_of_nodes()))

number_of_leaves = 0
for a in range(8):
    if G.degree(a) == 1:
        number_of_leaves = number_of_leaves + 1

print("Graf ma {} liści" .format(number_of_leaves))
number_of_3s = 0
for a in range(8):
    if G.degree(a) == 3:
        number_of_3s = number_of_3s + 1
print("Graf ma {} wierzchołków trzeciego stopnia" .format(number_of_3s))




