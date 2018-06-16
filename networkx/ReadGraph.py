import networkx as nx
import matplotlib.pyplot as plt
import scipy as sp

G = nx.read_adjlist('GraphTests\Test3.txt', comments='#',create_using=None,
delimiter=' ',nodetype=None, encoding='utf-8')
plt.figure(1, figsize=(2, 2))
nx.draw(G, node_size=2)
plt.show()

H = nx.complement(G)
plt.figure(1, figsize=(2, 2))
nx.draw(H, node_size=2)
plt.show()

J = nx.line_graph(G)
plt.figure(1, figsize=(2, 2))
nx.draw(J, node_size=2)
plt.show()
