from collections import deque

graph = {}

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
 
            for i in graph[front]:
                cur = i[0]
                if not visited[cur]:
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

def find_longest_path(u, v, parent):
    path = []
    while v != u:
        path.append(v)
        v = parent[v]
    path.append(u)

    pEdges = []

    for i in range(len(path)-1):
        for e in graph[path[i]]:
            if e[0] == path[i+1]:
                pEdges.append(e)

    return pEdges


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
            
    node, Dis, _ = BFS(1, n)
    node_2, LongDis, parent = BFS(node, n)

    longest_path = find_longest_path(node, node_2, parent)
    print("Longest Path:", longest_path)





