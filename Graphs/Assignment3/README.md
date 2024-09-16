# Paths in Graphs 1
## Table of Content

## Problem Introduction
You would like to compute the minimum number of flight segments to get from one city to another one. For
this, you construct the following undirected graph: vertices represent cities, there is an edge between two
vertices whenever there is a flight between the corresponding two cities. Then, it suffices to find a shortest
path from one of the given cities to the other one.

## Notes for the Paths in Graph 1

### Fastest Route
There are a lot of different algorithms for finding the fastest path within a weighted graph. The algorithm discussed and used to find the fastest route home from work or vice versa. I am using the Dijkstra's Algorithm to solve this graph and learn the concept of the optimal route and how they can differ based on the weights of the edges in the graph. 

The lecture introduces the idea of nodes and edges in a graph where nodes represent the points on a graph and the edge represents the connections between the points. I learned that the algorithm works by finding the closest node to the starting point and then considering all possible paths from that node to other nodes. I am building the intuition on how the algorithm works and highlights the importance of considering all possible paths to find the shortest or fastest route.

## Problem Description
Task. Given an undirected graph with 𝑛 vertices and 𝑚 edges and two vertices 𝑢 and 𝑣, compute the length
of a shortest path between 𝑢 and 𝑣 (that is, the minimum number of edges in a path from 𝑢 to 𝑣).
## Input Format
A graph is given in the standard format. The next line contains two vertices 𝑢 and 𝑣.
## Constraints
2 ≤ 𝑛 ≤ 105, 0 ≤ 𝑚 ≤ 105, 𝑢 ̸= 𝑣, 1 ≤ 𝑢, 𝑣 ≤ 𝑛.
## Output Format 
Output the minimum number of edges in a path from 𝑢 to 𝑣, or −1 if there is no path.
