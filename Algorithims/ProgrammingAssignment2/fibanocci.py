lis = []

def fibonacci_number(n):
    # Base cases, checks if n = 0 or 1 and returns accordingly
    if n == 0:
        return 0
    if n == 1:
        return 1

    lis = [0] * (n+1)
    lis[0] = 0
    lis[1] = 1

    for i in range(2, n+1):
        lis[i] = lis[i-1]+lis[i-2]

    return lis[n]


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
