# AUTHORS:
# Edison Ye (376334)
# Junyou Li (376330)
# Jacob Prud'homme (352428)

from collections import deque

graph = {}
M_frac = {}
M_integral = []
n = 0

def edge(u, v):
    if u < v:
        return (u, v)
    return (v, u)

def is_integral(x):
    return abs(x - 1) < 1e-5 or abs(x - 0) < 1e-5

def get_cycle():
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

def get_longest_path():
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

def round_fractional_matching():
    cycle, epsilon = get_cycle()

    while cycle:
        c = [[], []]
        num_rounded = [0, 0]
        k = 1

        for e in cycle:
            X = (M_frac[e] + k * epsilon, M_frac[e] - k * epsilon)
            for i, x in enumerate(X):
                if is_integral(x):
                    c[i].append(int(round(x)))
                    num_rounded[i] += 1
                else:
                    c[i].append(x)
            k = -k
        
        updates = c[0] if num_rounded[0] > num_rounded[1] else c[1]

        for i, e in enumerate(cycle):
            M_frac[e] = updates[i]
            if is_integral(updates[i]):
                u, v = e
                graph[u].pop(v)
                graph[v].pop(u)
                if len(graph[u]) == 0:
                    graph.pop(u)
                if len(graph[v]) == 0:
                    graph.pop(v)
                if updates[i] == 1:
                    M_integral.append(e)
    
        cycle, epsilon = get_cycle()
    
    while len(graph) > 0:
        longest_path, epsilon = get_longest_path()
        p = [[], []]
        num_rounded = [0, 0]
        k = 1

        for e in longest_path:
            X = (M_frac[e] + k * epsilon, M_frac[e] - k * epsilon)
            for i, x in enumerate(X):
                if is_integral(x):
                    p[i].append(int(round(x)))
                    num_rounded[i] += 1
                else:
                    p[i].append(x)
            k = -k
        
        updates = p[0] if num_rounded[0] > num_rounded[1] else p[1]

        for i, e in enumerate(longest_path):
            M_frac[e] = updates[i]
            if is_integral(updates[i]):
                u, v = e
                graph[u].pop(v)
                graph[v].pop(u)
                if len(graph[u]) == 0:
                    graph.pop(u)
                if len(graph[v]) == 0:
                    graph.pop(v)
                if updates[i] == 1:
                    M_integral.append(e)

n, m = map(int, input().split())

for _ in range(m):
    u, v, x = map(float, input().split())
    M_frac[edge(int(u), int(v))] = x

for e, x in M_frac.items():
    if is_integral(x):
        if (int(round(x)) == 1):
            M_integral.append(e)
        continue

    u, v = e
    if u not in graph:
        graph[u] = {}
    if v not in graph:
        graph[v] = {}

    graph[u][v] = True
    graph[v][u] = True

round_fractional_matching()

for i in M_integral:
    print(i[0], i[1])