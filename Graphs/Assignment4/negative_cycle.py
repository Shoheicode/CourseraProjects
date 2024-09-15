#Uses python3

import math
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
    # for i in range(len(adj)-1):
    #     # print("I VALUES", i)
    #     for j in range(len(adj[i])):
    #         relax(i, adj[i][j], cost[i][j])
    
    # # print(prev)
    # # print(dis)

    # cost = 0
    # for i in range(len(adj)):
    #     start = i
    #     next = None
    #     while start != next:
    #         if prev[i] == None:
    #             break
    #         next = prev[i]
    #         i = next
    #     if dis[start] < 0:
    #         return 1
    #     cost = 0
        

    # #write your code here
    # return 0
    # Initialize distances from source
    dist = [float('inf')] * n
    dist[0] = 0  # You can start from any arbitrary node, here we choose node 0
    
    # Perform relaxation for n-1 times
    for _ in range(n - 1):
        for u, v, weight in edges:
            if dist[u] != float('inf') and dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
    
    # Check for negative weight cycle
    for u, v, weight in edges:
        if dist[u] != float('inf') and dist[u] + weight < dist[v]:
            return 1  # Negative cycle found
    
    return 0  # No negative cycle


if __name__ == '__main__':
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
    n, m = map(int, input().split())  # n: number of vertices, m: number of edges
    edges = []
    for _ in range(m):
        u, v, r_ij = map(int, input().split())  # u, v are vertices, r_ij is the exchange rate
        edges.append((u - 1, v - 1, -math.log(r_ij)))  # Convert exchange rate to negative log
    
    # Run Bellman-Ford algorithm to detect negative cycle
    print(negative_cycle(n, edges))

