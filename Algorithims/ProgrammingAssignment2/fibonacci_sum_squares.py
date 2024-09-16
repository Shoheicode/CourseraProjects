def pisano_period(m):
    previous, current = 0, 1
    for i in range(m * m):
        previous, current = current, (previous + current) % m
        # Pisano period starts with 0, 1
        if previous == 0 and current == 1:
            return i + 1

def fibonacci_modulo(n, m):
    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m
    return current

def fibonacci_sum_squares(n):
    # Step 1: Find the Pisano period for modulo 10
    pisano_len = pisano_period(10)

    # Step 2: Reduce n using the Pisano period
    n_mod_pisano = n % pisano_len

    # Step 3: Compute F(n) % 10 and F(n+1) % 10
    fib_n = fibonacci_modulo(n_mod_pisano, 10)
    fib_n_plus_1 = fibonacci_modulo((n_mod_pisano + 1), 10)

    # Step 4: Compute (F(n) * F(n+1)) % 10
    result = (fib_n * fib_n_plus_1) % 10

    return result


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_squares(n))
