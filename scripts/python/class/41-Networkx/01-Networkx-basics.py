import networkx as nx
import matplotlib.pyplot as plt
'''
G=nx.Graph()

G.add_node([2, 5, 7, 8])

G.add_edge(1, 2)
'''

DG=nx.DiGraph()
DG.add_weighted_edges_from([(1,2,0.5), (3,1,0.75)])
DG.out_degree(1,weight='weight')
DG.degree(1,weight='weight')
DG.successors(1)
DG.neighbors(1)

nx.draw(DG)
nx.draw_random(DG)
nx.draw_circular(DG)
nx.draw_spectral(DG)

plt.show()
