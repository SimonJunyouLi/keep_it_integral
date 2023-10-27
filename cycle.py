# variables to be used
# in both functions
graph = {}
cycles = []


# Function to mark the vertex with
# different colors for different cycles
def dfs_cycle(u, p, color: list,
			par: list):
	# already (completely) visited vertex.
	if color[u] == 2:
		return

	# seen vertex, but was not 
	# completely visited -> cycle detected.
	# backtrack based on parents to
	# find the complete cycle.
	if color[u] == 1:
		v = []
		cur = p
		
		for i in graph[cur]:
			if i[0] == u:
				v.append(i)

		# backtrack the vertex which are
		# in the current cycle thats found
		while cur != u:
			for i in graph[par[cur]]:
				if i[0] == cur:
					v.append(i)
			cur = par[cur]


		cycles.append(v)

		return

	par[u] = p

	# partially visited.
	color[u] = 1

	# simple dfs on graph
	for v in graph[u]:

		# if it has not been visited previously
		if v[0] == par[u]:
			continue
		dfs_cycle(v[0], u, color, par)

	# completely visited.
	color[u] = 2

# add the edges to the graph
def addEdge(u, v):
	graph[u].append(v)
	graph[v].append(u)

# Function to print the cycles
def printCycles():

	# print all the vertex with same cycle
	for i in range(len(cycles)):

		# Print the i-th cycle
		print("Cycle Number %d:" % (i+1), end = " ")
		for x in cycles[i]:
			print(x, end = " ")
		print()

# Driver Code
if __name__ == "__main__":

	# arrays required to color the
	# graph, store the parent of node

	
	n, m = map(int, input().split())
	edges = []
	color = [0] * n
	par = [0] * n

	for _ in range(m):
		u, v, x = map(float, input().split())   
		edges.append((int(u), int(v), x))
	
	for u, v, x in edges:
		if u not in graph:
			graph[u] = []
		if v not in graph:
			graph[v] = []
		graph[u].append((v, (u, v, x)))
		graph[v].append((u, (u, v, x)))

	# call DFS to mark the cycles
	dfs_cycle(1, 0, color, par)

	# function to print the cycles
	printCycles()
