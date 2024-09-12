#Uses python3

import sys


def toposort(adj):
    used = [False] * len(adj)
    order = []

    def dfs(x):
        used[x] = True
        for neighbor in adj[x]:
            if not used[neighbor]:
                dfs(neighbor)
        order.append(x)

    # Step 4: Apply DFS for each unvisited node
    for i in range(len(adj)):
        if not used[i]:
            dfs(i)
    
    #write your code here
    order.reverse()
    return order

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')

