import sys


def negative_cycle(adj, cost):
    #write your code here
    n = len(adj)
    distance = [10**3]*n
    distance[0]=0
    for _ in range (n-1):
        for u in range (n):
            for i,v in enumerate(adj[u]):
                if distance[v]>distance[u]+cost[u][i]:
                    distance[v]=distance[u]+cost[u][i]
    
    for u in range (n):
        for i,v in enumerate(adj[u]):
            if distance[v]>distance[u]+cost[u][i]:
                return 1
            
    return 0


if __name__ == '__main__':
    n,m=map(int,input().split())
    edges=[list(map(int,input().split())) for i in range (m)]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for edge in edges:
        a,b,w=edge
        adj[a-1].append(b-1)
        cost[a-1].append(w)
    print(negative_cycle(adj, cost))