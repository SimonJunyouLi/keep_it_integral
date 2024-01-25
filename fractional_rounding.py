from utils.longest_path import get_longest_path
from utils.misc import edge, is_integral
from utils.cycle import get_cycle

graph = {}
M_frac = {}
M_integral = []
n = 0

def round_fractional_matching():
    cycle, epsilon = get_cycle(graph, n, M_frac)

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
    
        cycle, epsilon = get_cycle(graph, n, M_frac)
    
    while len(graph) > 0:
        longest_path, epsilon = get_longest_path(n, graph, M_frac)
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