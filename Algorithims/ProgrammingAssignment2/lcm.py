# Least Common Multiple (LCM):
# The LCM of two numbers is defined as the smallest integer which is a multiple of both integers. 
# LCM of an array is the smallest possible integer that is multiple of all the elements of the array.

# Needed to help find the Least Common Multiple
def gcd(a, b):
    if b == 0:
        return a
    aPrime = a%b

    return gcd(b, aPrime)

# This is the algorithm used to find the least common multiple
def lcm(a, b):
    return (a // gcd(a,b))*b

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm(a, b))

