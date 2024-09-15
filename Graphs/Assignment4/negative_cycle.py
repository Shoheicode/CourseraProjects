#Uses python3

import sys

def negative_cycle(n, edges):
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

    dist = [10**3] * n
    dist[0] = 0  # Start from an arbitrary vertex, here vertex 1 (index 0)
    
    # Step 2: Relax all edges n-1 times
    for _ in range(n):
        for u, v, w in edges:
            if dist[u] != 10**3 and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    
    # Step 3: Check for negative-weight cycle by trying to relax once more
    for u, v, w in edges:
        if dist[u] != 10**3 and dist[u] + w < dist[v]:
            return 1  # Negative cycle detected
    
    return 0  # No negative cycle

if __name__ == '__main__':
    n, m = map(int, input().split())  # n: number of vertices, m: number of edges
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())  # u: start vertex, v: end vertex, w: weight of edge
        edges.append((u - 1, v - 1, w))  # Convert to 0-based index
    
    print(negative_cycle(n, edges))
