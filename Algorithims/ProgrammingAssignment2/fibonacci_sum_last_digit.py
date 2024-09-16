

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
