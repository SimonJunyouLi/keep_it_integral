from utils.misc import edge

def get_cycle(graph, n, M_frac):
    visited = [False] * n
    parent = [-1] * n
    start = -1
    end = -1
    cycle = []
    epsilon = 0

    def dfs(v, p):
        visited[v] = True
        for u in graph[v]:
            if u == p:
                continue
            if visited[u]:
                nonlocal start, end
                start = u
                end = v
                return True
            parent[u] = v
            if dfs(u, v):
                return True
        return False

    for v in graph:
        if (not visited[v]) and dfs(v, parent[v]):
            break

    if start == -1:
        return None, None
    
    e = edge(start, end)
    x = M_frac[e]
    cycle.append(e)
    epsilon = min(x, 1 - x)
    z = end
    while z != start:
        e = edge(z, parent[z])
        x = M_frac[e]
        cycle.append(e)
        epsilon = min(epsilon, min(x, 1 - x))
        z = parent[z]
    
    return cycle, epsilon
