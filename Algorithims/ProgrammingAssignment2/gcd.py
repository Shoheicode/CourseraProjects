#This program can work on large numbers

# Naive Function (a,b)
# best = 0
# for d from 1 to a+b
#     if d|a and d|b:
#         best = d
# return best


def gcd(a, b):
    # Base case, when b == 0, it means that a is the lowest gcd
    if b == 0:
        return a
    aPrime = a%b

    return gcd(b, aPrime)


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd(a, b))
