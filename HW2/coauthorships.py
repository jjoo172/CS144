import json
from pprint import pprint
import networkx as nx
import matplotlib.pyplot as plt
import plotly.plotly as py
import numpy as np

with open('net_sci_coauthorships.txt') as data_file:    
    data = json.load(data_file)


G = nx.Graph()

# initialize nodes in graph
for node_key in data:
	G.add_node(node_key)

#initialize edges
for node_key in data:
	#node is a dictionary
	for value in data[node_key]:
		G.add_edge(node_key, value)


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
plt.hist(degrees, max(degrees))
plt.title("Number of vertices with various degrees")
plt.xlabel("Degree")
plt.ylabel("Number of vertices")

fig = plt.gcf()

plt.show()


dx = .01

# x is list of degrees: 1, 2, 3, 4, etc.
X = []
i = 0
while (i <= max(degrees)):
	X.append(i)
	i += 1

x_array = np.array(X)

# y is count for a given degree
Y  = []
i = 0
while (i <= max(degrees)):
	Y.append(degrees.count(i))
	i += 1

y_array = np.array(Y)

# Normalize the data to a proper PDF
y_array = y_array / (dx*y_array).sum()

# Compute the CDF
CY = np.cumsum(y_array*dx)

print x_array
print y_array

# Plot both
plt.plot(x_array, 1-CY)

plt.show()


"""
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
plt.title("CCDF")
plt.xlabel("Degree")
plt.ylabel("CCDF")
plt.show()
"""
