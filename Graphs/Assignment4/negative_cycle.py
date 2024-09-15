#Uses python3

import sys

def negative_cycle(adj, cost):
    # dis = [float('inf')] * len(adj)
    # prev = [None] * len(adj)
    
    # def relax(u, v, cos):
    #     # print("u: ", u)
    #     # print("v: ", v)
    #     # print("Cost value: ", cos)
    #     if dis[v] > dis[u] + cos:
    #         dis[v] = dis[u] + cos
    #         prev[v] = u

    # dis[0] = 0

    # # print("ADJACENT LIST", adj)
    # for i in range(len(adj)):
    #     # print("I VALUES", i)
    #     for j in range(len(adj[i])):
    #         relax(i, adj[i][j], cost[i][j])

    # cost = 0
    
    # for i in range(len(adj)):
    #     for j in range(len(adj[i])):
    #         if dis[i] != float('inf') and dis[i] + w < dis[adj[i][j]]:
    #             return 1
    # Step 1: Initialize distances
    dist = [float('inf')] * n
    dist[0] = 0  # Start from an arbitrary vertex, here vertex 1 (index 0)
    
    # Step 2: Relax all edges n-1 times
    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    
    # Step 3: Check for negative-weight cycle by trying to relax once more
    for u, v, w in edges:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            return 1  # Negative cycle detected
    
    return 0  # No negative cycle

if __name__ == '__main__':
    n, m = map(int, input().split())  # n: number of vertices, m: number of edges
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())  # u: start vertex, v: end vertex, w: weight of edge
        edges.append((u - 1, v - 1, w))  # Convert to 0-based index
    
    print(negative_cycle(n, edges))
    # input = sys.stdin.read()
    # data = list(map(int, input.split()))
    # n, m = data[0:2]
    # data = data[2:]
    # edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    # data = data[3 * m:]
    # adj = [[] for _ in range(n)]
    # cost = [[] for _ in range(n)]
    # for ((a, b), w) in edges:
    #     adj[a - 1].append(b - 1)
    #     cost[a - 1].append(w)
    # print(negative_cycle(adj, cost))
