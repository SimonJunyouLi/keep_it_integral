def round_fractional_matching(n, m, edges):
    integral_matching = []  # List to store the integral matching

    # Sort the edges in descending order of fractional contribution
    edges.sort(key=lambda x: -x[2])

    # Initialize sets to keep track of nodes that have been matched
    left_matched = set()
    right_matched = set()

    # Iterate through the sorted edges
    for u, v, x in edges:
        u = int(u)
        v = int(v)

        # If both nodes u and v are not matched, add the edge to the integral matching
        if u not in left_matched and v not in right_matched:
            integral_matching.append((u, v))
            left_matched.add(u)
            right_matched.add(v)

    return integral_matching

# Read input
n, m = map(int, input().split())
edges = []
for _ in range(m):
    u, v, x = map(float, input().split())
    edges.append((u, v, x))

integral_matching = round_fractional_matching(n, m, edges)

# Output the integral matching
for u, v in integral_matching:
    print(f"{int(u)} {int(v)}")
