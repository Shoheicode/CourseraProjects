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
