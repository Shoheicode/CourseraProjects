def gcd(a, b):
    if b == 0:
        return a
    aPrime = a%b

    return gcd(b, aPrime)

def lcm(a, b):
    return (a // gcd(a,b))*b

    assert False


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm(a, b))

