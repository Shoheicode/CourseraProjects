# To compute the n-th Fibonacci number modulo m, we can take advantage of the Pisano period, which is the 
# length of the repeating cycle of Fibonacci numbers modulo m. Here's the approach to efficiently solve this problem:

# Key Concepts:
# Pisano Period: The Fibonacci sequence modulo m is periodic, and the length of the cycle is called the Pisano 
# period. Knowing the Pisano period allows us to reduce the computation by mapping large Fibonacci indices to smaller ones.

# Modulo Reduction: Instead of directly computing the large Fibonacci number, we first reduce n using the Pisano period. 
# Once we know the Pisano period, we compute n % P, where P is the length of the Pisano period, and calculate the 
# reduced Fibonacci number.

# Steps to Solve:
# Find the Pisano Period: First, we need to compute the Pisano period for m. This can be done by generating the 
# Fibonacci sequence modulo m until we find a repetition of the pair (0, 1), which indicates the start of a new cycle.

# Reduce n modulo the Pisano period: Once we know the Pisano period P, reduce n by computing n % P.
# Compute the Fibonacci Number: Using the reduced n, compute the Fibonacci number modulo m.

def pisano_period(m):
    previous, current = 0, 1
    for i in range(m * m):  # Pisano period length is at most m*m
        previous, current = current, (previous + current) % m
        # A Pisano period starts with 0, 1
        if previous == 0 and current == 1:
            return i + 1

def fibonacci_huge(n, m):
    # Step 1: Find the Pisano period for m
    pisano_len = pisano_period(m)

    # Step 2: Reduce n modulo the Pisano period
    n = n % pisano_len

    # Step 3: Compute the n-th Fibonacci number modulo m
    previous, current = 0, 1
    
    if n == 0:
        return 0
    elif n == 1:
        return 1

    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fibonacci_huge(n, m))
