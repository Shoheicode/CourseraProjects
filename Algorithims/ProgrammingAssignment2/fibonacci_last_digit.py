lis = []

def fibonacci_number(n):
    if n <=1:
        return n

    lis = [0] * (n+1)
    lis[0] = 0
    lis[1] = 1

    for i in range(2, n+1):
        lis[i] = (lis[i-1]+lis[i-2]) % 10

    return lis[n]


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
