from sys import stdin

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
