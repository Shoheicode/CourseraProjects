#This program can work on large numbers

# Naive Function (a,b)
# best = 0
# for d from 1 to a+b
#     if d|a and d|b:
#         best = d
# return best

# Euclidean Algorithm
# The reason is that the greatest common divisor of a and b must be
# The greatest common divisor of a' and b.
# Let a' be the remainder when a is divided by b, then:
# gcd(a,b) = gcd(a', b) = gcd(b, a')

# Proof:
# let d be the greatest common divisor
# Because a' is a remainder, a = a' + bq for some q
# d divides into a nad b if and only if it divide a' and b
# because if d divides a' and b, it divides a' + bq which is a 
# so thus it must be a common divisor

'''
Thus for the algorithim, to find the GCD of a and b, we are going to try and find the
greatest common divisor of a' and b and go through the solution recursively.
'''

def gcd(a, b):
    # Base case, when b == 0, it means that a is the highest gcd
    if b == 0:
        return a
    aPrime = a%b

    return gcd(b, aPrime)


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd(a, b))
