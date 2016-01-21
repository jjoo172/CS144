import json
from pprint import pprint
import networkx as nx
import matplotlib.pyplot as plt

with open('net_sci_coauthorships.txt') as data_file:    
    data = json.load(data_file)



#!/usr/bin/env python
"""
Random graph from given degree sequence.
Draw degree rank plot and graph with matplotlib.
"""

G = nx.Graph()

# initialize nodes in graph
for node_key in data:
	G.add_node(node_key)

#initialize edges
for node_key in data:
	#node is a dictionary
	for value in data[node_key]:
		G.add_edge(node_key, value)
		#print node_key, value

#print (G.nodes())
#print (G.edges())

print ("Average clustering coefficient: " + str(nx.average_clustering(G)))

"""
degree_sequence=sorted(nx.degree(G).values(),reverse=True) # degree sequence
#print "Degree sequence", degree_sequence
dmax=max(degree_sequence)

plt.loglog(degree_sequence,'b-',marker='o')
plt.title("Degree rank plot")
plt.ylabel("degree")
plt.xlabel("rank")

# draw graph in inset
plt.axes([0.45,0.45,0.45,0.45])
Gcc=sorted(nx.connected_component_subgraphs(G), key = len, reverse=True)[0]
pos=nx.spring_layout(Gcc)
plt.axis('off')
nx.draw_networkx_nodes(Gcc,pos,node_size=20)
nx.draw_networkx_edges(Gcc,pos,alpha=0.4)

plt.savefig("degree_histogram.png")
plt.show()
"""