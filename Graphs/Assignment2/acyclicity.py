#Uses python3

import sys


def acyclic(adj):
    #print(adj)
    count= 0
    visited = [0] * len(adj)
    def explore(vertex):
        if visited[vertex] == 1:
            return True
        if visited[vertex] == 2:
            return False
        
        visited[vertex] == 1
        for i in adj[vertex]:
            if explore(i):
                return True
        
        visited[vertex] == 2
        return False
    
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
