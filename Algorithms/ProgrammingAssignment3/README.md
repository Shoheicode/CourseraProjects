# Programming Assignment 3: Greedy Algorithm

## Description:

## What is a Greedy Algorithm?
A greedy algorithm is an approach for solving problems by making a series of choices, each of which looks the best at the moment. The key idea behind greedy algorithms is to make a decision that seems optimal at every step, with the hope that these locally optimal solutions will lead to a globally optimal solution.

Characteristics of Greedy Algorithms:
1. <b>Greedy choice property</b>: At each step, the algorithm chooses the best option available without considering future consequences.
2. <b>Optimal substructure</b>: A problem exhibits optimal substructure if an optimal solution can be constructed from optimal solutions of its subproblems.

In order to make a Greedy Algorithm, you must have a Greedy Strategy.

A Greedy Strategy is basically:
- Make some greedy choice
- Reduce to a smaller problem (aka subproblem)
- Iterate

Subproblems are defined as:
A similar problem of smaller size.

Safe Move:
A greedy choice is called safe move if there is an optimal solution consistent with this first move.
