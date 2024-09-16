# The problem is to find the last digit of the sum of the first n Fibonacci numbers. 
# The key insight here is to use the property of Fibonacci sums and the fact that the Fibonacci 
# sequence follows a periodic cycle modulo 10 (Pisano period).

# Key Observations:
# The sum of the first n Fibonacci numbers, S(n) = F0 + F1 + ... + Fn, can be derived from a known formula:

# S(n)=F(n+2)−1
# This means that the sum of the first n Fibonacci numbers is equal to the (n+2)-th Fibonacci number minus 1.

# We only need the last digit of this sum, so the problem boils down to computing:
# (F(n+2)mod10)−1
# and handling the modulo operation carefully.

# The Fibonacci sequence modulo 10 repeats every 60 terms (Pisano period for modulo 10 is 60).

# Plan:
# Compute the Pisano period for modulo 10 (which is 60).
# Reduce the index n + 2 to within the Pisano period by taking it modulo 60.
# Compute the Fibonacci number for this reduced index.
# Subtract 1 and return the result modulo 10.

def fibonacci_sum(n):
    pisano_period = 60

    # Step 1: Find F(n+2) % 10
    def fibonacci_modulo(m):
        if m <= 1:
            return m

        previous, current = 0, 1
        for _ in range(m - 1):
            previous, current = current, (previous + current) % 10
        return current

    # Step 2: Reduce n+2 by Pisano period
    reduced_n = (n + 2) % pisano_period

    # Step 3: Compute F(reduced_n) % 10
    fib_n_plus_2_mod_10 = fibonacci_modulo(reduced_n)

    # Step 4: Compute result (F(n+2) - 1) % 10
    result = (fib_n_plus_2_mod_10 - 1) % 10
    return result


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum(n))

# Time Complexity:
# Since we compute Fibonacci numbers in a linear fashion up to 60 iterations (Aka constant time) (due to the Pisano period), 
# the time complexity is O(1), making it efficient even for very large n.
