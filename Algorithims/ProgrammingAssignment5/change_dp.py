def change(money):
    # Initialize a list to store the minimum coins for each amount up to 'money'
    dp = [float('inf')] * (money + 1)
    
    # Set the base case: 0 money requires 0 coins
    dp[0] = 0
    
    # Iterate through each amount from 1 to 'money'
    for i in range(1, money + 1):
        # Compute the minimum coins required for amount 'i'
        if i >= 1:
            dp[i] = min(dp[i], dp[i - 1] + 1)  # Using a 1-coin
        if i >= 3:
            dp[i] = min(dp[i], dp[i - 3] + 1)  # Using a 3-coin
        if i >= 4:
            dp[i] = min(dp[i], dp[i - 4] + 1)  # Using a 4-coin
    
    # The result will be the minimum coins required to make 'money'
    return dp[money]


if __name__ == '__main__':
    m = int(input())
    print(change(m))