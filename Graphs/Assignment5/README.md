# Minimum Spanning Trees

## Description:
In this Assignment/section, I studied the minimum spanning tree problem. I learned two elegant greedy algorithms for this problem: the first one is due to Kruskal and uses the disjoint sets data structure, the second one is due to Prim and uses the priority queue data structure. 

In the programming assignment for this module, I computed an optimal way of building roads between cities and an optimal way of partitioning a given set of objects into clusters (a fundamental problem in data mining).

## Learning Objectives
- Explain what a spanning tree is
- Describe algorithms for computing minimum spanning trees
- Create an efficient program for clustering

## Cut Property
In their video lecture, we learned about the cut property, which is a lemma that justifies the safety of the strategies used in Kruskal's Algorithm and Prim's Algorithm for finding minimum spanning trees. The cut property states that if we have a graph with a set of edges and a subset of edges called X, which is known to be part of some optimal solution, and the vertices are partitioned into two parts, then if we add the lightest edge that joins the vertices from different parts to X, the resulting set of edges will also be part of a minimum spanning tree. The video provides a formal statement of the lemma and explains its proof using a small example. Understanding the cut property helps us understand why the strategies used in Kruskal's Algorithm and Prim's Algorithm are safe and can lead to optimal solutions.

The cut property is significant in ensuring the optimality of the solutions obtained by Kruskal's Algorithm and Prim's Algorithm. The cut property states that if we have a graph with a set of edges and a subset of edges called X, which is known to be part of some optimal solution, and the vertices are partitioned into two parts, then if we add the lightest edge that joins the vertices from different parts to X, the resulting set of edges will also be part of a minimum spanning tree.

By proving the cut property, we can show that the strategies used in Kruskal's Algorithm and Prim's Algorithm are safe. This means that if at any step we have a subset of edges, X, which is a subset of some optimal solution, adding the next edge according to the strategies used in these algorithms will also result in a set of edges that is part of some optimal solution. This justifies that the algorithms will eventually construct a minimum spanning tree.

In other words, the cut property ensures that the edges selected by Kruskal's Algorithm and Prim's Algorithm are always safe choices that contribute to the optimality of the final solution. It guarantees that the algorithms will find the minimum spanning tree by iteratively adding edges that maintain the acyclic property and connect the tree to new vertices.

## Kruskal's Algorithm
The Kruskal Algorithm is used to find the minimum spanning tree of a graph.

Imagine you have a graph with a bunch of vertices (points) and edges (lines connecting the vertices). The goal is to find a tree that connects all the vertices with the minimum total weight. The Kruskal Algorithm helps us do that.

Here's how it works:
1. We start with an empty set of edges.
2. We sort all the edges in the graph by their weight, from smallest to largest.
3. We go through each edge in order and add it to the set of edges if it doesn't create a cycle.
4. To check if adding an edge creates a cycle, we use a data structure called disjoint sets.
5. If adding the edge doesn't create a cycle, we add it to the set of edges and merge the sets that contain the vertices of the edge.
6. We repeat this process until we have a tree that connects all the vertices.

The Kruskal Algorithm guarantees that the tree we find is the minimum spanning tree, meaning it has the smallest total weight among all possible trees that connect all the vertices. It's a clever and efficient way to solve this problem!

## Prim's Algorithm
We learned about Prim's Algorithm, which is a method for finding the minimum spanning tree of a graph. A minimum spanning tree is a tree that connects all the vertices of a graph with the minimum total weight.

Here's a breakdown of the algorithm:
1. We start with an empty tree and gradually grow it by adding vertices.
2. At each iteration, we select the vertex that can be attached to the current tree by the lightest possible edge.
3. To quickly find the vertex with the smallest weight, we use a priority queue data structure.
4. We update the priorities of the vertices based on the edges that connect them to the current tree.
5. We repeat this process until all vertices are included in the tree.

The algorithm ensures that the resulting tree is a minimum spanning tree, meaning it has the smallest total weight among all possible spanning trees of the graph.

To summarize, Prim's Algorithm grows a tree by attaching vertices with the lightest possible edges. It uses a priority queue to efficiently find the next vertex to add. By following this greedy strategy, we can find the minimum spanning tree of a graph.
