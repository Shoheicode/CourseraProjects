def compute_operations(n):
    # Initialize DP table
    dp = [0] * (n + 1)  # dp[i] will store the minimum number of operations to reach i
    
    # Compute the minimum number of operations for each number from 2 to n
    for i in range(2, n + 1):
        # Start by considering the operation of subtracting 1
        dp[i] = dp[i - 1] + 1
        
        # Check if i is divisible by 2
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)
        
        # Check if i is divisible by 3
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)
    
    # Reconstruct the sequence of operations by backtracking
    sequence = []
    while n > 0:
        sequence.append(n)
        # Determine which operation was used to get to n
        if n % 3 == 0 and dp[n // 3] == dp[n] - 1:
            n //= 3
        elif n % 2 == 0 and dp[n // 2] == dp[n] - 1:
            n //= 2
        else:
            n -= 1
    
    # Reverse the sequence to start from 1
    sequence.reverse()

    return sequence


if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)
