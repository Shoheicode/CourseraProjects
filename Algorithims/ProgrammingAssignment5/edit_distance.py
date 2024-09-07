def edit_distance(first_string, second_string):
    # Initialize a DP table
    n, m = len(A), len(B)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Base case: edit distance of empty strings
    for i in range(1, n + 1):
        dp[i][0] = i  # Deleting all characters in A
    for j in range(1, m + 1):
        dp[0][j] = j  # Inserting all characters in B

    # Fill the table using the recurrence relation
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # No change needed
            else:
                dp[i][j] = min(
                    dp[i - 1][j] + 1,   # Deletion
                    dp[i][j - 1] + 1,   # Insertion
                    dp[i - 1][j - 1] + 1  # Substitution
                )

    # The result is the edit distance between A and B
    return dp[n][m]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
