#Uses python3

import sys


def acyclic(adj):
    #print(adj)
    count= 0
    visited = []
    def explore(vertex):
        visited.append(vertex)
        for i in adj[vertex]:
            if i in visited:
                return 1
        
        return 0
    
    count = explore(0)

    return count

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
