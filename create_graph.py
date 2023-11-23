import networkx as nx
import random
import matplotlib.pyplot as plt

# Undirected graph
G = nx.Graph()
nodes = [1,2,3,4]
G.add_nodes_from(nodes)
print("Number of nodes = ", G.number_of_nodes())

edges = []
for i in range(0,4):
    j = i + 1
    for j in range(0, 4):
        if i != j:
            edges.append([nodes[i], nodes[j], random.randrange(0,100)])

G.add_weighted_edges_from(edges)
G.remove_edge(1, 3)
print("Number of edges = ", G.number_of_edges())

UG = G.to_undirected()
print("Undirected graph: ", list(UG.edges.data('weight')))

# Compute the strength of each node by adding the weights of edges incident with the node
print("Undirected graph, node strength: ", UG.degree(weight='weight'))

# Directed graph
DG = nx.DiGraph()
DG.add_nodes_from(nodes)
DG.add_weighted_edges_from(edges)
"""
for u, v, weight in DG.edges(data="weight"):
    DG[u][v]["weight"] = random.randrange(0,100)
"""

print("in", DG.in_edges.data())
print("out", DG.out_edges.data())

"""
# Compute the strength of each node in two ways
# outgoing edges
iter = 0
outgoing_weights = []
total_outgoing_weights = 0.000
for u, v, weight in DG.out_edges.data(data="weight"):
    if u == nodes[iter]:
        total_outgoing_weights += weight
    else:
        outgoing_weights.append([u, total_outgoing_weights])
        total_outgoing_weights = 0.000
        if iter < 3:
            iter += 1

# incoming edges
iter = 0
incoming_weights = []
total_incoming_weights = 0.000
for u, v, weight in (DG.in_edges.data(data="weight")):
    if u == nodes[iter]:
        total_incoming_weights += weight
    else:
        incoming_weights.append([u, total_incoming_weights])
        total_incoming_weights = 0.000
        if iter < 3:
            iter += 1

# print("incoming", incoming_weights)
# print("outgoing", outgoing_weights)
"""

print("outgoing: ", DG.in_degree(weight='weight'))
print("incoming: ", DG.out_degree(weight='weight'))

# Drawing graphs
options = {
    "font_size": 18,
    "node_size": 1000,
    "node_color": "white",
    "edgecolors": "black",
    "linewidths": 2,
    "width": 3,
    "arrowsize":20,
    "arrows": True
}

nx.draw_networkx(G, pos=nx.circular_layout(G), **options)
plt.savefig('fig1.png')
plt.show()

nx.draw_networkx(UG, **options)
plt.savefig('fig2.png')
plt.show()

pos=nx.spring_layout(DG)
nx.draw_networkx(DG, pos, **options, with_labels=True)
labels = nx.get_edge_attributes(DG, "weight")
nx.draw_networkx_edge_labels(DG, pos, edge_labels=labels, label_pos=.66)
plt.savefig('fig3.png')
plt.show()
