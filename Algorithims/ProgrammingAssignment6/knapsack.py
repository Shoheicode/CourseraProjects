from sys import stdin

# Explanation:
# Dynamic Programming Table:
# The table 
# dp
# [
# 𝑖
# ]
# [
# 𝑤
# ]
# dp[i][w] stores the maximum weight we can carry with the first 
# 𝑖
# i gold bars and a backpack of capacity 
# 𝑤
# w.
# We initialize the table with 0, as with zero items or zero capacity, the maximum weight is zero.
# Filling the Table:

# For each gold bar 
# 𝑖
# i, we consider two options:
# Don't take the bar: 
# dp
# [
# 𝑖
# ]
# [
# 𝑤
# ]
# =
# dp
# [
# 𝑖
# −
# 1
# ]
# [
# 𝑤
# ]
# dp[i][w]=dp[i−1][w]
# Take the bar if it fits: 
# dp
# [
# 𝑖
# ]
# [
# 𝑤
# ]
# =
# max
# ⁡
# (
# dp
# [
# 𝑖
# ]
# [
# 𝑤
# ]
# ,
# dp
# [
# 𝑖
# −
# 1
# ]
# [
# 𝑤
# −
# 𝑤
# 𝑖
# ]
# +
# 𝑤
# 𝑖
# )
# dp[i][w]=max(dp[i][w],dp[i−1][w−w 
# i
# ​
#  ]+w 
# i
# ​
#  )
# Final Answer:

# The result is stored in 
# dp
# [
# 𝑛
# ]
# [
# 𝑊
# ]
# dp[n][W], which gives the maximum weight we can carry with all the gold bars considered and the given capacity 
# 𝑊
# W.

def maximum_gold(capacity, weights):
    n = len(weights)
    # Create a 2D DP table with (n+1) rows and (W+1) columns
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Fill the table using the recurrence relation
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            dp[i][w] = dp[i - 1][w]  # Don't take the i-th bar
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i][w], dp[i - 1][w - weights[i - 1]] + weights[i - 1])

    # The maximum weight that can be put into the backpack is in dp[n][W]
    return dp[n][capacity]


if __name__ == '__main__':
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == n

    print(maximum_gold(input_capacity, input_weights))
