#Uses python3

import sys
import queue


def distance(adj, cost, s, t):
    # set a list called distance to store the distance being infinity 
    dis = [float('inf')] * len(adj)
    prev = [None] * len(adj)
    dis[s] = 0

    priorityQ = queue.PriorityQueue()
    priorityQ.put((0,s))
   

    while not priorityQ.empty():
        disT, minIn = priorityQ.get()

        print("Distance:", disT)
        print("Minimum Index: ", minIn)
        
        for i in range(len(cost[minIn])):
            print(dis[i])
            v = adj[minIn][i]
            if dis[v] > dis[minIn] + cost[minIn][i]:
                dis[v] = dis[minIn] + cost[minIn][i]
                prev[v] = minIn

                priorityQ.put((dis[v], v))

    print("Adjacency list")
    for i in adj:
        print(i)
    print("Cost list")
    for a in cost:
        print(a)
    #write your code here
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
