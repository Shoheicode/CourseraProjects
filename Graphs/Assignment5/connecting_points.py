#Uses python3
import sys
import math
import heapq

def minimum_distance(x, y):
    n = len(x)
    result = 0.
    visited = [False] * n
    min_edge = [float('inf')] * n
    min_edge[0] = 0  # Starting from the first point
    pq = [(0, 0)]  # (edge weight, point index)

    while pq:
        current_length, u = heapq.heappop(pq)
        
        if visited[u]:
            continue
        visited[u] = True
        result += current_length

        for v in range(n):
            if not visited[v]:
                # Calculate the Euclidean distance between points u and v
                distance = math.sqrt((x[u] - x[v]) ** 2 + (y[u] - y[v]) ** 2)
                if distance < min_edge[v]:
                    min_edge[v] = distance
                    heapq.heappush(pq, (distance, v))

    #write your code here
    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
