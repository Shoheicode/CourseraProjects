# Uses python3
import sys

# To compute the last digit of the partial sum of Fibonacci numbers from 
# Fm to Fn, i.e., S(m,n)=Fm + Fm+1 + ⋯ +Fn
 
# we can use the fact that the sum of Fibonacci numbers from F0 to Fn can be computed using a known identity:

# S(0,n)=Fn+2 −1

# Thus, the sum of Fibonacci numbers from Fm to Fn can be derived by subtracting the sum of the first m−1 Fibonacci numbers 
# from the sum of the first n Fibonacci numbers:
# S(m,n)=S(0,n)−S(0,m−1)=(F_n+2_−1)−(F_m+1_−1)
# This simplifies to:

# S(m,n)=F_n+2_−F_m+1_
# ​
 
# We only care about the last digit, so the problem is reduced to calculating:

# (
# 𝐹
# 𝑛
# +
# 2
# −
# 𝐹
# 𝑚
# +
# 1
# )
# m
# o
# d
#  
#  
# 10
# (F 
# n+2
# ​
#  −F 
# m+1
# ​
#  )mod10
# Steps:
# Pisano Period: The Fibonacci sequence modulo 10 has a periodic nature (Pisano period), which we will use to reduce the indices 
# 𝑛
# +
# 2
# n+2 and 
# 𝑚
# +
# 1
# m+1.

# Fibonacci Modulo: We compute the Fibonacci numbers 
# 𝐹
# 𝑛
# +
# 2
# m
# o
# d
#  
#  
# 10
# F 
# n+2
# ​
#  mod10 and 
# 𝐹
# 𝑚
# +
# 1
# m
# o
# d
#  
#  
# 10
# F 
# m+1
# ​
#  mod10.

# Modulo Calculation: Finally, we calculate the difference modulo 10.

def pisano_period(m):
    previous, current = 0, 1
    for i in range(m * m):  # Pisano period length is at most m*m
        previous, current = current, (previous + current) % m
        # A Pisano period starts with 0, 1
        if previous == 0 and current == 1:
            return i + 1

def fibonacci_modulo(n, m):
    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m
    return current

def fibonacci_partial_sum(m, n):
    # Step 1: Find the Pisano period for modulo 10
    pisano_len = pisano_period(10)

    # Step 2: Compute F(n+2) % 10 and F(m+1) % 10
    n_plus_2 = (n + 2) % pisano_len
    m_plus_1 = (m + 1) % pisano_len

    fib_n_plus_2_mod_10 = fibonacci_modulo(n_plus_2, 10)
    fib_m_plus_1_mod_10 = fibonacci_modulo(m_plus_1, 10)

    # Step 3: Calculate the result (F(n+2) - F(m+1)) % 10
    result = (fib_n_plus_2_mod_10 - fib_m_plus_1_mod_10) % 10

    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum(from_, to))
