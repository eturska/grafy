import networkx as nx

J = nx.erdos_renyi_graph(10, 0.4)
print(nx.is_tree(J))
print(nx.is_bipartite(J))
print(nx.cycle_basis(J, 0))


