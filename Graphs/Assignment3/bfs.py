#Uses python3

import sys
import queue

def distance(adj, s, t):
    #first create a list to store the distance from each node
    dis = [0] * len(adj)
    #make all the distances infinity for now so that it will start putting distance later
    for i in range(len(adj)):
        dis[i] = float('inf')
    
    # set the starting point to be zero
    dis[s] = 0

    #Create the queue for the bfs function and put in the index s into the queue as the starting point
    qu = queue.Queue()
    qu.put(s)

    # while the queue is not empty, loop through the possible nodes
    while not qu.empty():
        # Get the index of the next value in the queue
        val = qu.get()
        # loop through the adjacency list at the index val
        for i in adj[val]:
            # if the distance has not been established (infinity), put the index i into the queue. and update the distance at index i to the distance at val plus 1
            if dis[i] == float('inf'):
                qu.put(i)
                dis[i] = dis[val]+1

    # If the distance at index t is infinity, that path from the start s to t is non existant.
    if float('inf') == dis[t]:
        return -1

    #otherwise, return the distance at index t
    return dis[t]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
