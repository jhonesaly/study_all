import networkx as nx
import sys
import matplotlib.pyplot as plt
from matplotlib.image import imread
import os

os.system('cls')

# Importa outputs de gen_rand_praph.py

sys.path.append('modules')
import modules.gen_rand_graph as scr1

vert = scr1.vert
arest = scr1.arest
weight_arest = scr1.weight_arest

# img = imread("graph.png")
# plt.imshow(img)

# Executa o algoritmo de Prim

G = nx.Graph()
G.add_nodes_from(vert)

orig, dest = zip(*arest)

for i in range(len(arest)):
    G.add_edge(orig[i], dest[i], weight=weight_arest[i])

print(G)

x, y = zip(*vert)
mst = nx.minimum_spanning_tree(G, weight='weight')
pos = {vert[i]: (x[i], y[i]) for i in range(len(vert))}
nx.draw(G, pos, with_labels=True)
nx.draw(mst, pos, with_labels=True, node_color='red', node_size=100, font_size=12, width=2, edge_color='red')
plt.show()