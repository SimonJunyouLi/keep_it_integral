from utils.misc import edge
from collections import deque

def get_longest_path(n, graph, M_frac):
    visited = [False] * n
    longest_path = []
    longest_path_epsilon = 0

    def farthest_vertex(r):
        d = [-1] * n
        parent = [-1] * n
        d[r] = 0
        q = deque([r])

        while len(q) > 0:
            v = q.popleft()
            for u in graph[v]:
                if d[u] == -1:
                    q.appendleft(u)
                    d[u] = d[v] + 1
                    parent[u] = v
        
        d_max = 0
        farthest = -1

        for w in graph:
            if (d[w] > d_max):
                d_max = d[w]
                farthest = w
        
        return farthest, parent

    for v in graph:
        if visited[v]:
            continue

        path = []
        epsilon = 1
        v1, _ = farthest_vertex(v)
        v2, parent = farthest_vertex(v1)

        z = v2
        visited[z] = True

        while z != v1:
            e = edge(z, parent[z])
            x = M_frac[e]
            path.append(e)
            epsilon = min(epsilon, min(x, 1 - x))
            z = parent[z]
            visited[z] = True
        
        if len(path) > len(longest_path):
            longest_path = path
            longest_path_epsilon = epsilon

    return longest_path, longest_path_epsilon