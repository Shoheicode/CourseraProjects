
# Needed to help find the Least Common Multiple
def gcd(a, b):
    if b == 0:
        return a
    aPrime = a%b

    return gcd(b, aPrime)

def lcm(a, b):
    return (a // gcd(a,b))*b

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm(a, b))

