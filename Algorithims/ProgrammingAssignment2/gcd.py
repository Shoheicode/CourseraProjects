#This program can work on large numbers

def gcd(a, b):
    # Base case, when b == 0, it means that a is the lowest gcd
    if b == 0:
        return a
    aPrime = a%b

    return gcd(b, aPrime)


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd(a, b))
