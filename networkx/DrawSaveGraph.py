import networkx as nx
import matplotlib.pyplot as plt
import scipy as sp

J = nx.erdos_renyi_graph(4, 0.5)
plt.figure(1, figsize=(2, 2))
nx.draw(J, node_size=2)
plt.show()
A = nx.adjacency_matrix(J)
print(A.todense())
nx.write_adjlist(J, 'lista_sasiedztwa.txt')


