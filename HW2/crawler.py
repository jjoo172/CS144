import fetcher
import Queue as q

bfs_queue = q.Queue()

links = fetcher.fetch_links("http://www.caltech.edu/")

for link in links:
	if "caltech.edu" in link:
		bfs_queue.put(link)

while (bfs_queue.empty() == False):
	try child_links = fetcher.fetch_links(bfs_queue.get())
	