def fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    lis = [0] * (n+1)
    lis[0] = 0
    lis[1] = 1

    for i in range(2, n+1):
        lis[i] = (lis[i-1]+lis[i-2])

    return lis[n] %m


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fibonacci_huge_naive(n, m))
