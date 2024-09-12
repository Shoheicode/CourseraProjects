#Uses python3

import sys

def dfs(adj, used, order, x):
    used[x] = True
    for neighbor in adj[x]:
        if not used[neighbor]:
            dfs(neighbor)
    order.append(x)


def toposort(adj):
    used = [0] * len(adj)
    order = []

    # Step 4: Apply DFS for each unvisited node
    for i in range(n):
        if not used[i]:
            dfs(adj, used, order, i)
    
    #write your code here
    return order[::-1]

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

