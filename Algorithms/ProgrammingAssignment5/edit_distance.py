# Explanation:
# Base Cases:

# When one string is empty, the edit distance is the length of the other string.
# Dynamic Programming Table:

# The table 
# dp
# [
# 𝑖
# ]
# [
# 𝑗
# ]
# dp[i][j] stores the minimum edit distance between the first 
# 𝑖
# i characters of string 
# 𝐴
# A and the first 
# 𝑗
# j characters of string 
# 𝐵
# B.
# Filling the Table:

# For each character pair 
# 𝐴
# [
# 𝑖
# −
# 1
# ]
# A[i−1] and 
# 𝐵
# [
# 𝑗
# −
# 1
# ]
# B[j−1], if they match, no operation is needed.
# If they do not match, we consider all three operations (insert, delete, substitute) and take the minimum.
# Final Answer:

# The value at 
# dp
# [
# 𝑛
# ]
# [
# 𝑚
# ]
# dp[n][m] gives the edit distance between the two entire strings.

def edit_distance(first_string, second_string):
    # Initialize a DP table
    n, m = len(first_string), len(second_string)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Base case: edit distance of empty strings
    for i in range(1, n + 1):
        dp[i][0] = i  # Deleting all characters in A
    for j in range(1, m + 1):
        dp[0][j] = j  # Inserting all characters in B

    # Fill the table using the recurrence relation
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if first_string[i - 1] == second_string[j - 1]:
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
