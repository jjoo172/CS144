import json
from pprint import pprint
import networkx as nx
import matplotlib.pyplot as plt
import plotly.plotly as py
import numpy as np

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

print ("Overall clustering coefficient: " + str(nx.transitivity(G)))
print ("Average clustering coefficient: " + str(nx.average_clustering(G)))
print ("Diameter: " + str(nx.diameter(G)))
print ("Average Diameter: " + str(nx.average_shortest_path_length(G)))

# iterating through every node in graph, getting its degree.
degrees = []

for node in nx.nodes(G):
	degrees.append(nx.degree(G, node))
	#num_nodes = degree(node);

degrees.sort()

#plot the histogram of the degrees
plt.hist(degrees)
plt.title("Number of vertices with various degrees")
plt.xlabel("Degree")
plt.ylabel("Number of vertices")

fig = plt.gcf()

plt.show()

# plot the ccdf by first finding the total amount, and then
# iterating through each value of x, and determining the probability of that x
# over the total.

degrees.sort()

ccdf = []

total = sum(degrees)

i = 0.0
# iterate through each degree, denoted by i
while (i <= max(degrees)):
	running_sum = 0.0
	# for each node, if the degree is less than or equal to i, add it to the running_sum
	for n in degrees:
		if n <= i:
			running_sum += n
	i = i + 1.0
	ccdf.append(1 - (running_sum/total))

plt.plot(ccdf)
plt.show()


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