from collections import deque

# variables to be used
# in both functions
n, m = map(int, input().split())
edges = []
graph = [[0 for _ in range(n)] for _ in range(n)]
cycles = []

def integral(num):
    return abs(num-1) < 1e-5 or abs(num) < 1e-5

# Function to mark the vertex with
# different colors for different cycles
def dfs_cycle(u, p, color: list, par: list): 
    print("cycles", cycles)
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
        v.append((u, cur, graph[u][cur]))

		# backtrack the vertex which are
		# in the current cycle thats found
        while cur != u:
            cur = par[cur]
            v.append((par[cur], cur, graph[cur][par[cur]]))
        cycles.append(v)
        return

    par[u] = p

	# partially visited.
    color[u] = 1

	# simple dfs on graph
    for v in range(len(graph[u])):
		# if it has not been visited previously
        if v == par[u]: continue
        if not integral(graph[u][v]): 
            print(u, v)
            dfs_cycle(v, u, color, par)

	# completely visited.
    color[u] = 2
     
def BFS(u, n):
        # marking all nodes as unvisited
        visited = [False for i in range(n)]
        # mark all distance with -1
        distance = [-1 for i in range(n)]
        parent = [-1 for i in range(n)]  # To keep track of the parent node in the path
 
        # distance of u from u will be 0
        distance[u] = 0
        # in-built library for queue which performs fast operations on both the ends
        queue = deque()
        queue.append(u)
        # mark node u as visited
        visited[u] = True
 
        while queue:
 
            # pop the front of the queue(0th element)
            front = queue.popleft()
            # loop for all adjacent nodes of node front

            # print(graph)
 
            for v in range(len(graph[front])):
                cur = v
                if not visited[cur] and graph[front][cur] != 0:
                    # mark the ith node as visited
                    visited[cur] = True
                    # make distance of i , one more than distance of front
                    distance[cur] = distance[front]+1
                    parent[cur] = front  # Update the parent node
                    # Push node into the stack only if it is not visited already
                    queue.append(cur)
 
        maxDis = 0
 
        # get farthest node distance and its index
        for i in range(n):
            if distance[i] > maxDis:
 
                maxDis = distance[i]
                nodeIdx = i
 
        return nodeIdx, maxDis, parent

def BFS_forest(n):
    visited = [False for i in range(n)]
    components = []  # List to store the components in the forest

    for u in range(n):
        if not visited[u] and not set(graph[u]) == {0}:
            # Start a BFS from unvisited nodes to explore a component
            component = []
            queue = deque()
            queue.append(u)
            visited[u] = True

            while queue:
                front = queue.popleft()
                component.append(front)

                for i in range(len(graph[front])):
                    cur = i
                    if not visited[cur] and graph[front][cur] != 0:
                        visited[cur] = True
                        queue.append(cur)

            components.append(component)
    return components

def find_longest_path(u, v, parent):
    path = []
    pEdges = []

    while v != u:
        path.append(v)
        v = parent[v]
    path.append(u)

    for i in range(len(path)-1):
        for e in range(len(graph[path[i]])):
            if e == path[i+1]:
                pEdges.append((path[i], e, graph[path[i]][e]))

    return pEdges

def round_fractional_matching(n, m, edges):
    if not edges:
        return []

    integral_matching = []

    # print("edges in the graph: ", edges)
    remove = []
    for u, v, x in edges:
        if abs(x-1) < 1e-5 or abs(x-0) < 1e-5:
            integral_matching.append((u,v))
            remove.append((u,v,x))
    edges = [edge for edge in edges if edge not in remove]

    if not edges: return integral_matching

    color = [0] * n
    par = [0] * n
    dfs_cycle(edges[0][0], 0, color, par)
    
    while cycles:
        cycle = cycles[0]

        c0, c1, c2 = [], [], []
        cnt = 0
        epsilon = cycle[0][2]

        for u, v, x in cycle:
            if 1 - x < epsilon:
                epsilon = 1-x
            elif x < epsilon:
                epsilon = x
        
        for u, v, x in cycle:
            if u > v: u, v = v, u
            c0.append((u,v,x))
            if cnt % 2 == 0:
                c1.append((u, v, x-epsilon))
                c2.append((u, v, x+epsilon))
            else:
                c1.append((u, v, x+epsilon))
                c2.append((u, v, x-epsilon))
            cnt+=1

        cnt1, cnt2 = [], []
        for i in range(len(c1)):
            if integral(c1[i][2]): cnt1.append(c1[i])
            if integral(c2[i][2]): cnt2.append(c2[i])

        edges = [edge for edge in edges if edge not in c0]
        if len(cnt1) >= len(cnt2):
            for u, v, x in cnt1:
                if abs(x-1) < 1e-5: integral_matching.append((u,v))
            c1 = [e for e in c1 if e not in cnt1]
            edges.extend(c1)
        else:
            for u, v, x in cnt2:
                if abs(x-1) < 1e-5: integral_matching.append((u,v))
            c2 = [e for e in c2 if e not in cnt2]
            edges.extend(c2)

        for i, j in zip(range(n), range(n)):
            graph[i][j] = 0

        for u, v, x in edges:
            graph[u][v] = x
            graph[v][u] = x

        cycles.clear()
        if edges:
            color = [0] * n
            par = [0] * n
            dfs_cycle(edges[0][0], 0, color, par)

    ########## H (edges) is acyclic ###########

    while edges:
        print("in edges")
        print("edges", edges)
        for i, j in zip(range(n), range(n)):
            graph[i][j] = 0
        for u, v, x in edges:
            graph[u][v] = x
            graph[v][u] = x

        longest_path = []
        components = BFS_forest(n)

        for component in components:
            node, _, _ = BFS(component[0], n)
            node_2, _, parent = BFS(node, n)

            temp_path = find_longest_path(node, node_2, parent)

            if len(temp_path) > len(longest_path):
                 longest_path = temp_path
        
        c0, c1, c2 = [], [], []
        cnt = 0
        epsilon = longest_path[0][2]

        for u, v, x in longest_path:
            if 1 - x < epsilon:
                epsilon = 1-x
            elif x < epsilon:
                epsilon = x
        
        for u, v, x in longest_path:
            if u > v: u, v = v, u
            c0.append((u,v,x))
            if cnt % 2 == 0:
                c1.append((u, v, x-epsilon))
                c2.append((u, v, x+epsilon))
            else:
                c1.append((u, v, x+epsilon))
                c2.append((u, v, x-epsilon))
            cnt+=1

        cnt1, cnt2 = [], []
        for i in range(len(c1)):
            if integral(c1[i][2]): cnt1.append(c1[i])
            if integral(c2[i][2]): cnt2.append(c2[i])

        # remove edges in the longest path
        edges = [edge for edge in edges if edge not in c0]
        print("longest", longest_path)
        print("edge after removal", edges)
        print("cnt1", cnt1)
        if len(cnt1) >= len(cnt2):
            for u, v, x in cnt1:
                if abs(x-1) < 1e-5: integral_matching.append((u,v))
            c1 = [e for e in c1 if e not in cnt1] # remove integral values from edges
            print("c1 after removal", c1)
            edges.extend(c1) # add updated non-integral values back to edges
            print("edges after addition", edges)
        else:
            for u, v, x in cnt2:
                if abs(x-1) < 1e-5: integral_matching.append((u,v))
            c2 = [e for e in c2 if e not in cnt2]
            edges.extend(c2)

    return integral_matching


for _ in range(m):
    u, v, x = map(float, input().split())
    edges.append((int(u), int(v), x))

for u, v, x in edges:
    graph[u][v] = x
    graph[v][u] = x

integral_matching = round_fractional_matching(n, m, edges)

for i in integral_matching:
     print(i[0], i[1])