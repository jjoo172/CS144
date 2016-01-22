import json
from pprint import pprint
import networkx as nx
import matplotlib.pyplot as plt
import plotly.plotly as py
import numpy as np
import fetcher
import Queue as q
import time

bfs_queue = q.Queue()
visited_links = []

G = nx.DiGraph()
G_undir = nx.Graph()
root = "http://www.caltech.edu/"

bfs_queue.put(root)
G.add_node(root)
G_undir.add_node(root)

depth = 0

outcount = {}

while (bfs_queue.empty() == False and depth < 2001):
	cur_link = bfs_queue.get()
	links = fetcher.fetch_links(cur_link)

	if links != None:
		#iterate through children
		for link in links:
			if "caltech.edu" in link and link not in visited_links:
				time.sleep(0.5)

				# update graph and visited_links array
				bfs_queue.put(link)
				visited_links.append(link)

				# add to dictionary, as well as how many hyperlinks it has
				try:
					hyperlinks = fetcher.fetch_links(link)
					outcount[link] = len(hyperlinks)
				except:
					outcount[link] = 0

				#if it gets to this part, it will be a new link. Thus, add this link to G.
				G.add_node(link)
				G_undir.add_node(link)

				print link
				#add edges
				depth += 1

			# add edge from link to child
			G.add_edge(cur_link, link)
			G_undir.add_edge(cur_link, link)


# data stuff
print ("Overall clustering coefficient: " + str(nx.transitivity(G_undir)))

#since average clustering coefficient can't be calculated for a directed graph, use a non-directed
# version to  calculate average clustering coefficient.
print ("Average clustering coefficient: " + str(nx.average_clustering(G_undir)))
print ("Diameter: " + str(nx.diameter(G_undir)))
print ("Average Diameter: " + str(nx.average_shortest_path_length(G_undir)))

# Get out degrees from our dictionary
outdegrees = []

for entry in outcount:
	outdegrees.append(outcount[entry])
	#num_nodes = degree(node);

outdegrees.sort()

#plot the histogram of the out-degrees
plt.hist(outdegrees, max(outdegrees))
plt.title("Hyperlinks per page")
plt.xlabel("Links on page")
plt.ylabel("Count")

fig = plt.gcf()

plt.show()


# iterating through every node in graph, getting its degree.
indegrees = []

for node in nx.nodes(G):
	indegrees.append(G.in_degree(node))
	#num_nodes = degree(node);

indegrees.sort()

#plot the histogram of the in-degrees
plt.hist(indegrees, max(indegrees))
plt.title("Number of references to page")
plt.xlabel("References to page")
plt.ylabel("Count")

fig = plt.gcf()

plt.show()

# plot the ccdf by first finding the total amount, and then
# iterating through each value of x, and determining the probability of that x
# over the total.


##################################################
## CCDF
dx = .01

# x is list of degrees: 1, 2, 3, 4, etc.
X = []
i = 0
while (i <= max(outdegrees)):
	X.append(i)
	i += 1

x_array = np.array(X)

# y is count for a given degree
Y  = []
i = 0
while (i <= max(outdegrees)):
	Y.append(outdegrees.count(i))
	i += 1

y_array = np.array(Y)

# Normalize the data to a proper PDF
y_array = y_array / (dx*y_array).sum()

# Compute the CDF
CY = np.cumsum(y_array*dx)

# Plot both
plt.plot(x_array, 1-CY)
plt.title("CCDF")
plt.xlabel("Degree")
plt.ylabel("CCDF")
plt.show()



##################################################
## CCDF
dx = .01

# x is list of degrees: 1, 2, 3, 4, etc.
X = []
i = 0
while (i <= max(indegrees)):
	X.append(i)
	i += 1

x_array = np.array(X)

# y is count for a given degree
Y  = []
i = 0
while (i <= max(indegrees)):
	Y.append(indegrees.count(i))
	i += 1

y_array = np.array(Y)

# Normalize the data to a proper PDF
y_array = y_array / (dx*y_array).sum()

# Compute the CDF
CY = np.cumsum(y_array*dx)

# Plot both
plt.plot(x_array, 1-CY)
plt.title("CCDF")
plt.xlabel("Degree")
plt.ylabel("CCDF")
plt.show()
